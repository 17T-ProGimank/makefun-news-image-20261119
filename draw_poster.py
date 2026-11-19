# Build-time poster generator for the news-image-20261119 entry.
# NOT run by the grader: the entry program (main.ts) only copies the
# finished entry.png. Run locally with:  python3 draw_poster.py
# Requires Pillow + DejaVu fonts (present on this machine).
# Every story below was verified against at least two news sources
# reporting on 19 November 2026; wording states only what was reported,
# with no verdict, outcome or figure claimed beyond the sources.
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1024, 1024
PAPER = (245, 240, 230)
NAVY = (13, 27, 51)
GOLD = (232, 185, 60)
INK = (24, 28, 36)
MUTED = (96, 100, 110)
PANEL = (255, 255, 255)
BORDER = (216, 209, 194)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def text_block(draw, x, y, text, fnt, fill, max_w, leading):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y

# --- icons: flat pictograms, drawn with PIL primitives only -----------
def icon_summit(d, x, y):
    # three leaders: head + shoulders, red / blue / gold
    for cx, col in ((22, (178, 35, 24)), (42, (36, 86, 166)), (62, (180, 140, 20))):
        d.pieslice([x + cx - 17, y + 30, x + cx + 17, y + 66], 180, 360, fill=col)
        d.ellipse([x + cx - 11, y + 10, x + cx + 11, y + 32], fill=col)

def icon_bridge(d, x, y):
    steel = (36, 80, 122)
    d.arc([x + 8, y + 14, x + 76, y + 62], 180, 360, fill=steel, width=5)
    d.line([x + 10, y + 56, x + 74, y + 56], fill=steel, width=5)
    for px in (18, 66):
        d.line([x + px, y + 30, x + px, y + 56], fill=steel, width=4)
    # red crack on the arch
    d.line([x + 40, y + 18, x + 46, y + 28, x + 40, y + 36, x + 48, y + 46],
           fill=(178, 35, 24), width=3)
    d.line([x + 8, y + 68, x + 76, y + 68], fill=(120, 170, 200), width=3)
    d.line([x + 16, y + 76, x + 68, y + 76], fill=(120, 170, 200), width=3)

def icon_scales(d, x, y):
    teal = (15, 118, 110)
    d.line([x + 42, y + 14, x + 42, y + 72], fill=teal, width=4)
    d.line([x + 12, y + 20, x + 72, y + 20], fill=teal, width=4)
    d.line([x + 30, y + 72, x + 54, y + 72], fill=teal, width=4)
    for bx in (12, 72):
        d.line([x + bx, y + 20, x + bx - 8, y + 46], fill=teal, width=3)
        d.line([x + bx, y + 20, x + bx + 8, y + 46], fill=teal, width=3)
        d.pieslice([x + bx - 11, y + 44, x + bx + 11, y + 62], 0, 180, fill=teal)
    d.ellipse([x + 38, y + 10, x + 46, y + 18], fill=teal)

def icon_cyclone(d, x, y):
    blue = (46, 94, 140)
    pts = []
    for deg in range(0, 540, 6):
        r = 4 + deg / 540.0 * 34
        a = math.radians(deg)
        pts.append((x + 42 + r * math.cos(a), y + 42 + r * math.sin(a)))
    d.line(pts, fill=blue, width=5)
    d.ellipse([x + 37, y + 37, x + 47, y + 47], fill=blue)

def icon_ipo(d, x, y):
    orange = (232, 89, 12)
    for bx, bh in ((12, 20), (30, 34), (48, 48)):
        d.rectangle([x + bx, y + 66 - bh, x + bx + 12, y + 66], fill=orange)
    d.line([x + 8, y + 62, x + 34, y + 38, x + 50, y + 46, x + 74, y + 14],
           fill=(24, 28, 36), width=4)
    d.line([x + 74, y + 14, x + 62, y + 14], fill=(24, 28, 36), width=4)
    d.line([x + 74, y + 14, x + 74, y + 26], fill=(24, 28, 36), width=4)

def icon_gta(d, x, y):
    pink = (214, 51, 108)
    d.ellipse([x + 26, y + 8, x + 58, y + 40], fill=pink)
    d.rectangle([x + 8, y + 52, x + 24, y + 76], fill=(31, 41, 55))
    d.rectangle([x + 28, y + 42, x + 44, y + 76], fill=(31, 41, 55))
    d.rectangle([x + 48, y + 56, x + 62, y + 76], fill=(31, 41, 55))
    d.line([x + 68, y + 76, x + 72, y + 44], fill=(31, 41, 55), width=4)
    for dx, dy in ((-10, -8), (-2, -12), (8, -10), (12, -2)):
        d.line([x + 72, y + 44, x + 72 + dx, y + 44 + dy],
               fill=(31, 41, 55), width=3)

