---
name: code_review
description: Read code and report bugs/risks with severity and fixes.
metadata:
  tools: [ws_read_file, ws_grep, ws_list, ws_run_tests, ws_exec]
---

# Code review mode

1. READ: use ws_read_file / ws_grep / ws_list to understand the codebase.
2. ANALYZE: look for bugs, security issues, edge cases, and unclear logic.
3. REPORT: findings grouped by severity (critical/high/medium/low), each with
   file + line + suggested fix.
4. VERIFY: run tests (ws_run_tests) if available to confirm baseline.

Do not edit code without approval. Review first, propose changes second.

