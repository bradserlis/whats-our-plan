from django.urls import path
from django.conf.urls import url



from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('groups/', views.groups_list, name="groups_list"),
    path('groups/form/', views.groups_form, name="groups_form"),
    path('groups/create/', views.groups_create, name="groups_create"),
    path('groups/<int:pk>/', views.groups_detail),
    path('groups/<int:pk>/activities/create', views.activity_create),
    path('groups/<int:pk>/activities/set', views.get_random_activity),
    path('groups/<int:pk>/join/', views.groups_join),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]