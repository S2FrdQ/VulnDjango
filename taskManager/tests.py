import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Project, User

class ProjectMethodTests(TestCase):

    def test_was_project_created_recently(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        title="Practical DevSecOps"
        text="Practical DevSecOps Description"
        start_date = timezone.now()
        due_date = timezone.now() + datetime.timedelta(days=30)

        project = Project(title, text, start_date, due_date)
        self.assertEqual(project.was_created_recently(), True)

    def test_was_project_overdue(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        title="Practical DevSecOps"
        text="Practical DevSecOps Description"
        start_date = timezone.now()
        due_date = timezone.now() + datetime.timedelta(days=30)

        project = Project(title, text, start_date, due_date)
        self.assertEqual(project.is_overdue(), False)

    def test_was_project_created_with_proper_title(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        title="Practical DevSecOps"
        text="Practical DevSecOps Description"
        start_date = timezone.now()
        due_date = timezone.now() + datetime.timedelta(days=30)

        project = Project(title, text, start_date, due_date)
        self.assertEqual(project.title, text)
