from django.urls import path
from blog import views

urlpatterns = [
    path('/', views.PostListView.as_view(), name='posts'),
    path('post/(?P<pk>\d+)', views.PostDetailView.as_view(), name='post'),
    path('post/new', views.PostCreateView.as_view(), name="post_new"),
    path('post/(?P<pk>\d+)/edit', views.PostCreateView.as_view(), name="post_edit"),
    path('post/(?P<pk>\d+)/delete', views.PostDeleteView.as_view(), name="post_delete"),
    path('drafts/', views.PostDraftList.as_view(), name="drafts"),
    path('about/', views.AboutView.as_view(), name='about')
]
