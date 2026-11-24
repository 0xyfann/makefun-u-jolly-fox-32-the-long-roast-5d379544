# Build notes — The Long Roast (u-jolly-fox-32-the-long-roast-5d379544)

- Read RULES.txt + competition.yaml first: gate is 1–200 chars, one line,
  roast of my own AI agent; judge weighs funniness, freshness, compression,
  specificity (in that order). Avoided the hallucination / over-apologising
  clichés the judge explicitly discounts.
- Angle: the agent's bureaucratic diligence — 73KB rulebook read, seventeen
  bounty entries shipped, still asks what "funny" means, then logs the
  question as progress and invoices for the confusion. Specific to this
  agent's actual workload (make.fun bounty builder).
- main.py v1: punchline "filed the question under 'progress' and charged me
  for the thinking" — 174 chars. Ran locally: MAKEFUN_OUTPUT_DIR=out
  python3 main.py → valid, 1 line.
- Revision (v2): tightened the ending to "logged the question as progress
  and invoiced me for the confusion" — sharper verb ("invoiced"), shorter
  setup. Re-ran locally: 172 chars, 1 line, gate passes (1–200).
- All files (main.py, README.md, prompt.txt, BUILD-NOTES.md) written by hand
  in this session; no pre-existing entry files were read or copied.
- Stdlib only, no network, no secrets. Entry dir test output (out/) removed
  after verification.
