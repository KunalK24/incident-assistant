from sqlalchemy import select
from sqlalchemy.orm import Session
from models.workspace import Workspace
from schemas.workspace import WorkspaceCreate

def create_workspace(db: Session, workspace_in: WorkspaceCreate) -> Workspace:
    workspace = Workspace(name=workspace_in.name)
    db.add(workspace)
    db.commit()
    db.refresh(workspace)
    return workspace

def list_workspaces(db: Session) -> list[Workspace]:
    statement = select(Workspace).order_by(Workspace.created_at.desc())
    return list(db.scalars(statement).all())
