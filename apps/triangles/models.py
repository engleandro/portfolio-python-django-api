import logging
import traceback
from typing import Union

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy
from environs import Env

from main.models import BaseModel
from src.triangle import Triangle as Tri

env = Env()
env.read_env()

logger = logging.getLogger(env.str("AWS_CLOUDWATCH_LOGGER"))


def is_a_number(data):
    if not isinstance(data, Union[int, float]):
        raise ValidationError(
            gettext_lazy("%(data) is not a number (int, float)"),
            params={"data": data},
        )
    elif data <= 0:
        raise ValidationError(
            gettext_lazy("%(data) is not a positive number"),
            params={"data": data},
        )


class Triangle(BaseModel):
    class Meta:
        db_table = "triangles"

    class TriangleType(models.TextChoices):
        EQUILATERAL = "Equilateral", gettext_lazy("Equilateral")
        ISOSCELES = "Isosceles", gettext_lazy("Isosceles")
        SCALENE = "Scalene", gettext_lazy("Scalene")
        INVALID = "Invalid", gettext_lazy("Invalid")

    edge1 = models.FloatField(validators=[is_a_number], verbose_name="Edge 1")
    edge2 = models.FloatField(validators=[is_a_number], verbose_name="Edge 2")
    edge3 = models.FloatField(validators=[is_a_number], verbose_name="Edge 3")
    type = models.CharField(max_length=20, choices=TriangleType.choices)

    def type(self):
        try:
            type = Tri().type(lengths=[self.edge1, self.edge2, self.edge3]).value
            logger.info(f"Triangle({self.edge1}, {self.edge2}, {self.edge3}) is {type}")
        except ValueError:
            logger.error(traceback.format_exc())
            return "Invalid"

        if type == self.TriangleType.EQUILATERAL:
            return self.TriangleType.EQUILATERAL
        elif type == self.TriangleType.ISOSCELES:
            return self.TriangleType.ISOSCELES
        elif type == self.TriangleType.SCALENE:
            return self.TriangleType.SCALENE

    def __str__(self):
        return f"Triangle({self.edge1}, {self.edge2}, {self.edge3})"
