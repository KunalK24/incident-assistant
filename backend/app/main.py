from fastapi import FastAPI
from api.routes.workspaces import router as workspaces_router

app = FastAPI()

app.include_router(workspaces_router)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
