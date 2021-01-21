from django.test import TestCase

# Create your tests here.
class Post(models.Model):
    desc = models.TextField()
    image = models.ImageField(upload_to='post_pics', default='default.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.desc

    @classmethod
    def get_all_posts(cls):
        return cls.objects.order_by('-date_posted')

    @classmethod
    def delete_post(cls, post_id):
        post = cls.objects.filter(pk=post_id)
        post.delete()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) 
    


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content