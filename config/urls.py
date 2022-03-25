from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from base.views import UserDetail, UserList, UserUpdate, Login, Top, Signup, Logout, PostCreate, PostDetail, PostList, \
    PostUpdate, PostDelete, FollowUnFollow, Like, CommentCreate, CommentUpdate, CommentDelete

urlpatterns = [
    path('', Top.as_view(), name="top"),
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name="login"),
    path('user/<str:pk>/update/', UserUpdate.as_view(), name="user_update"),
    path('user/<str:pk>/', UserDetail.as_view(), name="user_detail"),
    path('users/', UserList.as_view(), name="user_list"),
    path('post/new', PostCreate.as_view(), name="new_post"),
    path('posts', PostList.as_view(), name="post_list"),
    path('post/<str:pk>', PostDetail.as_view(), name="post_detail"),
    path('post/<str:pk>/update', PostUpdate.as_view(), name="post_update"),
    path('post/<str:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('signup/', Signup.as_view(), name="sign_up"),
    path('logout/', Logout.as_view(), name='logout'),
    path('user/<str:pk>/follow', FollowUnFollow.as_view(), name="follow"),
    path('post/<str:pk>/like', Like.as_view(), name="like"),
    path('post/<str:pk>/comment/new', CommentCreate.as_view(), name="new_comment"),
    path('comment/<str:pk>/update/', CommentUpdate.as_view(), name="comment_update"),
    path('comment/<str:pk>/delete/', CommentDelete.as_view(), name="comment_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
