from django.db import models
from user_app.models import User

# Create your models here.
class Phrase(models.Model):
    phrase = models.CharField(max_length=300)
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True,)
    background = models.ImageField(upload_to='images/backgrounds', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='active / not active')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='created date')

    def __str__(self):
        return self.phrase

    class Meta:
        verbose_name = 'phrase'
        verbose_name_plural = 'phrases'