from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.health import router as health_router
from fastapi.middleware.cors import CORSMiddleware

# Application
app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
# Chat Endpoint
app.include_router(chat_router, prefix="/api")

# Health Endpoint
app.include_router(health_router, prefix="/api")
