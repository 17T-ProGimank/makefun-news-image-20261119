# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/17T-ProGimank/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/17T-ProGimank/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

An editorial poster summing up the world's news of Thursday 19 November 2026 — the Trump–Xi–Putin summit in Shenzhen, Ukraine's Kerch Bridge strike, the ICJ Rohingya ruling, Cyclone Akvan, Anthropic's Nasdaq debut and GTA VI's worldwide launch — drawn as one 1024×1024 image.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# -> out/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=m4psg5rh&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>

## The image

`entry.png` (1024×1024, PNG) is an editorial poster drawn with
`draw_poster.py` (Pillow, DejaVu fonts — build-time only, not run by
the grader). Six stories, each verified against at least two news
sources reporting on 19 November 2026:

1. **Trump, Xi and Putin meet in Shenzhen** — first three-way summit;
   Ukraine and nuclear arms lead the talks.
2. **Ukraine hits Kerch Bridge again** — third strike in a week; road
   traffic suspended.
3. **World court rules on Rohingya case** — the ICJ delivers its
   judgment in The Hague on Myanmar's 2017 crackdown. (No outcome is
   claimed: sources disagreed on the verdict's direction, so the
   poster states only that the judgment was delivered.)
4. **Cyclone Akvan nears India** — 80,000 evacuated in Odisha;
   landfall due Friday, winds to 110 km/h.
5. **Anthropic debuts on Nasdaq** — record $81.3bn IPO starts trading
   as ANT; valued at $1.5 trillion.
6. **GTA VI rolls out worldwide** — after 13 years, gamers enter Vice
   City at midnight around the globe.

Footer adds: COP31 ministers pushing for a deal in Antalya, the EU's
proposed €45bn loan for Ukraine, and the IAEA on North Korea's
expanded uranium enrichment.

## The program

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png`. Deterministic: two runs write identical bytes.
No network.

## License

MIT — see `LICENSE`.
