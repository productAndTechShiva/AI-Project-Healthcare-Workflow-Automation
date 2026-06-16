"""
Main entry point of application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.test_ai import router as test_ai_router
from app.api.test_analysis import router as test_analysis_router
from app.api.test_workflow import router as test_workflow_router
from app.api.workflow import router as workflow_router

app = FastAPI(
    title="AI Healthcare Workflow Automation Assistant",
    version="1.0.0"
)

# Allow React frontend to access API

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

app.include_router(test_ai_router)
app.include_router(test_analysis_router)
app.include_router(test_workflow_router)
app.include_router(workflow_router)


@app.get("/")
def root():
    return {
        "message": "AI Healthcare Workflow Automation Assistant API"
    }