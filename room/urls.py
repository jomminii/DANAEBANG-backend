from .views      import (
    DetailView,
    TradeHistoryView,
    NearInfoView,
    RoomListView,
    RoomUploadView
)

from django.urls import path

urlpatterns = [
    path('/detail', DetailView.as_view()),
    path('/trade-history', TradeHistoryView.as_view()),
    path('/near' , NearInfoView.as_view()),
    path('/upload', RoomUploadView.as_view()),
    path('/list' ,RoomListView.as_view()),
]
