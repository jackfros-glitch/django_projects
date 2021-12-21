from django.shortcuts import render
from .owner import OwnerCreateView, OwnerListView, OwnerDetailView, OwnerUpdateView, OwnerDeleteView
from .models import Ads
from django.urls import reverse_lazy

# Create your views here.

class AdsCreateView(OwnerCreateView):
    model = Ads
    fields = ["title", "text", "price"]
    success_url = reverse_lazy("ads:all")

class AdsListView(OwnerListView):
    model = Ads

class AdsDetailView(OwnerDetailView):
    model = Ads

class AdsUpdateView(OwnerUpdateView):
    model = Ads
    fields = ["title", "text", "price"]
    success_url = reverse_lazy("ads:all")

class AdsDeleteView(OwnerDeleteView):
    model = Ads
    success_url = reverse_lazy("ads:all")