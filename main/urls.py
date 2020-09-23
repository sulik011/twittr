from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from posts import views
router = SimpleRouter()

router.register('api/posts', views.PostAPIView)
router.register('api/comments', views.CommentAPIView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('', include('posts.urls'))

]

urlpatterns += router.urls