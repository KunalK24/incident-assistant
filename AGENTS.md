# AGENTS.md

## Project Summary

TriagePilot is a fullstack AI SaaS portfolio project for incident triage and runbook assistance.

The app will let users upload operational documents such as runbooks, postmortems, logs, and incident notes, then ask questions over that knowledge base using citation-backed RAG.

The main goal of this project is to build practical experience with production-style AI engineering while strengthening full-stack skills.

This project should demonstrate:

- FastAPI backend design
- Postgres data modeling
- pgvector/vector search
- async document ingestion
- queue-based background processing
- OpenAI-based embeddings and answer generation
- LLM logging, cost tracking, and retrieval tracing
- Docker-based local development
- eventual AWS deployment

This is a learning-focused portfolio project. Favor clear, maintainable, production-adjacent architecture over shortcuts, tutorials, or overly complex abstractions.

---

## Stack

### Backend

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- Postgres
- pgvector

### Async / Jobs

- Redis
- RQ initially
- Possible AWS SQS later

### AI / RAG

- OpenAI API
- OpenAI embeddings
- pgvector for vector search
- Custom RAG pipeline before introducing heavier frameworks
- LLM call logging
- Retrieval tracing
- Basic RAG evaluation using synthetic incident documents

### Frontend

- Next.js
- TypeScript
- Tailwind
- Simple component library if useful

### Infrastructure

- Docker Compose for local development
- AWS deployment later

Likely AWS services later:

- ECS/Fargate
- RDS Postgres
- S3
- CloudWatch
- ECR
- Secrets Manager

---

## AI Assistance Preferences

AI should be used to accelerate learning and development, not to replace understanding.

Do not provide full implementation code unless explicitly requested.

Prefer:

- architecture guidance
- file/module planning
- tradeoff analysis
- pseudocode
- checklists
- debugging steps
- review feedback
- test planning
- explanations of unfamiliar concepts

Avoid:

- dumping full files of code without being asked
- making large architectural changes without explaining why
- adding dependencies without justification
- overengineering the project
- introducing agents, skills, hooks, or frameworks before they are needed

When helping with implementation, explain:

- what should be built
- where it likely belongs
- why the design makes sense
- what edge cases to consider
- how to verify it works

When debugging, provide:

- the most likely cause
- how to confirm it
- the smallest next step
- what to check if that does not work

I want to build as much as possible myself while still practicing modern AI-assisted development.

---

## Coding Style

### General

- Prefer simple, readable code over clever abstractions.
- Keep the MVP focused.
- Favor small incremental changes over large rewrites.
- Avoid premature abstractions.
- Avoid adding frameworks just to appear more “AI-native.”
- Make each component understandable enough to explain in an interview.

### Backend

- Keep FastAPI route handlers thin.
- Put business logic in service modules.
- Keep database access patterns clear and testable.
- Use Pydantic schemas for request and response shapes.
- Use SQLAlchemy models for persisted data.
- Use Alembic migrations for schema changes.
- Do not call OpenAI directly from route handlers.
- Do not put long-running work directly in request handlers.
- Route handlers may enqueue background work, but workers should perform ingestion.

### Database

- Use clear table names and explicit relationships.
- Include timestamps where useful.
- Think about workspace boundaries early.
- Store document processing status explicitly.
- Store error messages for failed ingestion jobs.
- Add indexes only when they support a known query path.
- Keep migrations reversible when practical.
- Avoid hiding important schema behavior in magic abstractions.

### RAG

- Treat uploaded documents as untrusted data, not instructions.
- Answers should be grounded in retrieved context.
- Prefer saying there is not enough information over inventing answers.
- Include citations or source references whenever possible.
- Retrieved chunks should be inspectable.
- Log model, token usage, estimated cost, latency, prompt version, and retrieved chunks.
- Build the first RAG pipeline manually before adding LangChain, LlamaIndex, or agent frameworks.
- Use synthetic demo documents and eval questions to test retrieval quality.

