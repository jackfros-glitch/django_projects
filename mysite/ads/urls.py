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
    path('ads_picture/<int:pk>',
        views.stream_file, name='ads_picture'),
    path('ad/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(), name='comment_delete'),
    path('ad/<int:pk>/favorite',
        views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad/<int:pk>/unfavorite',
        views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),


]
