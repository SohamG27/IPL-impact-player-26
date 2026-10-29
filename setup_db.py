import sqlite3
import os

def setup_database():
    db_path = 'ipl_offline_storage.db'
    
    if os.path.exists(db_path):
        os.remove(db_path)
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS master_players (
            player       TEXT PRIMARY KEY,
            team         TEXT,
            base_demand  INTEGER,
            sr           INTEGER,
            hype         INTEGER,
            role         TEXT,
            nationality  TEXT,
            matches      INTEGER,
            batting_avg  REAL,
            wickets      INTEGER,
            bio          TEXT
        )
    ''')
    
    # (player, team, base_demand, sr, hype, role, nationality, matches, batting_avg, wickets, bio)
    players_data = [
        # ── RCB ──────────────────────────────────────────────────────────────
        ('Virat Kohli',      'RCB', 95, 137, 98, 'Batsman',         'Indian',      237, 37.97, 4,
         'The most successful run-scorer in IPL history with over 8,000 runs; legendary aggressive top-order batter and former RCB captain.'),
        ('Rajat Patidar',    'RCB', 85, 142, 80, 'Batsman',         'Indian',       56, 34.20, 0,
         'Explosive middle-order batter known for his stunning century in the 2022 IPL Eliminator; brings flair and consistency for RCB.'),
        ('Devdutt Padikkal', 'RCB', 82, 128, 75, 'Batsman',         'Indian',       47, 28.65, 0,
         'Left-handed opener with elegant strokeplay; promising young talent who rose through RCB ranks.'),
        ('Phil Salt',        'RCB', 88, 155, 85, 'Wicket-Keeper',   'English',      32, 33.40, 0,
         'Explosive England T20I opener; electric bat-pad reflexes and brutal power-hitting make him a match-winner at the top.'),
        ('Josh Hazlewood',   'RCB', 87, 115, 82, 'Bowler',          'Australian',   66, 12.00, 69,
         'World-class Australian pace bowler; lethal with the new ball and death-over specialist capable of taking key wickets.'),
        ('Krunal Pandya',    'RCB', 80, 130, 78, 'All-Rounder',     'Indian',      109, 22.30, 58,
         'Reliable left-arm spinning all-rounder; useful lower-order runs and handy wickets make him a great team balance option.'),

        # ── CSK ──────────────────────────────────────────────────────────────
        ('MS Dhoni',         'CSK', 90, 135, 99, 'Wicket-Keeper',   'Indian',      250, 26.55, 0,
         'Iconic CSK captain and the greatest finisher in IPL history; led CSK to five titles with unmatched calmness under pressure.'),
        ('Ruturaj Gaikwad',  'CSK', 92, 138, 90, 'Batsman',         'Indian',       86, 42.00, 0,
         'IPL 2021 Orange Cap winner and current CSK captain; classical right-hand opener known for big first-up innings.'),
        ('Shivam Dube',      'CSK', 86, 145, 88, 'All-Rounder',     'Indian',       84, 28.40, 20,
         'Hard-hitting left-handed middle-order batter and handy medium-pacer; a key match-winner at No. 5 or 6 for CSK.'),
        ('Sanju Samson',     'CSK', 89, 140, 92, 'Wicket-Keeper',   'Indian',      160, 31.50, 0,
         'Gifted stroke-maker and T20 specialist who combines elegance with aggression; among the most talented batters in India.'),
        ('Rahul Chahar',     'CSK', 80, 120, 75, 'Bowler',          'Indian',       76, 10.00, 81,
         'Leg-spin and googly artist who bamboozles top-order batters in the powerplay; a proven wicket-taker in T20 cricket.'),
        ('Sarfaraz Khan',    'CSK', 78, 132, 70, 'Batsman',         'Indian',       37, 30.10, 0,
         'Aggressive middle-order batter from Mumbai; raw power and hunger make him an exciting finisher for CSK.'),

        # ── MI ───────────────────────────────────────────────────────────────
        ('Rohit Sharma',     'MI',  92, 130, 96, 'Batsman',         'Indian',      243, 30.35, 15,
         'Five-time IPL-winning captain for Mumbai Indians; one of the greatest T20 batters with devastating pull shots.'),
        ('Hardik Pandya',    'MI',  85, 145, 88, 'All-Rounder',     'Indian',      128, 27.80, 75,
         'Dynamic pace-bowling all-rounder; match-winning with both bat and ball, current MI captain known for high-pressure performances.'),
        ('Suryakumar Yadav', 'MI',  94, 152, 95, 'Batsman',         'Indian',      144, 33.68, 0,
         'The reigning ICC T20I No. 1 batter; 360-degree strokeplay and unmatched consistency make him MI\'s most dangerous weapon.'),
        ('Jasprit Bumrah',   'MI',  98, 110, 97, 'Bowler',          'Indian',      135, 4.00,  145,
         'The world\'s best fast bowler; unique slingy action, deadly yorkers and toe-crushing bouncers make him nearly unplayable.'),
        ('Trent Boult',      'MI',  88, 115, 85, 'Bowler',          'New Zealander', 80, 8.00, 90,
         'Master of swing and seam; deadly with the new ball and brilliant in the powerplay — one of T20 cricket\'s premier pace bowlers.'),
        ('Tilak Varma',      'MI',  84, 135, 80, 'Batsman',         'Indian',       48, 35.40, 0,
         'Young left-handed batter with elegant technique and temperament well beyond his years; MI\'s next big batting star.'),

        # ── KKR ──────────────────────────────────────────────────────────────
        ('Sunil Narine',     'KKR', 90, 160, 92, 'All-Rounder',     'Trinidadian', 175, 24.50, 163,
         'Arguably the most impactful mystery spinner in IPL history; reinvented himself as a devastating powerplay opener for KKR.'),
        ('Rinku Singh',      'KKR', 88, 148, 94, 'Batsman',         'Indian',       58, 38.20, 0,
         'Hero of the famous 5-sixes-off-5-balls IPL over; ice-cool finisher with supernatural calmness under extreme pressure.'),
        ('Cameron Green',    'KKR', 91, 140, 90, 'All-Rounder',     'Australian',   20, 32.00, 12,
         'Imposing Australian all-rounder; fearsome power at the top of the order and useful seam bowling make him a genuine match-winner.'),
        ('Mustafizur Rahman','KKR', 85, 118, 82, 'Bowler',          'Bangladeshi',  77, 6.50,  83,
         'The "Fizz" — Bangladesh\'s greatest T20 bowler; cutter and slower-ball specialist who is devastating in the death overs.'),
        ('Matheesha Pathirana','KKR',87, 120, 85, 'Bowler',         'Sri Lankan',   24, 5.00,  33,
         'Fearsome Sri Lankan slinger with an unorthodox action; vicious yorkers and pace variations make him one of the hottest young bowlers.'),
        ('Ajinkya Rahane',   'KKR', 78, 125, 75, 'Batsman',         'Indian',      105, 25.80, 0,
         'Solid and stylish top-order batter; experienced IPL hand with a reputation for big innings when his team needs it most.'),

        # ── LSG ──────────────────────────────────────────────────────────────
        ('Rishabh Pant',     'LSG', 93, 145, 96, 'Wicket-Keeper',   'Indian',      111, 35.20, 0,
         'The most explosive left-handed batter in T20 cricket; unorthodox strokeplay, electrifying wicket-keeping and sheer audacity define him.'),
        ('Nicholas Pooran',  'LSG', 91, 165, 92, 'Wicket-Keeper',   'West Indian',  88, 28.70, 0,
         'West Indian power-hitter with one of the highest strike rates in IPL; brutal sixes and match-defining cameos.'),
        ('Ayush Badoni',     'LSG', 82, 140, 78, 'Batsman',         'Indian',       37, 30.00, 0,
         'Composed middle-order batter with a knack for crunch-situation innings; rising star of LSG\'s batting lineup.'),
        ('Mohammed Shami',   'LSG', 90, 110, 88, 'Bowler',          'Indian',      105, 5.00,  114,
         'India\'s premier fast bowler; master of swing and seam with the ability to bowl match-winning spells at any stage of the game.'),
        ('Avesh Khan',       'LSG', 83, 115, 75, 'Bowler',          'Indian',       54, 6.00,   60,
         'Tall right-arm pacer with genuine pace and a lethal bouncer; emerging as one of India\'s most reliable IPL fast bowlers.'),
        ('Aiden Markram',    'LSG', 85, 135, 82, 'All-Rounder',     'South African', 30, 32.00, 8,
         'South African batting all-rounder; technically correct opener who can also bowl useful off-spin when conditions demand.'),

        # ── GT ───────────────────────────────────────────────────────────────
        ('Shubman Gill',     'GT',  94, 135, 95, 'Batsman',         'Indian',       98, 42.10, 0,
         'India\'s next great batting star; elegant technique, prolific IPL runs and a consistent ability to dominate all bowling types.'),
        ('Sai Sudharsan',    'GT',  86, 132, 82, 'Batsman',         'Indian',       34, 38.50, 0,
         'Technically gifted left-hander who shot to fame with a stunning 96 in the IPL 2023 final; very bright future ahead.'),
        ('Jos Buttler',      'GT',  92, 150, 96, 'Wicket-Keeper',   'English',     107, 40.00, 0,
         'Two-time Orange Cap winner; one of the most dangerous T20 openers in the world — "The Butts" turns up in the biggest games.'),
        ('Rashid Khan',      'GT',  96, 140, 98, 'Bowler',          'Afghan',      113, 15.60, 112,
         'The greatest leg-spinner in T20 cricket; unplayable googlies, sub-6 economy and a handy lower-order bat make him truly elite.'),
        ('Mohammed Siraj',   'GT',  87, 112, 84, 'Bowler',          'Indian',       71, 6.50,   73,
         'India\'s No. 1 pace bowler in Tests; sharp reverse swing and consistent line and length make him a wicket-taking machine.'),
        ('Washington Sundar','GT',  82, 125, 78, 'All-Rounder',     'Indian',       56, 22.00,  52,
         'Reliable off-spinning all-rounder; contains runs in the powerplay and contributes handy lower-order runs when needed.'),

        # ── SRH ──────────────────────────────────────────────────────────────
        ('Travis Head',      'SRH', 93, 175, 94, 'Batsman',         'Australian',   28, 43.20, 0,
         'World Cup-winning Aussie opener; highest strike rate at the top for any consistent IPL batter — destroys any powerplay attack.'),
        ('Heinrich Klaasen', 'SRH', 92, 170, 93, 'Wicket-Keeper',   'South African', 62, 36.80, 0,
         'South Africa\'s most destructive middle-order batter; SRH\'s 2024 record-run campaign was powered by his astonishing hitting.'),
        ('Pat Cummins',      'SRH', 95, 135, 97, 'All-Rounder',     'Australian',   58, 20.00,  65,
         'Australia\'s World Cup-winning captain; versatile pace-bowling all-rounder who can win matches in both innings.'),
        ('Abhishek Sharma',  'SRH', 88, 168, 90, 'All-Rounder',     'Indian',       46, 34.00,  18,
         'Explosive left-handed opener and handy left-arm spinner; broke out with record-smashing IPL 2024 season for SRH.'),
        ('Harshal Patel',    'SRH', 84, 120, 82, 'Bowler',          'Indian',       98, 14.00,  105,
         'IPL Purple Cap winner (2021); master of the slower-ball bouncer and change-ups that makes him near-unplayable at death.'),
        ('Ishan Kishan',     'SRH', 86, 140, 85, 'Wicket-Keeper',   'Indian',      105, 32.00, 0,
         'Left-handed aggressive keeper-batter; capable of taking any bowling attack apart from ball one with fearless strokeplay.'),

        # ── DC ───────────────────────────────────────────────────────────────
        ('Tristan Stubbs',   'DC',  88, 160, 85, 'Batsman',         'South African', 24, 30.50, 0,
         'Young South African power-hitter who lit up IPL 2023 for MI; big-hitting middle-order batter with an exceptional future.'),
        ('Kuldeep Yadav',    'DC',  90, 115, 88, 'Bowler',          'Indian',       86, 9.00,   95,
         'India\'s premier wrist-spinner; revived IPL career with DC featuring disguised googlies and a devastating chinaman delivery.'),
        ('David Miller',     'DC',  87, 145, 84, 'Batsman',         'South African', 118, 33.00, 0,
         '\"Killer Miller\" — the most feared T20 finisher from South Africa; ice-cold under pressure with a match-winning six always on tap.'),
        ('Mitchell Starc',   'DC',  91, 120, 88, 'Bowler',          'Australian',   36, 8.00,   44,
         'The most expensive player ever bought at IPL auction; Australia\'s left-arm pace icon known for searing in-swing and reverse-swing.'),
        ('Abishek Porel',    'DC',  78, 135, 70, 'Wicket-Keeper',   'Indian',       18, 27.00,  0,
         'Young Bengal wicket-keeper batter with quick hands and sharp reflexes; an exciting prospect for DC\'s future lineup.'),
        ('Karun Nair',       'DC',  75, 128, 65, 'Batsman',         'Indian',       40, 24.00,  0,
         'Experienced middle-order batter remembered for his 303* in Tests; brings stability and big-game experience to DC.'),

        # ── RR ───────────────────────────────────────────────────────────────
        ('Yashasvi Jaiswal', 'RR',  93, 148, 94, 'Batsman',         'Indian',       39, 44.80,  0,
         'India\'s next superstar opener; from Mumbai\'s chawls to the IPL top-10, his rise is one of cricket\'s greatest stories.'),
        ('Dhruv Jurel',      'RR',  84, 135, 80, 'Wicket-Keeper',   'Indian',       16, 32.00,  0,
         'Young UP wicket-keeper who made a stunning Test debut for India in 2024; calm under pressure with sharp glove-work behind the stumps.'),
        ('Riyan Parag',      'RR',  85, 140, 82, 'All-Rounder',     'Indian',       65, 28.00,  12,
         'Assam\'s big talent; aggressive middle-order batter and part-time spinner who has matured into a key contributor for RR.'),
        ('Ravindra Jadeja',  'RR',  90, 130, 92, 'All-Rounder',     'Indian',      228, 26.50, 135,
         'India\'s greatest cricketing all-rounder; devastating left-arm spin, game-changing fielding and a vital lower-order bat.'),
        ('Jofra Archer',     'RR',  88, 120, 88, 'Bowler',          'English',      35, 6.50,   41,
         'England\'s most talented fast bowler; electric pace, unplayable bouncer and death-over mastery — devastating when fit.'),
        ('Shimron Hetmyer',  'RR',  86, 152, 85, 'Batsman',         'West Indian',  82, 31.20,  0,
         'The Caribbean power-hitter who consistently delivers death-over centuries for RR; brutal hitting mixed with smart cricket.'),

        # ── PBKS ─────────────────────────────────────────────────────────────
        ('Shreyas Iyer',     'PBKS', 90, 132, 91, 'Batsman',        'Indian',      115, 32.80,  3,
         'Stylish and effective middle-order anchor; IPL 2022 championship-winning captain for KKR who reads the game brilliantly.'),
        ('Prabhsimran Singh','PBKS', 81, 145, 75, 'Wicket-Keeper',  'Indian',       24, 30.00,  0,
         'Young hard-hitting Punjab opener with a clean bat swing; expected to be PBKS\'s long-term opener of choice.'),
        ('Marcus Stoinis',   'PBKS', 88, 148, 86, 'All-Rounder',    'Australian',   79, 28.00,  25,
         'Australian big-hitting all-rounder; blitzkrieg power at the top combined with useful medium-pace bowling at any stage.'),
        ('Yuzvendra Chahal', 'PBKS', 89, 110, 88, 'Bowler',         'Indian',      142, 7.50,  187,
         'IPL\'s highest wicket-taker; leg-spin master with a loopy googly and relentless accuracy — wickets in every game.'),
        ('Arshdeep Singh',   'PBKS', 87, 115, 85, 'Bowler',         'Indian',       72, 8.00,   82,
         'India\'s premier death-over specialist left-arm pacer; nail-in yorkers, wide variations and a huge big-game temperament.'),
        ('Nehal Wadhera',    'PBKS', 80, 138, 72, 'Batsman',        'Indian',       18, 26.00,   0,
         'Promising young middle-order batter from Punjab; known for a big six-hitting game and cool-headed finishing abilities.'),
    ]
    
    cursor.executemany('''
        INSERT INTO master_players (player, team, base_demand, sr, hype, role, nationality, matches, batting_avg, wickets, bio)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', players_data)
    
    conn.commit()
    conn.close()
    print(f"Database {db_path} initialized with {len(players_data)} players.")

if __name__ == '__main__':
    setup_database()
