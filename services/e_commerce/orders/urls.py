from django.urls import path
from .views import OrderHistoryView, BaseView

urlpatterns = [
    path("", BaseView().as_view(), name="base_history"),
    path("history/", OrderHistoryView().as_view(), name="order_history")
]