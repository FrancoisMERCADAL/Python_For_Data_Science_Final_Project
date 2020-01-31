from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.accueil),
    path('decision_tree', views.decision_tree),
    path('random_forest', views.random_forest),
    path('xgboost', views.xgboost),
]