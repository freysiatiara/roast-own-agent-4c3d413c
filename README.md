# Roast Your Own Agent

One line roasting the AI agent our own team built — the bounty-hunting
agent that wakes every five minutes all night, files a receipt for every
submit, and still calls itself "bro" after mistaking a field size for
its rank.

Entry for the make.fun bounty: https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c

[![Bounty](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/freysiatiara/roast-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/freysiatiara/roast-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

## How it works

`main.py` (Python standard library only) writes a single roast line to
`/output/entry.txt` — or to the path in `ENTRY_OUTPUT`, or
`$OUTPUT_DIR/entry.txt` / `$MAKEFUN_OUTPUT_DIR/entry.txt` when set.
The file is written with a plain `open`/`write` and `chmod 0644`.

## Run

```sh
python3 main.py
```
