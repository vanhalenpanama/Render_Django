from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # 수정본
    path('logout/', views.logout_view, name='logout'),
    # 제대로 구현되지 않음
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 다른 URL 패턴들  
]


    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'), 
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'), 