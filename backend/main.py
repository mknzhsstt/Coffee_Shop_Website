from fastapi import FastAPI
from app.menu_categories.categories_router import router as categories_router
from app.menu_items.items_router import router as items_router
from app.locations.locations_router import router as locations_router
from app.opening_hours.hours_router import router as hours_router

app = FastAPI(title="Coffee Shop API", version="1.0.0")

# Include routers
app.include_router(categories_router, prefix="/api/categories", tags=["Categories"])
app.include_router(items_router, prefix="/api/items", tags=["Menu Items"])
app.include_router(locations_router, prefix="/api/locations", tags=["Locations"])
app.include_router(hours_router, prefix="/api/hours", tags=["Opening Hours"])


@app.get("/")
async def root():
    return {"message": "Welcome to Coffee Shop API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
