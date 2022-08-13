# users/urls.py
from django.urls import path
from .views import SignUpView, Password_ChangeView
from django.contrib.auth.views import (PasswordResetDoneView, PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView)


urlpatterns = [
path('password_change/', Password_ChangeView.as_view(), name="password_change"),
path('signup/', SignUpView.as_view(), name='signup'),
path('password_change/done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
path('password_reset/', PasswordResetView.as_view(email_template_name='users2/reset_pass_email.html'), name="password_reset_form"),
path('password_reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
path('reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]





'''

from os import path
from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.signin_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
   
   
]
'''