from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import SlugField
from django.db.models.query_utils import select_related_descend
from django.utils.text import slugify
from froala_editor.fields import FroalaField
from .helper import *

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    is_varified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

class swapmodel(models.Model):
    kit = models.object()
    kit_number = models.IntegerField(max_length=15)
    slug = models.SlugField(max_length=15 , null=True , blank=True)
    User = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()(self):

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: Optional[str] = ..., update_fields: Optional[Iterable[str]] = ...) -> None:
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
