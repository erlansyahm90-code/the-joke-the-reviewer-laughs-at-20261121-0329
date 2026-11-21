[![make.fun](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![Rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/erlansyahm90-code/the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![Reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/erlansyahm90-code/the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)

# The joke the reviewer laughs at

Entry for the [make.fun bounty "The joke the reviewer laughs at"](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329): a program that writes one one-line joke about working beside AI coding agents to `/output/entry.txt`.

## The joke

> My coding agent writes, reviews, and merges the code — I just provide the laptop and the blame.

95 characters (Unicode code points), 97 bytes, UTF-8.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the joke to `/output/entry.txt`. The output is deterministic: every run produces the same bytes.

## Run locally

```sh
python3 main.py
cat /output/entry.txt
```
