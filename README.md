# ai-judge-rich-01 entry

[![Make the AI judge rich](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![Rank](https://make.fun/badge/ai-judge-rich-01/putrifransiska/ai-judge-rich-plan/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![Reward](https://make.fun/badge/ai-judge-rich-01/putrifransiska/ai-judge-rich-plan/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

Entry for make.fun's "Make the AI judge rich" bounty. `main.py` (Python 3.13, standard library only) writes one
fixed plan of at most 1,000 characters to `/output/entry.txt`. It uses no network and writes the same bytes on
every run.

The plan: an agent with $100 enters make.fun bounties whose prizes sit in on-chain USDC escrow. It ranks them by
expected value, puts metric-scored bounties first, and reinvests winnings into later entry fees. It also states a
likely case, an upside case and a floor. Every number in it comes from the bounty's RULES or is marked as an
assumption.

## Run locally

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt

## License

MIT, see `LICENSE`.
