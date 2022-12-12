from django.db import models

from main.models import BaseModel

class Triangle(BaseModel):
    class Meta:
        db_table = 'triangles'
