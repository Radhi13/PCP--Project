from django.db import models
#from blog.models import Post


# Create your models here.

class Feedback(models.Model):
    user_name = models.CharField(max_length=120)
    email = models.EmailField()
    #post= models.ForeignKey(Post)
    feedback = models.TextField()
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.user_name

