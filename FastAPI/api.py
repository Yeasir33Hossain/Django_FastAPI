# your_project/api.py
import os
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import List
from django.core.serializers import serialize
from django.http import JsonResponse
from django.db import models

# Add these lines to configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_FastAPI.settings")
import django

django.setup()

from DjangoFastAPI.models import Product, SubCategory

app = FastAPI()


class SubCategorySchema(BaseModel):
    name: str


class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    subcategory: SubCategorySchema


@app.get("/products/", response_model=List[ProductSchema])
def get_products(
        name: str = Query(None, title="Product Name", description="Filter by product name"),
        description: str = Query(None, title="Product Description", description="Filter by product description"),
        min_price: float = Query(None, title="Minimum Price", description="Filter by minimum price"),
        max_price: float = Query(None, title="Maximum Price", description="Filter by maximum price"),
        subcategory_name: str = Query(None, title="Subcategory Name", description="Filter by subcategory name"),
):
    filters = {}

    if name:
        filters['name__icontains'] = name

    if description:
        filters['description__icontains'] = description

    if min_price is not None:
        filters['price__gte'] = min_price

    if max_price is not None:
        filters['price__lte'] = max_price

    if subcategory_name:
        subcategory = SubCategory.objects.filter(name__icontains=subcategory_name).first()
        if subcategory:
            filters['subcategory'] = subcategory.id

    products = Product.objects.filter(**filters)

    return products
