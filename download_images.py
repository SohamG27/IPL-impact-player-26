"""
Download IPL player images from Wikipedia / Wikimedia Commons.
Run once from d:/IPL to populate static/images/players/
Usage: python download_images.py
"""
import os
import time
import urllib.request

SAVE_DIR = os.path.join("static", "images", "players")
os.makedirs(SAVE_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    )
}

# Verified Wikimedia Commons URLs
PLAYER_IMAGES = {
    # RCB
    "Virat Kohli":        "https://upload.wikimedia.org/wikipedia/commons/1/15/Virat_Kohli_portrait.jpg",
    "Rajat Patidar":      "https://upload.wikimedia.org/wikipedia/commons/3/36/Patidar.jpg",
    "Devdutt Padikkal":   "https://upload.wikimedia.org/wikipedia/commons/e/e5/Devdutt_Padikkal_2023.jpg",
    "Phil Salt":          "https://upload.wikimedia.org/wikipedia/commons/4/4b/2_02_Phil_Salt.jpg",
    "Josh Hazlewood":     "https://upload.wikimedia.org/wikipedia/commons/9/90/RSA_vs_AUS_Day_1_-_Josh_Hazlewood-1_%28cropped%29.jpg",
    "Krunal Pandya":      "https://upload.wikimedia.org/wikipedia/commons/b/b3/Krunal_Pandya_and_Hardik_Pandya_%28cropped%29_%28cropped%29.jpg",

    # CSK
    "MS Dhoni":           "https://upload.wikimedia.org/wikipedia/commons/c/c9/MS_Dhoni.jpg",
    "Ruturaj Gaikwad":    "https://upload.wikimedia.org/wikipedia/commons/2/27/Ruturaj_Gaikwad.jpeg",
    "Shivam Dube":        "https://upload.wikimedia.org/wikipedia/commons/e/eb/Shivam_Dube.jpg",
    "Sanju Samson":       "https://upload.wikimedia.org/wikipedia/commons/7/70/Sanju_Samson_in_PMO_New_Delhi.jpg",
    "Sarfaraz Khan":      "https://upload.wikimedia.org/wikipedia/commons/4/44/Sarfaraz_Khan_Pic2.jpg",

    # MI
    "Rohit Sharma":       "https://upload.wikimedia.org/wikipedia/commons/c/cc/Rohit_Gurunath_Sharma.jpg",
    "Hardik Pandya":      "https://upload.wikimedia.org/wikipedia/commons/f/fc/Hardik_Pandya_in_PMO_New_Delhi.jpg",
    "Suryakumar Yadav":   "https://upload.wikimedia.org/wikipedia/commons/b/b7/Suryakumar_Yadav_in_PMO_New_Delhi.jpg",
    "Jasprit Bumrah":     "https://upload.wikimedia.org/wikipedia/commons/a/ac/Jasprit_Bumrah.jpg",
    "Trent Boult":        "https://upload.wikimedia.org/wikipedia/commons/2/29/Trent_Boult.jpg",
    "Tilak Varma":        "https://upload.wikimedia.org/wikipedia/commons/0/0b/Tilak_Varma_in_March_2026.png",
    "Ishan Kishan":       "https://upload.wikimedia.org/wikipedia/commons/d/d7/Ishan_Kishan.jpg",
    "Mohammed Shami":     "https://upload.wikimedia.org/wikipedia/commons/b/bc/Mohammed_Shami_%28cropped%29.jpg",

    # KKR
    "Sunil Narine":       "https://upload.wikimedia.org/wikipedia/commons/e/ee/Sunil_Narine.jpg",
    "Cameron Green":      "https://upload.wikimedia.org/wikipedia/commons/b/b4/Cameron_Green_fielding_Boxing_Day_2022_%28cropped%29.jpg",
    "Mustafizur Rahman":  "https://upload.wikimedia.org/wikipedia/commons/a/a3/Mustafizur_Rahman_%284%29_%28cropped%29.jpg",
    "Matheesha Pathirana":"https://upload.wikimedia.org/wikipedia/commons/3/38/Matheesha_Pathirana.png",
    "Ajinkya Rahane":     "https://upload.wikimedia.org/wikipedia/commons/9/96/Ajinkya_Rahane_2016_%28cropped%29.jpg",
    "Mitchell Starc":     "https://upload.wikimedia.org/wikipedia/commons/3/38/Mitchell_Starc_2023.jpg",

    # LSG
    "Rishabh Pant":       "https://upload.wikimedia.org/wikipedia/commons/7/77/Rishabh_Pant.jpg",
    "Aiden Markram":      "https://upload.wikimedia.org/wikipedia/commons/c/ca/Aiden_Markram_%28cropped%29.jpg",
    "Karun Nair":         "https://upload.wikimedia.org/wikipedia/commons/d/d8/Karun_nair_With_Rashid_Zirak.jpg",

    # GT
    "Shubman Gill":       "https://upload.wikimedia.org/wikipedia/commons/3/34/Shubman_Gill_2023_%28cropped%29.jpg",
    "Sai Sudharsan":      "https://upload.wikimedia.org/wikipedia/commons/e/e4/Sai_Sudharsan.jpg",
    "Jos Buttler":        "https://upload.wikimedia.org/wikipedia/commons/0/01/Jos_Buttler_in_2023.jpg",
    "Rashid Khan":        "https://upload.wikimedia.org/wikipedia/commons/7/71/Rashid_Khan.jpg",
    "Mohammed Siraj":     "https://upload.wikimedia.org/wikipedia/commons/a/ac/Mohammed_Siraj.jpg",
    "Washington Sundar":  "https://upload.wikimedia.org/wikipedia/commons/2/23/Washington_Sundar.jpg",
    "David Miller":       "https://upload.wikimedia.org/wikipedia/commons/c/c5/DAVID_MILLER_%2815704846295%29.jpg",

    # SRH
    "Travis Head":        "https://upload.wikimedia.org/wikipedia/commons/0/05/Travis_Head_bowling_at_Perth_Stadium%2C_First_Test_Australia_versus_West_Indies%2C_2_December_2022_03_%28cropped%29.jpg",
    "Pat Cummins":        "https://upload.wikimedia.org/wikipedia/commons/b/b5/RSA_vs_AUS_Day_1_-_Pat_Cummins.jpg",
    "Abhishek Sharma":    "https://upload.wikimedia.org/wikipedia/commons/5/5e/Abhishek_Sharma.jpg",
    "Tristan Stubbs":     "https://upload.wikimedia.org/wikipedia/commons/e/e4/Tristan_Stubbs_sa.jpg",

    # DC
    "Kuldeep Yadav":      "https://upload.wikimedia.org/wikipedia/commons/5/5e/Kuldeep_Yadav.jpg",

    # RR
    "Yashasvi Jaiswal":   "https://upload.wikimedia.org/wikipedia/commons/3/3a/Yashasvi_Jaiswal.jpg",
    "Ravindra Jadeja":    "https://upload.wikimedia.org/wikipedia/commons/b/b1/Ravindra_Jadeja_in_2018.jpg",
    "Jofra Archer":       "https://upload.wikimedia.org/wikipedia/commons/d/de/Jofra_Archer_%283%29.jpg",
    "Shimron Hetmyer":    "https://upload.wikimedia.org/wikipedia/commons/8/8a/Shimron_Hetmyer.jpg",
    "Yuzvendra Chahal":   "https://upload.wikimedia.org/wikipedia/commons/d/da/Yuzvendra_Chahal.jpg",

    # PBKS
    "Shreyas Iyer":       "https://upload.wikimedia.org/wikipedia/commons/9/96/Shreyas_Iyer_2021.jpg",
    "Marcus Stoinis":     "https://upload.wikimedia.org/wikipedia/commons/2/2b/2018.01.21.15.22.25-Stoinis_%2839081521620%29.jpg",
    "Arshdeep Singh":     "https://upload.wikimedia.org/wikipedia/commons/2/2c/Arshdeep_Singh_2022.jpg",
}


