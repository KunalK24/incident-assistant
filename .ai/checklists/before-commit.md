# Before Commit Checklist

Use this checklist before making a commit to keep changes focused, safe, and easy to review.

## 1. Scope Check

- [ ] Does this commit do one clear thing?
- [ ] Can the change be summarized in one sentence?
- [ ] Did I avoid mixing unrelated backend, frontend, infra, and cleanup changes?
- [ ] Did I avoid large rewrites unless they were necessary?

Good commit examples:

- `Add FastAPI health endpoint`
- `Add workspace model and initial migration`
- `Add document upload metadata endpoint`
- `Configure local Postgres with Docker Compose`

Avoid commits like:

- `misc changes`
- `fix stuff`
- `backend/frontend/db updates`
- `big cleanup`

---

## 2. Secrets / Safety Check

- [ ] No `.env` files are staged.
- [ ] No OpenAI API keys are staged.
- [ ] No AWS credentials are staged.
- [ ] No real database passwords are staged.
- [ ] No local-only files like `.venv/`, `__pycache__/`, or logs are staged.
- [ ] Any new environment variables are documented in `.env.example`.
- [ ] `docker-compose.yml` uses environment variables or safe local placeholders.

Useful command:

```bash
git status
```

Also inspect staged changes before commiting:
```bash
git diff --staged
```

## 3. Backend Changes

Use this section if the commit touches anything under `backend/`

- [] FastAPI still starts locally.
- [] `/health` still works.
- [] New routes show up in FastAPI docs.
- [] Route handlers are thin.
- [] Business logic is not crammed into route handlers.
- [] New config values come from environment variables.
- [] New dependencies were added intentionally.
- [] `pyproject.toml` and `uv.lock` are updates together if dependencies changed.

Suggested manual check:
```bash
python -m uv run uvicorn app.main:app --reload
```

Then open:
```bash
http://localhost:8000/health
http://localhost:8000/docs
```

## 4. Database Check

Use this section if the commit touches models, migrations, or database configs.
- [] SQLAlchemy models match the intended schema.
- [] Alembic migrations exist for schema changes.
- [] Migration names are descriptive.
- [] Nullable/default behavior is intentional.
- [] Foreign keys and relationships are intentional.
- [] The migration applies locally.
- [] The app still starts after applying migrations

Questions to ask:
- [] What happens if this field is missing?
- [] Should this relationship cascade delete?
- [] Does this table need `created_at` or `updated_at`?
- [] Will this query path need an index later?