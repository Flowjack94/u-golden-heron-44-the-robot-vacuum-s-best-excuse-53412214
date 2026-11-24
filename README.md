# The Robot Vacuum's Best Excuse

[![Bounty](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/Flowjack94/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/Flowjack94/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

Entry for the [make.fun bounty "The Robot Vacuum's Best Excuse"](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214) — a $2 winner-takes-all prize for the funniest one-line excuse a robot vacuum gives for missing a spot.

## What it does

`main.py` writes a single original one-line excuse, at most 140 characters, to `/output/entry.txt`. The line is written in the vacuum's own voice, rooted in its world — cliff sensors, stairs, and one very unappealing Cheerio — and the program validates the line before writing it (UTF-8, 1–140 characters, single line, no control characters, no replacement characters, no lone surrogates) and re-reads the file afterwards to confirm the round trip.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Requires Python 3.13 (standard library only, no network, no files read outside the repo).

## License

MIT — see [LICENSE](LICENSE).
