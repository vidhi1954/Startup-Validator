from fastapi import FastAPI

from routes.analyze import router

app = FastAPI(
    title="Startup Validator"
)

app.include_router(router)

@app.get("/")
def root():

    return {
        "message": "Startup Validator Running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)