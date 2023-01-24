from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^$',Index,name="Index"),
		url(r'About/$',About,name="About"),
		url(r'Category/$',Category,name="Category"),
		url(r'Blog/$',Blog,name="Blog"),
		url(r'Blog_Details/$',Blog_Details,name="Blog_Details"),
		url(r'Contact/$',Contact,name="Contact"),
	]