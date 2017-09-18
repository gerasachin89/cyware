from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    # Requirement -1 (Search Api for user)
    url(r'^user_search/$',  views.user_search.as_view()),
    # Requirement 3- Store data using Api with managing unique contraints
    url(r'^add_user/$',  views.add_user.as_view()),

]
