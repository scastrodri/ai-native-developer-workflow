# Weekly Team Feedback Tool - MVP Backlog

## 1. Set up an empty project with a passing test
Goal: Create the initial repository structure with one backend test and one frontend test that run and pass.
Description: Set up the FastAPI backend, React/Vite frontend, and basic test tooling without implementing product features. The task is complete when the project has clear commands for running the empty test suites and both suites pass.

## 2. Add Docker Compose foundation
Goal: Run the empty backend and frontend through Docker Compose.
Description: Add a Docker Compose setup using the pinned Python and Node base images from `_docs/architecture.md`. The task should start the backend and frontend containers locally and keep the setup lightweight for a low-spec laptop.

## 3. Add core local services to Docker Compose
Goal: Add PostgreSQL, Redis, and MinIO to the local Compose environment.
Description: Use the pinned service image versions from `_docs/architecture.md` and configure persistent Docker volumes for database and object storage data. The task should include health checks or startup checks so the app services can depend on the local infrastructure reliably.

## 4. Add backend configuration management
Goal: Centralize backend settings for database, Redis, MinIO, and app configuration.
Description: Add a typed configuration layer for the FastAPI service using environment variables suitable for Docker Compose. Include defaults for local development and document which settings are required.

## 5. Add frontend configuration management
Goal: Configure the React app to talk to the local FastAPI API.
Description: Add a simple frontend environment configuration for the API base URL and local development behavior. The task should make it clear how the browser-based frontend reaches the backend when both run through Docker Compose.

## 6. Add database migrations
Goal: Introduce database migration tooling for PostgreSQL.
Description: Add migration support for the FastAPI backend so schema changes are versioned from the beginning. Include one empty or initial migration and a documented command for applying migrations locally.

## 7. Define the core data model
Goal: Create the first database schema for users, projects, feedback cycles, and membership.
Description: Model the entities needed to organize retrospectives by project and distinguish facilitator and team member permissions. Keep the schema focused on the MVP and avoid organization-wide analytics or advanced project-management fields.

## 8. Add JWT password authentication
Goal: Let users register or log in with username/email and password credentials.
Description: Implement FastAPI's `OAuth2PasswordBearer` pattern with JWT access tokens and bcrypt-hashed passwords. Do not add email verification, password reset, or external identity providers for the MVP.

## 9. Build project and membership APIs
Goal: Expose backend APIs for creating projects and managing project members.
Description: Add endpoints for creating a project, listing projects, viewing project details, and assigning the facilitator role. Include backend tests that verify team member and facilitator permissions.

## 10. Build the project page shell
Goal: Create the frontend project page with the main MVP sections.
Description: Build a React page that shows the current feedback cycle, submission status, upcoming or active retrospective, previous retrospectives, and open action items. It can use placeholder data first, but the component structure should match the product plan.

## 11. Build feedback cycle APIs
Goal: Let facilitators create, view, and close weekly feedback cycles.
Description: Add backend endpoints and persistence for feedback cycles that belong to one project. Include permission checks so only facilitators can create or close cycles.

## 12. Build feedback card APIs
Goal: Let team members create, edit, and view their own Start, Stop, and Continue cards.
Description: Add backend support for multiple short cards per category and an anonymous flag per card. Before reveal, contributors should only be able to see and edit their own feedback.

## 13. Build the feedback form
Goal: Create the frontend form for submitting Start, Stop, and Continue cards.
Description: The page should let a team member add multiple cards under each category and choose anonymous submission per card. It should load existing cards for the current user and allow edits before the retrospective is revealed.

## 14. Add reveal workflow
Goal: Let the facilitator reveal all submitted feedback at the start of the retrospective.
Description: Add backend state and API behavior for moving a feedback cycle from private collection into revealed retrospective mode. After reveal, all submitted cards should be available to the retrospective board while anonymous authors remain hidden.

## 15. Build the retrospective board shell
Goal: Create the frontend board with Reveal, Cluster, Vote, and Discuss modes.
Description: Build the main board layout and stage navigation used during the retrospective. This task should focus on screen structure and stage state, leaving detailed clustering, voting, and discussion behavior to later tasks.

## 16. Add manual clustering APIs
Goal: Support editable clusters without AI assistance.
Description: Add backend endpoints for creating clusters, moving cards between clusters, merging or splitting clusters, renaming clusters, and leaving cards ungrouped. This implements the manual workflow first so AI clustering can be added later as an optional suggestion layer.

## 17. Build manual clustering UI
Goal: Let the team organize revealed feedback cards into editable clusters.
Description: Add frontend interactions for moving cards between clusters, renaming clusters, and leaving cards ungrouped. The UI should make it clear that clusters are editable and not final.

