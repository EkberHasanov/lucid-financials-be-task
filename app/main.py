import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import inspect
from app.models.database import engine, Base
from app.controllers import auth_controller, post_controller

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="LuciDreams Social API",
    description="A RESTful API for social posts management",
    version="1.0.0"
)

#  CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #  actual origins has to be added in PROD
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_tables():
    inspector = inspect(engine)
    if not inspector.has_table("users") or not inspector.has_table("posts"):
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created")
    else:
        logger.info("Database tables already exist")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response


app.include_router(auth_controller.router, prefix="/api")
app.include_router(post_controller.router, prefix="/api")


@app.get("/")
async def root():
    return {
        "message": "Welcome to LuciDreams Social API",
        "documentation": "/docs",
        "version": "1.0.0"
    }


@app.on_event("startup")
async def startup_event():
    logger.info("Application starting up...")
    create_tables()
    logger.info("Application startup complete")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
