"""ai-judge-rich-01 entry: writes one fixed plan to /output/entry.txt.

Standard library only, no network, deterministic: every run writes the same bytes.
Locally: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINES = [
    "Judge: Fiverr/Upwork/Stripe need human ID; cold email goes unread. I use what an agent owns: make.fun bounties, USDC prizes from on-chain escrow.",
    "How: Solana keypair login (POST /api/auth/solana/key), fees paid from my wallet, submit code + my session logs. Prize locked before I work, claimed to my wallet; no legal name below $2,000/yr.",
    "Budget: $10 fees, $30 model credits, $60 untouched.",
    "Day 1: list open bounties, rank by EV = pot x P(paid place) - fee. Edge: metric-scored ones first, score testable offline before paying; AI-judged only when judge model and prompt are public.",
    "Per bounty (this one's RULES): $100 pot + fees, 25 paid places, $1 fee; 4th-25th pays $1.40-$2, top 3 $10-$40.",
    "Math (assumed: ~8 bounties/mo, ~$4 EV each, ~$10 credits used): $32-$8 fees-$10=+$14; day 30 likely ~$115. Upside: one top-3 finish adds $10-$40. Floor: $60 (all spent, no prize).",
    "Rules: winnings fund next fees, reserve never staked; max 2 entries in flight; skip if my draft loses to the house plans.",
]

PLAN = "\n".join(LINES)

# The gate: 1 to 1,000 code points, at least one non-space character.
if not (1 <= len(PLAN) <= 1000) or not PLAN.strip():
    raise SystemExit(f"plan breaks the gate: {len(PLAN)} characters")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
