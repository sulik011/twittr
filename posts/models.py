from django.db.models import Q
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ArticleManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(title__icontains=query) | Q(content__icontains=query))
            qs = qs.filter(or_lookup)

        return qs

class Post(models.Model):
    objects = ArticleManager()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=80)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default=None, null=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ('-publish',)




class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
