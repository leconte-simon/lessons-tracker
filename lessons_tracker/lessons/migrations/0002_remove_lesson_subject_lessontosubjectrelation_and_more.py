import django.db.models.deletion
from django.db import migrations, models

from django.apps.registry import Apps
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def create_many_to_many_relationship_based_on_foreign_key(
    apps: Apps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    Lesson = apps.get_model("lessons", "Lesson")
    LessonToSubjectRelation = apps.get_model("lessons", "LessonToSubjectRelation")
    for lesson in Lesson.objects.all():
        LessonToSubjectRelation.objects.create(lesson=lesson, subject=lesson.subject)


class Migration(migrations.Migration):
    dependencies = [
        ("lessons", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LessonToSubjectRelation",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lessons.lesson"
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lessons.classsubject",
                    ),
                ),
            ],
            options={
                "unique_together": {("lesson", "subject")},
            },
        ),
        migrations.AddField(
            model_name="lesson",
            name="subjects",
            field=models.ManyToManyField(
                related_name="lessons",
                through="lessons.LessonToSubjectRelation",
                to="lessons.classsubject",
            ),
        ),
        migrations.RunPython(
            code=create_many_to_many_relationship_based_on_foreign_key,
        ),
        migrations.RemoveField(
            model_name="lesson",
            name="subject",
        ),
    ]
