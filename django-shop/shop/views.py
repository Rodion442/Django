from django.http import Http404
from django.shortcuts import render

ITEMS = [
    {"id": 1, "name": "Laptop Gamingowy", "category": "Elektronika", "price": 4500, "is_available": True},
    {"id": 2, "name": "Mysz Bezprzewodowa", "category": "Akcesoria", "price": 120, "is_available": True},
    {"id": 3, "name": "Klawiatura Mechaniczna", "category": "Akcesoria", "price": 350, "is_available": False},
    {"id": 4, "name": "Monitor 4K", "category": "Monitory", "price": 1800, "is_available": True},
    {"id": 5, "name": "Słuchawki", "category": "Akcesoria", "price": 250, "is_available": False},
]

def index(request):
    return render(request, "shop/index.html")

def item_list(request):
    return render(request, "shop/item_list.html", {"items": ITEMS})

def item_detail(request, item_id):
    item = next((i for i in ITEMS if i["id"] == item_id), None)
    if item is None:
        raise Http404("Nie znaleziono przedmiotu")
    return render(request, "shop/item_detail.html", {"item": item})