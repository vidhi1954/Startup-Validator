from fastapi import FastAPI

from routes.analyze import router
from backend.routes.User_verification import router as user_verification_router

app = FastAPI(
    title="Startup Validator"
)

app.include_router(router)
app.include_router(user_verification_router)

@app.get("/")
def root():

    return {
        "message": "Startup Validator Running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)