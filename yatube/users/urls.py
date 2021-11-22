from django.urls import path
from . import views
from django.contrib.auth import views as r



app_name = 'users'

urlpatterns = [
    # Авторизация
    path('login/', r.LoginView.as_view(template_name='users/login.html'), name='login'), 

    # Выход
    path('logout/', r.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'), 

    # Смена пароля
    path('password_change/', r.PasswordChangeView.as_view(), name='password_change'),

    # Сообщение об успешном изменении пароля
    path('password_change/done/', r.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Восстановление пароля
    path('password_reset/', r.PasswordResetView.as_view(), name='password_reset'),
    # path("password_reset", views.password_reset_request, name="password_reset"),


    # Сообщение об отправке ссылки для восстановления пароля
    path('password_reset/done/', r.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # Вход по ссылке для восстановления пароля
    path('reset/<uidb64>/<token>/', r.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # Сообщение об успешном восстановлении пароля
    path('reset/done/', r.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('login',
    #     r.LoginView.as_view(),
    #     # LoginView.as_view(template_name='users/login.html'),
    #     name='login'
    # ),
    # path(
    #     'logout/',
    #     LogoutView.as_view(template_name='users/logged_out.html'),
    #     name='logout'
    # ),
    # path(
    #     'password_change/',
    #     PasswordChangeView.as_view(template_name='users/password_change_form.html'),
    #     # (template_name='users/password_change_form.html'),
    #     name='password_change'
    # ),
    # path(
    #     'password_change/done/',
    #     PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
    #     name='password_change_done'

    # ),
    # path('password_reset/', r.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', r.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', r.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # # path(
    # #     'password_reset/',
    # #     PasswordResetView.as_view(template_name='users/password_reset_form.html'),
    # #     name='password_reset'
    # # ),
    path('signup/', views.SignUp.as_view(), name='signup'),

]
