"""comments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from comments.api import CreateCommentAPI, ListCommentAPI, NumberOfCommentsAPI

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/1.0/comment/(?P<url>[0-9]+)$', ListCommentAPI.as_view(), name="list_comments"),
    url(r'^api/1.0/comment/number/(?P<post_id>[0-9]+)$', NumberOfCommentsAPI.as_view(), name="number_of_comments"),
    url(r'^api/1.0/comment/', CreateCommentAPI.as_view(), name="create_comment")
]
