from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.bond_list, name='bond_list'), 
    path('def', views.default_bond_list, name = 'default_bond_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.bond_detail, name='bond_detail'),
    path('post/<int:pk>/sell/', views.bond_sell, name='bond_sell'),
    path('post/buy/', views.bondother_list, name='bond_buy'),   
    path('post/buy/post/<int:pk>', views.bondother_detail, name='bond_buy_detail'),
    path('post/contract/sell', views.contract_sell, name = 'contract_sell'),
    path('post/contract/buy', views.contract_buy, name = 'contract_buy'),    
]



