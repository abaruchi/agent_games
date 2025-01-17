# routes/auth/auth_router.py
import logging

from fastapi import APIRouter, Depends
from models_api import ResponseModel
from routes.auth.auth_db import (
    InvalidCredentialsError,
    get_admin_token,
    get_db,
    get_team_token,
)
from routes.auth.auth_models import AdminLogin, TeamLogin
from sqlmodel import Session

logger = logging.getLogger(__name__)

# Create the router instance
auth_router = APIRouter()


@auth_router.post("/admin-login", response_model=ResponseModel)
def admin_login(login: AdminLogin, session: Session = Depends(get_db)):
    """
    Endpoint for administrator login
    """
    logger.info(f'Admin login attempt for username: "{login.username}"')
    try:
        token = get_admin_token(session, login.username, login.password)
        return ResponseModel(status="success", message="Login successful", data=token)
    except InvalidCredentialsError as e:
        return ResponseModel(status="failed", message=str(e))
    except Exception as e:
        logger.error(f"Unexpected error during admin login: {str(e)}")
        return ResponseModel(status="failed", message="An unexpected error occurred")


@auth_router.post("/team-login", response_model=ResponseModel)
def team_login(credentials: TeamLogin, session: Session = Depends(get_db)):
    """
    Endpoint for team login
    """
    try:
        team_token = get_team_token(session, credentials.name, credentials.password)
        logger.info(f"Generated token for team {credentials.name}: {team_token}")
        print(f"Generated token for team {credentials.name}: {team_token}")
        return ResponseModel(
            status="success", message="Login successful", data=team_token
        )
    except InvalidCredentialsError as e:
        return ResponseModel(status="failed", message=str(e))
    except Exception as e:
        logger.error(f"Unexpected error during team login: {str(e)}")
        return ResponseModel(status="failed", message="An unexpected error occurred")
