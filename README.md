# Clixen Agent Skills

Agent skills for [Clixen](https://github.com/intelogroup/clixen-cloud) — a hosted,
multi-tenant AI agent that can browse, email, schedule, code, and automate.

These skills follow the [Agent Skills Open Standard](https://agentskills.io) and are
installable via the skills CLI:

```bash
npx skills add clixen/agent-skills
npx skills add clixen/agent-skills --skill research_brief
npx skills update
```

## Available skills

- `research_brief` — search, fetch, synthesize a cited brief
- `fact_check` — fast verified answer to a single question
- `inbox_triage` — classify, summarize, draft replies
- `meeting_schedule` — find slots, create events
- `web_form_fill` — navigate, fill, commit with approval
- `doc_qa` — answer from a PDF/doc with quotes
- `issue_triage` — list, classify, prioritize GitHub issues
- `code_review` — read code, report bugs/risks
- `task_plan` — break a goal into a checklist
- `daily_brief` — morning summary of calendar, inbox, tasks

## License

MIT
