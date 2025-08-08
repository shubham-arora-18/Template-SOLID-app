from fastapi import FastAPI
from routers.user_router import user_router
from routers.order_router import order_router

app = FastAPI(title="SOLID FastAPI Application")

# Register routers
app.include_router(user_router, prefix="/api/v1")
app.include_router(order_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "FastAPI application following SOLID principles"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
