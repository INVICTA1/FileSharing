from django.conf.urls import url, include
from django.contrib.auth import login, logout
from django.contrib.auth.views import logout_then_login
from . import views
from django.contrib.auth.password_validation import password_changed
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetView,PasswordResetCompleteView,PasswordResetDoneView
from django.contrib.auth import views as views_email
from django.urls import path

app_name = 'fileSharing'
urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^password_changed', views.a_change_password, name='a_change_password'),
    url(r'^account/files', views.user_files, name='user_files'),
    path(r'delete/<str:name>/', views.del_user_files, name='del_user_files'),
    url(r'^password-reset/$', views_email.PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),
    url(r'^password-reset/done/$', views_email.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]
