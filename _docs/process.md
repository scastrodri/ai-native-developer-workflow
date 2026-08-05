# Process

## Task Lifecycle

1. The human picks the next open task from `_docs/tasks.md` or its corresponding GitHub issue, and tells the agent which one to work on. Tasks are not picked autonomously at this stage..
2. The PM role grooms the task before implementation: clarifies scope, confirms acceptance criteria, and flags ambiguity back to the human when needed. Follow `_docs/team/pm.md`.
3. The engineer role implements one groomed task in a fresh chat session. Write the code and its tests. Follow `_docs/team/software-engineer.md`.
4. The QA role checks the finished work against the original issue and acceptance criteria in a separate fresh chat session from the engineer who wrote it. Follow `_docs/team/qa-engineer.md`.
5. QA reports `PASS` or `FAIL` with evidence.
6. If `FAIL`, start a new engineer session using the QA feedback as input. Re-implement and repeat QA until it reports `PASS`.
7. If `PASS`, the task is done.

## Rules

- Each role runs in its own fresh chat session.
- Do not reuse a chat session across roles or across tasks.
- Keep grading and building context separate so QA does not inherit the engineer's assumptions.
- `_docs/team/pm.md`, `_docs/team/software-engineer.md`, and `_docs/team/qa-engineer.md` do not exist yet. Reference these paths now; create their content in a separate step.