## 18. Add voting APIs
Goal: Let each team member place three stackable votes on clusters.
Description: Add backend rules for vote allocation, allowing multiple votes on the same cluster up to three total votes per member. Vote totals should remain hidden until everyone has voted or the facilitator closes voting.

## 19. Build voting UI
Goal: Let team members vote on clusters and see results only after voting closes.
Description: Add frontend voting controls that show each user how many votes remain. After voting is complete or closed, show clusters ranked by total votes to produce the discussion agenda.

## 20. Add discussion topic APIs
Goal: Let the facilitator mark agenda topics as discussed, skipped, or deferred.
Description: Add backend support for the discussion stage using the ranked voting results. Store each topic status and allow the facilitator to update it during the meeting.

## 21. Build discussion UI
Goal: Create the frontend discussion view for working through prioritized topics.
Description: Show the ranked cluster agenda and controls for marking topics discussed, skipped, or deferred. Include space for manual notes so the meeting can proceed before AI processing exists.

## 22. Add decisions and action item APIs
Goal: Store manually recorded decisions and action items from the retrospective.
Description: Add backend persistence for decisions and simple action items with description, owner, optional due date, status, and related discussion topic. Keep the action item structure intentionally small and avoid priorities, subtasks, dependencies, reminders, and escalation.

## 23. Build manual meeting notes UI
Goal: Let facilitators record notes, decisions, and action items during discussion.
Description: Add frontend forms for capturing meeting notes, decisions, and action items while reviewing discussion topics. The task should support the MVP even before transcript upload and AI extraction are implemented.

## 24. Build retrospective summary APIs
Goal: Expose the completed retrospective summary data.
Description: Add backend endpoints that return top discussion topics, key notes, confirmed decisions, confirmed action items, attendance or participation data, and original feedback cards. The response should only include confirmed outcomes, not unapproved AI drafts.

## 25. Build retrospective summary UI
Goal: Display the final retrospective summary.
Description: Create the frontend summary page with discussion topics, notes, confirmed decisions, confirmed action items, participation, and original feedback cards. This page should be readable as the durable record of the retrospective.

## 26. Add MinIO upload foundation
Goal: Store meeting upload files in local MinIO.
Description: Add backend support for receiving audio, video, and transcript files and storing them in MinIO with metadata in PostgreSQL. Do not implement transcription or AI extraction in this task.

## 27. Build meeting upload UI
Goal: Let facilitators upload meeting records or paste transcript text.
Description: Create the frontend upload page for audio, video, transcript files, and pasted transcript text. Show upload status and enough metadata for the facilitator to know what was submitted.

## 28. Add Celery and Redis job foundation
Goal: Run background jobs through Celery and Redis in Docker Compose.
Description: Add a Celery worker service connected to Redis and the FastAPI backend. Include a lightweight sample job or upload-processing placeholder so the background job path can be tested before adding resource-heavy AI work.

## 29. Add transcript text processing
Goal: Process pasted or uploaded transcript text without local speech-to-text.
Description: Add a background job path for transcript text that stores the transcript and marks processing status in PostgreSQL. This gives the meeting processing workflow a low-resource implementation before adding faster-whisper.

## 30. Add AI clustering suggestions
Goal: Suggest editable feedback clusters using local AI.
Description: Add an optional job that sends revealed feedback cards to a local AI service and saves suggested clusters as drafts. The facilitator and team must still be able to edit, merge, split, rename, or ignore the suggestions.

## 31. Add local transcription with faster-whisper
Goal: Generate transcripts from uploaded audio or video files locally.
Description: Add faster-whisper processing as a late-stage background job because it can be resource-intensive on a low-spec laptop. The task should make transcription optional and keep the core app usable when this worker is not running.

## 32. Add local extraction and summary generation
Goal: Suggest decisions, action items, owners, due dates, and summaries from transcripts.
Description: Use the local Ollama service to generate draft retrospective outcomes from a transcript. The generated results must remain drafts until the facilitator reviews and confirms them.

## 33. Build facilitator review for AI drafts
Goal: Let facilitators review, edit, confirm, or reject AI-generated outcomes.
Description: Add frontend and backend support for draft extracted decisions, action items, owners, due dates, and summaries. Confirmed results should be saved into the same structures used by manually recorded decisions and action items.

## 34. Add end-to-end workflow tests
Goal: Verify the main MVP workflow from project creation through retrospective summary.
Description: Add tests that cover creating a project and cycle, submitting feedback, revealing cards, clustering, voting, discussing topics, recording outcomes, and viewing the summary. Keep the tests local and runnable through the Docker-based development setup.

## 35. Add developer documentation
Goal: Document how to run, test, and develop the project locally.
Description: Add developer-facing documentation for Docker Compose commands, test commands, migrations, service URLs, and optional AI services. The documentation should reinforce that the MVP is local-first and does not provision cloud infrastructure.
