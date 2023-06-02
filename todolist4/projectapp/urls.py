from . import views
from django.urls import path
urlpatterns=[
    # path("",views.index,name="index"),
    path('',views.html1,name="html1"),
    # path('index1',views.index1,name="index1"),
    path("update/<int:id>/", views.updatehtml, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),

]