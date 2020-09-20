from . import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:category_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>',
         views.ProdCatDetail, name='ProdCatDetail'),
]