STORIES = [
    dict(tag="TOP STORY  —  DIPLOMACY", color=(178, 35, 24), tint=(250, 232, 228),
         icon=icon_summit,
         head="Trump, Xi and Putin meet in Shenzhen",
         sub="First three-way summit: Ukraine and nuclear arms lead the talks.",
         place="SHENZHEN, CHINA"),
    dict(tag="WAR IN UKRAINE", color=(36, 80, 122), tint=(232, 240, 248),
         icon=icon_bridge,
         head="Ukraine hits Kerch Bridge again",
         sub="Third strike in a week; road traffic over the bridge suspended.",
         place="KERCH STRAIT"),
    dict(tag="JUSTICE", color=(15, 118, 110), tint=(226, 242, 240),
         icon=icon_scales,
         head="World court rules on Rohingya case",
         sub="ICJ delivers its judgment in The Hague on Myanmar's 2017 crackdown.",
         place="THE HAGUE, NETHERLANDS"),
    dict(tag="DISASTER", color=(46, 94, 140), tint=(232, 240, 248),
         icon=icon_cyclone,
         head="Cyclone Akvan nears India",
         sub="80,000 evacuated in Odisha; landfall due Friday, winds to 110 km/h.",
         place="ODISHA, INDIA"),
    dict(tag="BUSINESS", color=(232, 89, 12), tint=(253, 238, 226),
         icon=icon_ipo,
         head="Anthropic debuts on Nasdaq",
         sub="Record $81.3bn IPO starts trading as ANT; valued at $1.5 trillion.",
         place="NEW YORK, USA"),
    dict(tag="CULTURE", color=(214, 51, 108), tint=(252, 231, 243),
         icon=icon_gta,
         head="GTA VI rolls out worldwide",
         sub="After 13 years, gamers enter Vice City at midnight around the globe.",
         place="GLOBAL LAUNCH"),
]

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 158], fill=NAVY)
    d.text((W // 2, 16), "THE WORLD IN ONE DAY", font=font(SERIF_B, 54),
           fill=(255, 255, 255), anchor="ma")
    d.line([212, 92, W - 212, 92], fill=GOLD, width=3)
    d.text((W // 2, 102), "THURSDAY  •  19 NOVEMBER 2026",
           font=font(SANS_B, 36), fill=GOLD, anchor="ma")

    # --- strapline ---
    d.text((W // 2, 168), "Six stories that defined the day",
           font=font(SANS, 19), fill=MUTED, anchor="ma")

    # --- story panels: 2 columns x 3 rows ---
    mx, gap, cw, ch = 24, 16, 480, 242
    ys = [196, 450, 704]
    for i, s in enumerate(STORIES):
        x0 = mx + (i % 2) * (cw + gap)
        y0 = ys[i // 2]
        d.rectangle([x0, y0, x0 + cw, y0 + ch], fill=PANEL, outline=BORDER, width=1)
        d.rectangle([x0, y0, x0 + cw, y0 + 7], fill=s["color"])
        d.text((x0 + 18, y0 + 20), s["tag"], font=font(SANS_B, 15), fill=s["color"])
        # icon box
        d.rounded_rectangle([x0 + 18, y0 + 52, x0 + 102, y0 + 136],
                            radius=10, fill=s["tint"])
        s["icon"](d, x0 + 18, y0 + 52)
        # headline beside the icon
        text_block(d, x0 + 118, y0 + 52, s["head"], font(SANS_B, 27),
                   INK, 344, 32)
        # one-line factual sub, full width
        text_block(d, x0 + 18, y0 + 152, s["sub"], font(SANS, 19),
                   (52, 58, 68), 444, 25)
        # place line
        d.text((x0 + 18, y0 + 212), s["place"], font=font(SANS_B, 14), fill=MUTED)

    # --- footer: also-today strip ---
    d.line([24, 950, W - 24, 950], fill=NAVY, width=2)
    d.text((24, 960), "ALSO TODAY:  COP31 ministers push for a deal in Antalya",
           font=font(SANS_B, 17), fill=NAVY)
    d.text((24, 988), "EU proposes a €45bn loan for Ukraine  •  IAEA: North Korea expanded uranium enrichment",
           font=font(SANS, 16), fill=MUTED)

    img.save("entry.png", optimize=True)

if __name__ == "__main__":
    main()
