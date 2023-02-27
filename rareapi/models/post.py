from django.db import models

class Post(models.Model):
    user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    publication_date = models.DateField(auto_now_add=True)
    image_url = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    approved = models.BooleanField(null=False)