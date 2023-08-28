from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from Tolibjon import settings


urlpatterns=[

    path('login/',views.Login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('profile/',views.profile,name='profile')
]