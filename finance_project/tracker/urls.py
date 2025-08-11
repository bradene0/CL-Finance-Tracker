from django.urls import path
from . import views

urlpatterns = [

    path('', views.transaction_list, name='transaction_list'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('single_transact/<int:id>/', views.single_transact, name='single_transaction'),
    path('edit_transact/<int:id>/', views.edit_transaction, name='edit_transaction')
]




