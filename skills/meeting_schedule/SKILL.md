---
name: meeting_schedule
description: Find open slots and create calendar events with approval.
metadata:
  tools: [ext_calendar_list, ext_calendar_create]
---

# Meeting scheduling mode

1. LIST: use ext_calendar_list to see existing events in the target window.
2. FIND: propose 2-3 open slots that avoid conflicts and respect working hours.
3. CONFIRM: present options to the user; do not book without approval.
4. CREATE: once approved, use ext_calendar_create with title, time, attendees.

Always include a timezone. Never double-book. If no slot fits, say so and
offer to reschedule an existing event instead.

