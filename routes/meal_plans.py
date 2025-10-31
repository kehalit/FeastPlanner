from fastapi import APIRouter, HTTPException
from models import MealPlanCreate
from utils.supabase_client import supabase

router = APIRouter(prefix="/meal-plans", tags=["Meal Plans"])

@router.post("/")
def create_meal_plan(plan: MealPlanCreate):
    response = supabase.table("meal_plans").insert(plan.dict()).execute()
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return {"message": "Meal plan created", "data": response.data}

@router.get("/{user_id}")
def get_user_meal_plans(user_id: str):
    response = supabase.table("meal_plans").select("*").eq("user_id", user_id).execute()
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return response.data