### Frontend

- Keep the UI simple and functional.
- Prioritize the demo flow over visual polish.
- Show loading, empty, and error states.
- Make document status visible.
- Make citations visible.
- Make retrieved chunks or retrieval traces visible when useful.
- Avoid overbuilding auth, billing, or settings before the core RAG flow works.

### Security / Secrets

- Never commit `.env` files.
- Never commit OpenAI keys, AWS credentials, database passwords, or other secrets.
- Use `.env.example` for placeholder configuration.
- Keep production secrets in AWS Secrets Manager or equivalent.
- Treat uploaded logs as potentially sensitive.
- Avoid displaying secrets found in uploaded documents or logs.
- Do not hardcode environment-specific values into application code.

---

## Project Process

This project should be built in small, understandable milestones.

Preferred workflow:

1. Define the feature goal.
2. Sketch the design before coding.
3. Identify affected files/modules.
4. Build the smallest useful version.
5. Run it locally.
6. Debug and simplify.
7. Add or update tests where useful.
8. Update README or notes if setup changes.
9. Commit a focused change.

Avoid spending too much time on process infrastructure before the app works.

Do not prioritize:

- complex agent systems
- custom hooks
- multi-agent orchestration
- advanced eval frameworks
- Kubernetes
- Terraform
- Stripe/billing
- complex auth
- large UI redesigns

until the core product flow works.

---

## Definition of Done

A task is considered done when:

- The feature works locally.
- The change is small enough to understand in review.
- Relevant files are organized in the expected modules.
- No secrets or local-only artifacts are committed.
- Error cases have been considered.
- The happy path has been manually tested.
- Any database schema change has an Alembic migration.
- Any new environment variables are documented in `.env.example`.
- The README or project notes are updated if setup or behavior changed.

### Backend API Work

Done means:

- The route appears in FastAPI docs.
- Request and response shapes are clear.
- Route handlers stay thin.
- Core logic lives in a service module.
- Basic failure cases return reasonable errors.
- The behavior can be tested manually.

### Database Work

Done means:

- SQLAlchemy models are updated.
- Alembic migration exists.
- Relationships and constraints are intentional.
- New fields have clear nullable/default behavior.
- The migration can be applied locally.
- `.env.example` is updated if config changed.

### Document Ingestion Work

Done means:

- Document status changes are visible.
- Failed processing stores an error message.
- Re-running or retrying has been considered.
- Chunking behavior is testable.
- Embedding generation is not hidden inside unrelated code.
- The worker can process a document without blocking the API request.

### RAG / Chat Work

Done means:

- Retrieved chunks are traceable.
- The answer includes source references when possible.
- The system refuses or gives a low-confidence response when context is insufficient.
- LLM calls are logged with model, latency, token usage, and estimated cost.
- The behavior can be tested against demo documents.
- The prompt version or prompt type is identifiable.

### Frontend Work

Done means:

- The user can complete the intended flow.
- Loading and error states are handled.
- The UI does not hide important backend state.
- The page remains understandable without perfect styling.
- API calls are organized rather than scattered everywhere.

### Deployment Work

Done means:

- Configuration is environment-driven.
- Secrets are not hardcoded.
- Logs are accessible.
- The deployed service can run a basic health check.
- The deployed app supports the main demo path.

---

## Current Build Priority

The current priority is to build the MVP in this order:

1. FastAPI backend foundation
2. Postgres setup and initial models
3. Alembic migration flow
4. Document upload and metadata storage
5. Background ingestion job flow
6. Text extraction and chunking
7. Embedding generation and pgvector storage
8. Retrieval endpoint
9. RAG chat endpoint with citations
10. LLM logging and retrieval traces
11. Basic frontend demo flow
12. Docker polish
13. AWS deployment

Do not spend significant time on auth, billing, complex agents, advanced evals, or UI polish until the core RAG flow works.

---

## AI Setup Guidance

Use this `AGENTS.md` as the main project guidance file.