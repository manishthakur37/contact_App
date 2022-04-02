from django.urls import path
from .views import *
urlpatterns=[
	path('',IndexPage,name='home_view'),
	path('add/',AddPage,name='add_view'),
	path('profile/<str:pk>',ContactProfile,name='profile_view'),
	path('edit/<str:pk>',EditPage,name='edit_view'),
	path('delete/<str:pk>',DeletePage,name='delete_view'),
]
