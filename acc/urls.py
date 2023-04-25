from django.urls import path
from acc import views
from django.conf.urls import url
urlpatterns = [
    #path('',views.home,name='home'),
    path('data/',views.data,name='data'),
    path('',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
]