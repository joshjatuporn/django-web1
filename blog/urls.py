from django.urls import path
from .views import index, single_post, contact, search

urlpatterns = [
    # path('url name', function)
    path("", index, name="home"),
    path("posts/<int:id>", single_post), 
    #127.0.0.1:8000/posts/
    path("contact-us", contact, name="contact"),
    path("search", search, name="search")

]
