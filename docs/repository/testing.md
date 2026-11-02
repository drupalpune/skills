# Testing skills

Run `python3 scripts/test_skills.py` to validate file layout, fixture references, archive integrity and packaging. The script is deterministic and requires no API key.

The `evals/` files express human-reviewed expectations for model behaviour; the offline runner **does not actually execute the skill through an LLM**. For a release, manually audit representative fixtures using the target client and record the outcome in the PR. Never claim model behaviour passed because ZIP packaging passed.

When adding an eval case, include the input fixture, event type, must-check or must-not expectations, and a human-reviewed expected result. Keep invented examples clearly marked as synthetic. Inaccessible content must be scored `?`, not `0`.
