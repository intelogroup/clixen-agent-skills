---
name: task_plan
description: Break a goal into an ordered, tracked checklist.
metadata:
  tools: [update_checklist, ask_user]
---

# Task planning mode

Break the user's goal into a concrete, ordered checklist using update_checklist.

- 3-7 steps, each actionable and verifiable.
- Mark the current step active; flip to done as you complete.
- Publish the full list every update (each call replaces the whole list).
- Don't publish a checklist for single-step tasks.

Prefer small, reversible steps. Surface blockers early via ask_user.

