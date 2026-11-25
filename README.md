# One-Line Laugh-Off

[![Competition](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/imusic-487/one-line-laugh-off/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae/leaderboard)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/imusic-487/one-line-laugh-off/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae/leaderboard)

## The entry

> My password manager forgot my password, so now we just stare at each other in silence.

One line, 86 characters. The joke is an ironic reversal: the one tool whose entire job is remembering passwords forgot the password — and the standoff that follows is two parties who no longer trust each other, staring in silence. It lands on a cold read, the twist is the personified staring contest, and there is nothing left to trim.

## What this repo does

This is an entry for the make.fun bounty
[One-Line Laugh-Off](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the copy differs
in size or bytes, or if the text is not 1–200 characters. Nothing else:
no network, no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
