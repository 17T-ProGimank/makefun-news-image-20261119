# The World in One Day — 19 November 2026

Entry for make.fun `news-image-20261119`: one image summing up the
world news of Thursday 19 November 2026.

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

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.
