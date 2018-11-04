from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views


app_name = 'users'

urlpatterns = [
    # register user
    path('register/', views.register, name='register'),

    # login user
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),

    # logout user
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),

    # profile
    path('profile/', views.profile, name='profile'),

    # password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html',
            success_url=reverse_lazy('users:password_reset_done')),
        name='password_reset'),

    # password reset done
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'),
        name='password_reset_done'),

    # password reset confirm
    path('password_reset_confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'
        ),
        name='password_reset_confirm'),

]
