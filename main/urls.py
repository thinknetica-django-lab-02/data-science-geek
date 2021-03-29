from django.urls import path
from . import views

urlpatterns = [
    path('', views.GoodsListView.as_view(), name='goods'),
    path('<slug:slug>/', views.GoodsDetailView.as_view(), name='goods-detail'),
    path('category/<slug:slug>/', views.GoodsListByCategoryView.as_view(),
         name='goods-by-category'),
]
