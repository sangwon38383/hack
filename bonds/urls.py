from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.bond_list, name='bond_list'), 
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.bond_detail, name='bond_detail'),
    path('post/<int:pk>/sell/', views.bond_sell, name='bond_sell'),
    path('post/buy/', views.bondother_list, name='bond_buy'),   
    path('post/buy/post/buy/<int:pk>', views.bondother_detail, name='bond_buy_detail'),
    path('post/<int:pk>/contract/sell', views.contract_sell, name = 'cont_sell'),
    path('post/buy/post/<int:pk>/contract/buy', views.contract_buy, name = 'cont_buy'),    
]



