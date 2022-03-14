from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, blank=False,
                             help_text="Titel")
    body = RichTextField(
        blank=True, null=True, help_text="Tekst")
    image = models.ImageField(null=True, blank=True, upload_to="images/",
                              help_text=mark_safe("Pænest hvis billedet er kvadratisk. <a href='https://croppola.com/' target='_blank'>Kan f.eks. ændres her.</a>"))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)