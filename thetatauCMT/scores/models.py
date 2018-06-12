from enum import Enum
from django.db import models
from core.models import YearTermModel
from chapters.models import Chapter


class ScoreType(models.Model):
    class SECTION(Enum):
        brotherhood = ('Bro', 'Brotherhood')
        operate = ('Ops', 'Operate')
        professional = ('Pro', 'Professional')
        service = ('Ser', 'Service')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    class TYPES(Enum):
        event = ('Evt', 'Event')
        submit = ('Sub', 'Submit')
        special = ('Spe', 'Special')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    section = models.CharField(
        max_length=3,
        choices=[x.value for x in SECTION]
    )
    points = models.PositiveIntegerField(default=0)
    formula = models.CharField(max_length=200)
    name_short = models.CharField(max_length=20)
    type = models.CharField(
        max_length=3,
        choices=[x.value for x in SECTION]
    )
    base_points = models.PositiveIntegerField(default=0)
    attendance_multiplier = models.PositiveIntegerField(default=0)
    member_add = models.PositiveIntegerField(default=0)
    special = models.CharField(max_length=200)


class ScoreChapter(YearTermModel):
    chapter = models.ForeignKey(Chapter)
    type = models.ForeignKey(ScoreType)
    score = models.PositiveIntegerField(default=0)
