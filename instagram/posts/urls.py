from django.urls import path,include,re_path
from . import views

app_name='posts'

urlpatterns = [
    re_path(
        r'create/$',
        views.CreatePostView.as_view(),
        name='create'
    ),
    re_path(
        r'(?P<slug>[\w\-]{10})/$',
        views.DetailPostView.as_view(),
        name='view'
    ),
    re_path(
        r'(?P<slug>[\w\-]{10})/update/$',
        views.UpdatePostView.as_view(),
        name='update'
    ),
    re_path(
        r'(?P<slug>[\w\-]{10})/delete/$',
        views.DeletePostView.as_view(),
        name='delete'
    ),
    re_path(
        r'(?P<slug>[\w\-]{10})/like/$',
        views.like_post_view,
        name='like'
    ),
    re_path(
        r'(?P<slug>[\w\-]{10})/unlike/$',
        views.unlike_post_view,
        name='unlike'
    ),
]
