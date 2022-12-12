from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.fields.DateTimeField(auto_now_add=True)
    updated_at = models.fields.DateTimeField(auto_now=True)
    is_active = models.fields.BooleanField(default=True)
