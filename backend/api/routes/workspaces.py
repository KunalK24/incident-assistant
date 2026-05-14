from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.workspace import WorkspaceCreate, WorkspaceRead
from services.workspaces import create_workspace, list_workspaces

router = APIRouter(prefix="/workspaces", tags=["workspaces"])

@router.post("", response_model=WorkspaceRead, status_code=status.HTTP_201_CREATED)
def create_workspace_endpoint(
    workspace_in: WorkspaceCreate,
    db: Session = Depends(get_db),
) -> WorkspaceRead:
    return create_workspace(db, workspace_in)

@router.get("", response_model=list[WorkspaceRead])
def list_workspaces_endpoint(db: Session = Depends(get_db)) -> list[WorkspaceRead]:
    return list_workspaces(db)
