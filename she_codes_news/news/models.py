from django.contrib.auth import get_user_model
from django.db import models

CAT_CHOICES = (
    ('cat', 'CAT'),
    ('dog','DOG'),
    ('horse','HORSE'),
    ('duck','DUCK'),
    ('other','OTHER'),
)



class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(default="https://stickershop.line-scdn.net/stickershop/v1/product/3710576/LINEStorePC/main.png;compress=true")
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    content = models.TextField()
    catergory = models.CharField(max_length=6, choices=CAT_CHOICES, default='select')




