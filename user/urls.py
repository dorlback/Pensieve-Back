from django.urls import path
from user.views import UserListCreateView,UserRetrieveUpdateDestroyView, UserRetrieveView

urlpatterns = [
    path("users", UserListCreateView.as_view(), name="user-list-create"),
    path("users/<str:email>", UserRetrieveUpdateDestroyView.as_view(), name="user-detail-update-destroy"),
    # path("get-user/<str:email>", UserRetrieveView.as_view(), name='check-user-exists'),
]

