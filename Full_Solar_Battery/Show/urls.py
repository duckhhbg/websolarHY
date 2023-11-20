from django.urls import path
from .views import *

urlpatterns = [
    path('', Login.as_view(), name='Login'),
    path('Not_Login/', Not_Login, name='Not_Login'),
    path('index_HTML/', index_HTML, name='index_HTML'),
    path('solars_HTML/', solars_HTML, name='solars_HTML'),
    path('configuration_HTML/', configuration_HTML, name='configuration_HTML'),
    path('changepass_HTML/', changepass_HTML, name='changepass_HTML'),
    path('manager_HTML/', manager_HTML, name='manager_HTML'),
    path('manager_Delete/<int:id>/', manager_Delete, name='manager_Delete'),
    path('manager_Update/<str:id>', manager_Update, name='manager_Update'),
    path('Logout/', Logout, name='Logout')
]
