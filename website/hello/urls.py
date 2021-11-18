from django.urls import path
from . import views

urlpatterns= [
	path('',views.hello, name='hello'),
	path('get/<int:id>/',views.get, name='get'),
	path('update/<int:pk>',views.update.as_view(), name='update'),
	path('create/',views.create.as_view(), name='create'),
]