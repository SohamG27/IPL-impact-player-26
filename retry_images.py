"""
Retry using 250px thumbnails (Wikimedia allowed standard size).
"""
import os
import time
import urllib.request

SAVE_DIR = os.path.join("static", "images", "players")

HEADERS = {
    "User-Agent": "IPLDashboard/1.0 (educational project) Python-urllib/3.10"
}

RETRY_IMAGES = {
    "Suryakumar Yadav":   "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Suryakumar_Yadav_in_PMO_New_Delhi.jpg/250px-Suryakumar_Yadav_in_PMO_New_Delhi.jpg",
    "Jasprit Bumrah":     "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Jasprit_Bumrah.jpg/250px-Jasprit_Bumrah.jpg",
    "Ishan Kishan":       "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Ishan_Kishan.jpg/250px-Ishan_Kishan.jpg",
    "Mohammed Shami":     "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Mohammed_Shami_%28cropped%29.jpg/250px-Mohammed_Shami_%28cropped%29.jpg",
    "Cameron Green":      "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Cameron_Green_fielding_Boxing_Day_2022_%28cropped%29.jpg/250px-Cameron_Green_fielding_Boxing_Day_2022_%28cropped%29.jpg",
    "Matheesha Pathirana":"https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Matheesha_Pathirana.png/250px-Matheesha_Pathirana.png",
    "Mitchell Starc":     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Mitchell_Starc_2023.jpg/250px-Mitchell_Starc_2023.jpg",
    "Rishabh Pant":       "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Rishabh_Pant.jpg/250px-Rishabh_Pant.jpg",
    "Devdutt Padikkal":   "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Devdutt_Padikkal.jpg/250px-Devdutt_Padikkal.jpg",
    "Sai Sudharsan":      "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Sai_Sudharsan.jpg/250px-Sai_Sudharsan.jpg",
    "Washington Sundar":  "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Washington_Sundar.jpg/250px-Washington_Sundar.jpg",
    "David Miller":       "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/DAVID_MILLER_%2815704846295%29.jpg/250px-DAVID_MILLER_%2815704846295%29.jpg",
    "Tristan Stubbs":     "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Tristan_Stubbs_sa.jpg/250px-Tristan_Stubbs_sa.jpg",
    "Kuldeep Yadav":      "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Kuldeep_Yadav.jpg/250px-Kuldeep_Yadav.jpg",
    "Yashasvi Jaiswal":   "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Yashasvi_Jaiswal.jpg/250px-Yashasvi_Jaiswal.jpg",
    "Ravindra Jadeja":    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Ravindra_Jadeja_in_2018.jpg/250px-Ravindra_Jadeja_in_2018.jpg",
    "Yuzvendra Chahal":   "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Yuzvendra_Chahal.jpg/250px-Yuzvendra_Chahal.jpg",
    "Marcus Stoinis":     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/2018.01.21.15.22.25-Stoinis_%2839081521620%29.jpg/250px-2018.01.21.15.22.25-Stoinis_%2839081521620%29.jpg",
    "Arshdeep Singh":     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Arshdeep_Singh_2022.jpg/250px-Arshdeep_Singh_2022.jpg",
}


def already_exists(player):
    for ext in ('jpg', 'jpeg', 'png', 'webp'):
        path = os.path.join(SAVE_DIR, player.lower().replace(' ', '_') + '.' + ext)
        if os.path.exists(path) and os.path.getsize(path) > 3000:
            return True
    return False


def download(player, url):
    if already_exists(player):
        print(f"  [SKIP]  {player}")
        return True
    ext = url.split('?')[0].rsplit('.', 1)[-1].lower()
    if ext not in ('jpg', 'jpeg', 'png', 'webp'):
        ext = 'jpg'
    fname = player.lower().replace(' ', '_') + '.' + ext
    dest = os.path.join(SAVE_DIR, fname)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = resp.read()
        if len(data) < 1500:
            print(f"  [TINY]  {player}  ({len(data)} bytes)")
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
    for player, url in RETRY_IMAGES.items():
        result = download(player, url)
        if result:
            ok += 1
        else:
            fail += 1
        time.sleep(1)
    print(f"\nDone: {ok} OK  |  {fail} failed")
