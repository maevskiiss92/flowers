from django.urls import path, include
from Cart.views import CartView
from .views import CatalogView, FlowerDetailView

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    path('cart/', CartView.as_view(), name='cart'),
    path('<slug:slug>', FlowerDetailView.as_view(), name='detail')
]
