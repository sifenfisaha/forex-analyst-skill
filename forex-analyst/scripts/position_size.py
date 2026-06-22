#!/usr/bin/env python3
"""
position_size.py — Forex position sizing + risk/reward calculator.

For the forex-analyst skill. Enforces the user's risk rules:
  - risk 0.5%-1% of account per trade
  - minimum 1:3 reward-to-risk

Usage (CLI flags):
  python3 position_size.py --account 10000 --risk 1 \
      --pair EURUSD --entry 1.0850 --stop 1.0830 --tp 1.0910

  python3 position_size.py --account 10000 --risk 0.5 \
      --pair XAUUSD --entry 2350 --stop 2347 --tp 2362

  # JPY pair:
  python3 position_size.py -a 10000 -r 1 -p USDJPY -e 150.20 -s 150.00 -t 150.80

If run with no args, it prompts interactively.

NOTE: pip values are broker-dependent (especially gold & exotics).
Treat the output as a close estimate and confirm against your broker's
contract specs before sizing live. USD-denominated account assumed.
"""

import argparse
import sys


def pip_size(pair: str) -> float:
    """Pip increment for the pair. JPY pairs use 0.01; metals handled separately."""
    pair = pair.upper()
    if pair.endswith("JPY") or "JPY" in pair:
        return 0.01
    if pair.startswith("XAU") or pair.startswith("GOLD"):
        return 0.10          # 1 'pip' on gold commonly = $0.10 move
    if pair.startswith("XAG"):
        return 0.01
    return 0.0001            # standard FX


def pip_value_per_lot(pair: str, price: float) -> float:
    """
    Approx pip value in USD for 1.00 standard lot, USD account.
    - USD-quote majors (xxxUSD): $10/pip
    - USD-base pairs (USDxxx, incl. JPY): ~ (pip/price) * contract
    - XAUUSD: ~$1/pip per 100oz lot (1 pip = $0.10 move -> $0.10*100oz? broker-dependent)
    """
    pair = pair.upper()
    if pair.startswith("XAU") or pair.startswith("GOLD"):
        # 100 oz contract, 1 pip = $0.10 move => $0.10 * 100 = $10 per pip per lot.
        # (Many brokers quote gold as $1/point; CONFIRM with broker.)
        return 10.0
    if pair.startswith("XAG"):
        return 25.0  # 5000 oz silver contract approx; confirm broker
    # USD is the quote currency (e.g. EURUSD, GBPUSD): pip value fixed at $10/lot
    if pair.endswith("USD"):
        return 10.0
    # USD is the base currency (e.g. USDJPY, USDCHF, USDCAD)
    if pair.startswith("USD"):
        contract = 100_000
        return (pip_size(pair) / price) * contract
    # Cross pairs (e.g. EURJPY, GBPJPY) — approximate via quote; needs quote->USD rate.
    # Fallback: treat like $10/lot and warn.
    return 10.0


def main():
    p = argparse.ArgumentParser(description="Forex position size + RR calculator")
    p.add_argument("-a", "--account", type=float, help="Account equity in USD")
    p.add_argument("-r", "--risk", type=float, help="Risk %% per trade (0.5-1)")
    p.add_argument("-p", "--pair", type=str, help="Pair e.g. EURUSD, USDJPY, XAUUSD")
    p.add_argument("-e", "--entry", type=float, help="Entry price")
    p.add_argument("-s", "--stop", type=float, help="Stop price")
    p.add_argument("-t", "--tp", type=float, help="Target price (TP)")
    args = p.parse_args()

    def ask(prompt, cast):
        return cast(input(prompt).strip())

    account = args.account if args.account is not None else ask("Account equity (USD): ", float)
    risk = args.risk if args.risk is not None else ask("Risk % per trade (0.5-1): ", float)
    pair = (args.pair or ask("Pair (e.g. EURUSD): ", str)).upper()
    entry = args.entry if args.entry is not None else ask("Entry price: ", float)
    stop = args.stop if args.stop is not None else ask("Stop price: ", float)
    tp = args.tp if args.tp is not None else ask("Target price: ", float)

    # --- core math ---
    ps = pip_size(pair)
    risk_amount = account * (risk / 100.0)
    stop_pips = abs(entry - stop) / ps
    reward_pips = abs(tp - entry) / ps
    pv = pip_value_per_lot(pair, entry)

    if stop_pips == 0:
        print("ERROR: entry and stop are identical.")
        sys.exit(1)

    lots = risk_amount / (stop_pips * pv)
    rr = reward_pips / stop_pips
    reward_amount = risk_amount * rr
    direction = "LONG ▲" if tp > entry else "SHORT ▼"

    # --- output ---
    line = "=" * 52
    print(f"\n{line}")
    print(f"  {pair}  {direction}")
    print(line)
    print(f"  Account            : ${account:,.2f}")
    print(f"  Risk               : {risk:.2f}%  =  ${risk_amount:,.2f}")
    print(f"  Entry / Stop / TP  : {entry} / {stop} / {tp}")
    print(f"  Stop distance      : {stop_pips:.1f} pips")
    print(f"  Target distance    : {reward_pips:.1f} pips")
    print(f"  Pip value (1 lot)  : ${pv:,.2f}")
    print(line)
    print(f"  >> POSITION SIZE   : {lots:.2f} lots")
    print(f"     (mini {lots*10:.1f} / micro {lots*100:.0f})")
    print(f"  >> REWARD-TO-RISK  : 1 : {rr:.2f}")
    print(f"     Risk ${risk_amount:,.0f}  ->  Reward ${reward_amount:,.0f}")
    print(line)

    # --- rule enforcement (the skill's hard rules) ---
    flags = []
    if risk > 1.0:
        flags.append(f"⚠️  Risk {risk:.2f}% EXCEEDS the 1% max. Reduce to 0.5–1%.")
    if rr < 3.0:
        flags.append(f"❌ RR 1:{rr:.2f} is BELOW the 1:3 minimum. NO-TRADE — do not widen stop to fix this.")
    if not flags:
        print("  ✅ Passes risk rules: risk ≤1% and RR ≥1:3.")
    else:
        for f in flags:
            print("  " + f)
    print(line + "\n")

    if pair.startswith("XAU") or pair.startswith("XAG") or pair.startswith("USD") or "JPY" in pair:
        print("  ⓘ  Pip value for metals / JPY / USD-base pairs is broker-dependent.")
        print("     Confirm against your broker's contract spec before going live.\n")


if __name__ == "__main__":
    main()
