from django.urls import path
from django.conf import settings
from users.views import  profilePage ,userRegister, userLogin, ChangePasswordView, userLogout
from base.views import homePage
from django.conf.urls.static import static


urlpatterns = [
    path('', homePage, name='home_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
