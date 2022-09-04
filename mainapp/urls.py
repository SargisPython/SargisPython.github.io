from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *




urlpatterns=[
    path("", WorkExperienceListView.as_view(), name="home"),
    path("register", register, name="register"),
    path('login/', login, name='login'),
    path('logout/', user_logout, name='logout'),
    path("add_WorkExperience/",add_workExperience,name="add_WorkExperience"),
    path("change-password/",MyPasswordChangeView.as_view(),name="password-change-view"),
    path("change-password/done/",MyPasswordResetDoneView.as_view(),name="password-change-done-view"),

    path("reset_password/",
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),
    path("reset_password_sent/",
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),
    path("reset_password_complete/",
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),
]

