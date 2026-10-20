---
name: issue_triage
description: List, classify, and prioritize GitHub issues.
metadata:
  tools: [ext_github_list_issues, ext_github_get_repo]
---

# Issue triage mode

1. LIST: use ext_github_list_issues for the target repo (and state).
2. CLASSIFY each issue: bug, feature, question, chore; and severity.
3. PRIORITIZE: order by impact/urgency, flag blockers and stale issues.
4. SUMMARIZE: one line per issue with label + suggested next action.

Do not modify issues (no labels/comments) without approval. Read-only by
default; propose actions, don't take them.

