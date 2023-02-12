from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('about/', views.AboutView.as_view(), name='about'),

    re_path('post/(?P<pk>\d+)', views.PostDetailView.as_view(), name='post'),
    path('post/new', views.PostCreateView.as_view(), name="post_new"),
    re_path('post/(?P<pk>\d+)/edit', views.PostCreateView.as_view(), name="post_edit"),
    re_path('post/(?P<pk>\d+)/delete', views.PostDeleteView.as_view(), name="post_delete"),
    re_path('post/(?P<pk>\d+)/publish', views.post_publish, name="post_publish"),
    path('drafts/', views.PostDraftList.as_view(), name="drafts"),

    re_path('post/(?P<pk>\d+)/add_comment', views.add_comment_to_post, name='add_comment_to_post'),
    re_path('comment/(?P<pk>\d+)/approve', views.comment_approve, name='comment_approve'),
    re_path('comment/(?P<pk>\d+)/remove', views.comment_remove, name='comment_remove'),
    
]
