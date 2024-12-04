from django.urls import path
from api.tokens.views import (
    DecoratedTokenVerifyView,
    DecoratedTokenBlacklistView,
    DecoratedTokenRefreshView,
    DecoratedTokenObtainPairView,
)


urlpatterns = [
    path('token-refresh/', DecoratedTokenRefreshView.as_view(), name='token_refresh'),
    path('token-obtain/', DecoratedTokenObtainPairView.as_view(), name='token_obtain'),
    path('token-verify/', DecoratedTokenVerifyView.as_view(), name='token_verify'),
    path('token-black-list/', DecoratedTokenBlacklistView.as_view(), name='token_black_list'),
]
