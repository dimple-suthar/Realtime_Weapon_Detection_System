from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('alert/<str:pk>', views.alert, name='alert'),
    path('', views.home, name='home'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="detection/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetView.as_view(template_name="detection/password_reset_sent.html"),
         name="password_reset_done"),
     path('reset/<uidp64>/<token>/',
         auth_views.PasswordChangeDoneView.as_view(template_name="detection/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetView.as_view(template_name="detection/password_reset_done.html"),
         name="password_reset_complete"),

]