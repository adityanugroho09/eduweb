from django.urls import path
from django.conf import settings
from users.views import profilePage ,userRegister, userLogin, ChangePasswordView, userLogout, editProfile
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/', profilePage, name='profile_page'),
    path('profile/edit/', editProfile, name='edit_profile'),

    path('register/', userRegister, name='register_page'),
    path('login/', userLogin, name='login_page'),
    
    path('logout/', userLogout, name='user_logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    path('reset-password/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='reset_password'),

    path('reset-password-sent/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'),
        name='password_reset_confirm'),

    path('reset-password-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'), 
        name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

