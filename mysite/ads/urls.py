from django.urls import path
from . import views

app_name='ads'
urlpatterns = [
    path('', views.AdsListView.as_view(), name='all'),
    path('<int:pk>', views.AdsDetailView.as_view(), name='ads_detail'),
    path('create',
        views.AdsCreateView.as_view(), name='ads_create'),
    path('<int:pk>/update',
        views.AdsUpdateView.as_view(), name='ads_update'),
    path('<int:pk>/delete',
        views.AdsDeleteView.as_view(), name='ads_delete'),
]
