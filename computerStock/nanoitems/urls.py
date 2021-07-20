from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home),
#     path('products/', views.products),
#     path('promotions/', views.promotions),
#     path('contactus/', views.contactus),
# ]
urlpatterns = [
    path('', views.products,name='home'),
    path('products/', views.products,name='products'),
    path('promotions/', views.promotions,name='promotions'),
    path('addpromotion/', views.addpromotion, name='addpromotion'),
    path('contactus/', views.contactus,name='contactus'),
    path('addproduct/', views.addproduct,name='addproduct'),
    path('Edit/<int:id>',views.editproduct,name='edit'),
    path('Update/<int:id>',views.productUpdate,name='productUpdate'),
    path('Delete/<int:id>',views.productdelete,name='productdelete'),
]