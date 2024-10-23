from django.core.management import call_command
from io import StringIO
from django.test import TestCase


class MigrationTest(TestCase):
    def test_up_to_date_migrations(self) -> None:
        output = StringIO()
        call_command("makemigrations", no_input=True, dry_run=True, stdout=output)
        assert output.getvalue().strip() == "No changes detected", (
            "There are missing migrations:\n %s" % output.getvalue()
        )
