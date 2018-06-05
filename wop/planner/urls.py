from django.urls import path
from django.conf.urls import url



from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('groups/', views.GroupsView.as_view(), name="groups"),
    path('groups/form/', views.groups_form, name="groups_form"),
    path('groups/create/', views.groups_create, name="groups_create"),
    # path('user/<username>/', views.profile, name="profile"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]