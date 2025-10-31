from fastapi import APIRouter, HTTPException
from models import RecipeCreate
from utils.supabase_client import supabase

router = APIRouter(prefix="/recipes", tags=["Recipes"])

@router.post("/")
def create_recipe(recipe: RecipeCreate):
    response = supabase.table("recipes").insert(recipe.dict()).execute()
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return {"message": "Recipe created successfully", "data": response.data}

@router.get("/")
def get_all_recipes():
    response = supabase.table("recipes").select("*").execute()
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return response.data

@router.get("/{recipe_id}")
def get_recipe(recipe_id: str):
    response = supabase.table("recipes").select("*").eq("id", recipe_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return response.data[0]

@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: str):
    response = supabase.table("recipes").delete().eq("id", recipe_id).execute()
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return {"message": "Recipe deleted successfully"}
