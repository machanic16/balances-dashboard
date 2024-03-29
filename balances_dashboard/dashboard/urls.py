from django.urls import path, include
from . import views

app_name = 'dashboard'
urlpatterns = [
    
    path("", views.IndexView.as_view(), name="index"),
    path("store/<int:pk>/", views.StoreView.as_view(), name="store"),
    path("stores/",views.store_list)

]
