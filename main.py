from fastapi import FastAPI
from routes import recipies, meal_plans, favourites
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Meal Planner API", version="1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(recipies.router)
app.include_router(meal_plans.router)
app.include_router(favourites.router)

@app.get("/")
def root():
    return {"message": "Meal Planner API is running 🚀"}

