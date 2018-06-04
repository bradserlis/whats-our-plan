from django.urls import path
from django.conf.urls import url

from wop.planner import views as core_views


from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('user/<username>/', views.profile, name='profile'),
    path('signup/', core_views.signup, name='signup'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]