from fastapi import APIRouter, HTTPException
from models import FavouriteCreate
from utils.supabase_client import supabase

router = APIRouter(prefix="/favourites", tags=["Favourites"])

@router.post("/")
def add_favourite(fav: FavouriteCreate):
    response = supabase.table("favourites").insert(fav.dict()).execute()
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return {"message": "Added to favourites", "data": response.data}

@router.get("/{user_id}")
def get_user_favourites(user_id: str):
    response = (
        supabase.table("favourites")
        .select("recipe_id, recipes(title, description)")
        .eq("user_id", user_id)
        .execute()
    )
    if response.error:
        raise HTTPException(status_code=400, detail=response.error.message)
    return response.data
