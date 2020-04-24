from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, utils, financial_statements, companies

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(companies.router, prefix="/companies", tags=["companies"])
api_router.include_router(financial_statements.router, prefix="/financialstatements", tags=["financial_statements"])