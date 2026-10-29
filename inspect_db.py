import sqlite3
conn = sqlite3.connect('ipl_offline_storage.db')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cur.fetchall())
cur.execute("PRAGMA table_info(master_players)")
print("Schema:", cur.fetchall())
cur.execute("SELECT * FROM master_players LIMIT 5")
print("Sample rows:", cur.fetchall())
cur.execute("SELECT COUNT(*) FROM master_players")
print("Total players:", cur.fetchone())
conn.close()

