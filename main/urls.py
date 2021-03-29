from django.urls import path
from . import views

urlpatterns = [
    path('', views.GoodsListView.as_view(), name='goods'),
    path('<int:pk>/', views.GoodsDetailView.as_view(), name='goods-detail'),
    path('category/<str:category_name>/', views.GoodsListByCategoryView.as_view(),
         name='goods-by-category'),
]
