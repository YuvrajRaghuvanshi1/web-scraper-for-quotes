
from django.urls import path,include
from . import views
urlpatterns = [
    path('scrape/', views.scrape, name="scrape"),
    path('',views.home_list,name='home'),
    path('search/',views.search,name='search'),
]
