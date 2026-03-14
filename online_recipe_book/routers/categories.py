from fastapi import FastApi, HTTPException
from typing import List
import models.category
from models import CategoryBase, CategoryCreate, CategoryResponse, Category

from Module23.tools.app import response

app = FastApi()

@app.get("/", response_model = List)
def get_categories():
    return List[Category]

@app.post("/category/", response_model=Category)
def create_category(category:CategoryCreate):
    category_id = models.create_category(category)
    return category.Category(id = category_id, **category.dict())

@app.put("/category/{category_id}", response_model=Category)
def updated_category(category_id, category:Category):
    updated = category.database.update_category(category_id, category)
    if not updated:
        raise HTTPException(status_code=404,detail="Category not found.")
    return category.Category(id=category_id,**category.dict())


