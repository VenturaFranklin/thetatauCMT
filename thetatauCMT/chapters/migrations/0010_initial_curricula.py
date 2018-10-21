# Generated by Django 2.0.3 on 2018-09-10 02:06
import os
import csv
from django.db import migrations


def load_chapters(apps, schema_editor):
    chapter = apps.get_model("chapters", "Chapter")
    chapter_curricula = apps.get_model("chapters", "ChapterCurricula")
    with open(f'{os.path.split(__file__)[0]}/curricula.csv', newline='', encoding='windows-1252') as csvfile:
        reader = csv.DictReader(csvfile)
        for id_obj, row in enumerate(reader):
            try:
                chapter_obj = chapter.objects.get(name=row['chapter'])
            except chapter.DoesNotExist as e:
                print(row)
                raise e
            chapter_curricula(
                chapter=chapter_obj,
                major=row['major']
            ).save()


def delete(apps, schema_editor):
    chapter_curricula = apps.get_model("chapters", "ChapterCurricula")
    chapter_curricula.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0009_chaptercurricula'),
    ]

    operations = [
        migrations.RunPython(load_chapters, delete),
    ]