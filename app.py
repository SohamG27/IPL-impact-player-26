from flask import Flask, render_template, jsonify, request
import pandas as pd
import sqlite3
import json
import plotly
import plotly.graph_objects as go
import os

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('ipl_offline_storage.db')

@app.route('/')
def index():
    conn = get_db_connection()
    players = pd.read_sql('SELECT player, team FROM master_players ORDER BY team, player', conn)
    conn.close()
    # Group by team for the dropdown
    teams = {}
    for _, row in players.iterrows():
        teams.setdefault(row['team'], []).append(row['player'])
    return render_template('index.html', teams=teams)

@app.route('/get_player_data/<player_name>')
def get_player_data(player_name):
    conn = get_db_connection()
    df = pd.read_sql(
        "SELECT * FROM master_players WHERE player=?", conn, params=(player_name,)
    )
    conn.close()
    
    if df.empty:
        return jsonify({"error": "Player not found"}), 404

    p = df.iloc[0]

    # ── Radar / Spider Chart ──────────────────────────────────────────────
    categories = ['Demand', 'Strike Rate', 'Hype', 'Matches', 'Avg']
    # Normalise all metrics to 0-100
    sr_norm    = min(round(p['sr']           / 2.0,  1), 100)
    avg_norm   = min(round(p['batting_avg']  / 0.6,  1), 100)
    mat_norm   = min(round(p['matches']      / 2.5,  1), 100)

    values = [
        p['base_demand'],
        sr_norm,
        p['hype'],
        mat_norm,
        avg_norm,
    ]
    # Close the radar polygon
    values_closed = values + [values[0]]
    cats_closed   = categories + [categories[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values_closed,
        theta=cats_closed,
        fill='toself',
        fillcolor='rgba(255,215,0,0.15)',
        line=dict(color='#FFD700', width=2),
        marker=dict(color='#FFD700', size=8),
        name=player_name,
    ))
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(color='rgba(255,255,255,0.5)', size=10),
                gridcolor='rgba(255,255,255,0.1)',
                linecolor='rgba(255,255,255,0.1)',
            ),
            angularaxis=dict(
                tickfont=dict(color='white', size=13),
                gridcolor='rgba(255,255,255,0.08)',
                linecolor='rgba(255,255,255,0.1)',
            ),
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Outfit, sans-serif', size=13, color='white'),
        margin=dict(l=50, r=50, t=40, b=40),
        showlegend=False,
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # ── Impact Score ─────────────────────────────────────────────────────
    impact_score = round(
        (p['base_demand'] * 0.35) +
        (sr_norm          * 0.15) +
        (p['hype']        * 0.35) +
        (avg_norm         * 0.15),
        1
    )

    # ── Player Image ─────────────────────────────────────────────────────
    safe_name  = player_name.lower().replace(' ', '_')
    img_folder = os.path.join('static', 'images', 'players')
    image_url  = '/static/images/players/placeholder.png'   # default fallback

    for ext in ('jpg', 'jpeg', 'png', 'webp'):
        candidate = os.path.join(img_folder, f'{safe_name}.{ext}')
        if os.path.exists(candidate):
            image_url = f'/static/images/players/{safe_name}.{ext}'
            break

    return jsonify({
        "graph":        graphJSON,
        "team":         p['team'],
        "image":        image_url,
        "impact_score": impact_score,
        "role":         p['role'],
        "nationality":  p['nationality'],
        "matches":      int(p['matches']),
        "batting_avg":  float(p['batting_avg']),
        "wickets":      int(p['wickets']),
        "sr":           int(p['sr']),
        "bio":          p['bio'],
        "hype":         int(p['hype']),
        "demand":       int(p['base_demand']),
    })

if __name__ == '__main__':
    app.run(debug=True)