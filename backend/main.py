from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.menu_categories.categories_router import router as categories_router
from app.menu_items.items_router import router as items_router
from app.locations.locations_router import router as locations_router
from app.opening_hours.hours_router import router as hours_router

app = FastAPI(title="Coffee Shop API", version="1.0.0")

# Create tables (SQLite-friendly)
Base.metadata.create_all(bind=engine)

# CORS (so Vite/React can call the API from localhost:5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# If your routers already define prefixes like "/categories", "/items", etc.,
# only add a common base here:
app.include_router(categories_router, prefix="/api", tags=["Menu Categories"])
app.include_router(items_router,      prefix="/api", tags=["Menu Items"])
app.include_router(locations_router,  prefix="/api", tags=["Locations"])
app.include_router(hours_router,      prefix="/api", tags=["Opening Hours"])

@app.get("/")
async def root():
    return {"message": "Welcome to Coffee Shop API"}

@app.get("/health")
def health():
    return {"status": "ok"}
