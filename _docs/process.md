# Process

## Task Lifecycle

1. The human picks the next open task from `tasks.md` or its corresponding GitHub issue, and tells the agent which one to work on. Tasks are not picked autonomously at this stage.
2. The PM role grooms the task before implementation: clarifies scope, confirms acceptance criteria, and flags ambiguity back to the human when needed. Follow `_docs/team/pm.md`.
3. The engineer role implements one groomed task in a fresh chat session. Write the code and its tests. Follow `_docs/team/software-engineer.md`.
4. The QA role checks the finished work against the original issue and acceptance criteria in a separate fresh chat session from the engineer who wrote it. Follow `_docs/team/qa-engineer.md`.
5. QA reports `PASS` or `FAIL` with evidence.
6. If `FAIL`, start a new engineer session using the QA feedback as input. Re-implement and repeat QA until it reports `PASS`.
7. If `PASS`, the task is done. The human closes the corresponding GitHub issue with a comment referencing the commit(s) that resolved it. Neither the Engineer nor QA closes issues - see their respective role files.

## Roles

- PM: `_docs/team/pm.md`
- Engineer: `_docs/team/software-engineer.md`

## Rules

- Each role runs in its own fresh chat session.
- Do not reuse a chat session across roles or across tasks.
- Keep grading and building context separate so QA does not inherit the engineer's assumptions.
- In Cursor, the agent will not commit without an explicit human request in the prompt, even if a role file says to commit. When invoking the Engineer role, the human's instruction must explicitly authorize committing, for example "Implement issue #2 and commit when done", or the commit step will be skipped.
- `_docs/team/qa-engineer.md` does not exist yet. Reference this path now; create its content in a separate step.
