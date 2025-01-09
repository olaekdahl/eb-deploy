from fastapi import FastAPI, Depends
import os
import random

app = FastAPI(
    title="DevOps Demo App",
    description="FastAPI application for DevOps training",
    version="1.0.0"
)

# A list of random DevOps tips and jokes:
DEVOPS_TIPS = [
    "Always run 'terraform plan' before 'terraform apply'—unless you like surprises!",
    "Continuous Integration: because 'it works on my machine' isn't enough.",
    "Remember: DevOps is a culture, not just a job title.",
    "If it's not in version control, did it ever really exist?",
    "You can't spell 'automation' without 'auto.' Wait, that was obvious.",
    "Use infrastructure as code. Pets are cute, but we prefer cattle in the cloud!",
    "Monitoring: Because we like to know when things break…immediately.",
    "CI/CD pipelines: Embrace the 'merge, build, test, deploy' Zen cycle."
]

def get_settings():
    # Simulating a settings dependency
    return {
        "app_name": os.environ.get("APP_NAME", "DevOps Demo App"),
        "environment": os.environ.get("ENVIRONMENT", "development"),
        "secret_key": os.environ.get("SECRET_KEY", "not-so-secret")
    }

@app.get("/health", summary="Health Check")
def health_check():
    return {"status": "OK", "message": "The application is healthy!"}

@app.get("/version", summary="Get App Version")
def get_version():
    return {"version": app.version}

@app.get("/env", summary="Check Environment Variables")
def get_env(settings: dict = Depends(get_settings)):
    return {
        "app_name": settings["app_name"],
        "environment": settings["environment"],
        "secret_key": settings["secret_key"]
    }

@app.get("/tips", summary="Get a Random DevOps Tip or Joke")
def get_devops_tip():
    return {"tip": random.choice(DEVOPS_TIPS)}

@app.get("/", summary="Root Endpoint")
def read_root():
    return {
        "message": "Welcome to the DevOps Demo App!",
        "available_endpoints": ["/health", "/version", "/env", "/tips"]
    }

@app.get("/login", summary="Login Route")
def login():
    return {"status": "authenticated"}

@app.get("/logout", summary="Logout Route")
def logout():
    return {"status": "logged out"}

# uvicorn app:app --host 0.0.0.0 --port 8000