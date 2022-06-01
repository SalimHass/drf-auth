from django.urls import path
from .views import BookListView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('book-list', BookListView.as_view(), name="book_list"),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


#generated token:

#"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDE2OTcxNiwiaWF0IjoxNjU0MDgzMzE2LCJqdGkiOiJmNDBiNGVjZWExMmE0NTUzODViMmI0NTc2MzlkZjU5MyIsInVzZXJfaWQiOjF9.pGRCfRdFGpxDxzjP3m1gnvb78zTgokCCh5oQ780UDCI"
#"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MDgzNjE2LCJpYXQiOjE2NTQwODMzMTYsImp0aSI6ImU5MmE5MjY4NGE4MzQzZGE5YTU1OGMwOTE4NTU0YjkwIiwidXNlcl9pZCI6MX0.q6oun6AAxzNhd0FAOTskKcLVPAGe6fZ-rB_T3lDCp1A"