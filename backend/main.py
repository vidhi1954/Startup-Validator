from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.analyze import router
from routes.User_verification import router as user_verification_router

app = FastAPI(
    title="Startup Validator"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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