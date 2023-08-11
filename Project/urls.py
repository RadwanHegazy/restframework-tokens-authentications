
from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('names',views.NamesViewSet)

urlpatterns = [

    # default django admin panel 
    path('admin/', admin.site.urls),

    # permissions.IsAuthenticatedOrReadOnly
    path('',views.is_auth_or_readonly),

    # permissions.IsAuthenticated
    path('is-auth/',views.is_auth),

    # permissions.IsAdminUser
    path('is-admin/',views.is_admin),




    # Token Authentication
    # 1 - Get Tokens
    path('get-token/',obtain_auth_token),

    # 2 - GET data using token in Headers[token <TOKEN> ]
    path('token-auth/',views.token_authentication),
    



    # using token in CBV with viewsets
    path('names-tokens-cbv/',include(router.urls)),


    # login or logout
    path('api-auth/',include('rest_framework.urls'))
]