def safe_filename(name):
    return name.lower().replace(' ', '_') + '.jpg'


def download(player, url):
    # Determine extension from URL
    ext = url.split('?')[0].rsplit('.', 1)[-1].lower()
    if ext not in ('jpg', 'jpeg', 'png', 'webp'):
        ext = 'jpg'
    fname = player.lower().replace(' ', '_') + '.' + ext
    dest = os.path.join(SAVE_DIR, fname)

    # Also check for the .jpg variant (already downloaded)
    jpg_dest = os.path.join(SAVE_DIR, safe_filename(player))
    if os.path.exists(jpg_dest) and os.path.getsize(jpg_dest) > 5000:
        print(f"  [SKIP]  {player}  (already exists)")
        return True
    if os.path.exists(dest) and os.path.getsize(dest) > 5000:
        print(f"  [SKIP]  {player}  (already exists as .{ext})")
        return True

    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        if len(data) < 2000:
            print(f"  [TINY]  {player}  ({len(data)} bytes) -- skipping")
            return False
        with open(dest, 'wb') as f:
            f.write(data)
        print(f"  [OK]    {player}  ({len(data)//1024} KB)")
        return True
    except Exception as e:
        print(f"  [FAIL]  {player}  -> {e}")
        return False


if __name__ == '__main__':
    ok = fail = 0
    for player, url in PLAYER_IMAGES.items():
        result = download(player, url)
        if result:
            ok += 1
        else:
            fail += 1
        time.sleep(0.4)
    print(f"\nDone: {ok} OK  |  {fail} failed")
    print("Players without Wikimedia images will show placeholder.")
