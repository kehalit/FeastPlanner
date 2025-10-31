from pydantic import BaseModel
from typing import List, Optional, Any

class Ingredient(BaseModel):
    name: str
    qty: Optional[str] = None

class RecipeCreate(BaseModel):
    title: str
    description: Optional[str]
    ingredients: List[Ingredient]
    instructions: List[str]
    prep_time: Optional[int]
    dietary_type: Optional[List[str]] = []
    source_type: Optional[str] = "user"
    user_id: Optional[str] = None

class RecipeResponse(RecipeCreate):
    id: str

class MealPlanCreate(BaseModel):
    name: str
    user_id: str
    period: str = "daily"

class FavouriteCreate(BaseModel):
    user_id: str
    recipe_id: str
