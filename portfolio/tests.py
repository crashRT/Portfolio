from django.test import TestCase
from django.urls import reverse

from projects.models import ProjectsModel
from works.models import WorksModel


class PublicPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.work = WorksModel.objects.create(
            title="Test work",
            thumbnail="test.jpg",
            tag="picture",
        )
        cls.project = ProjectsModel.objects.create(
            title="Test project",
            thumbnail="test.jpg",
            abstract="Test project abstract",
        )

    def test_public_pages_render(self):
        urls = [
            reverse("top"),
            reverse("worklist"),
            reverse("worktag", args=["picture"]),
            reverse("workdetail", args=[self.work.pk]),
            reverse("projectslist"),
            reverse("projectstag", args=["web"]),
            reverse("projectsdetail", args=[self.project.pk]),
            reverse("noteslist"),
            reverse("notestag", args=["web"]),
            reverse("about"),
            reverse("contact"),
        ]

        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url, secure=True)
                self.assertEqual(response.status_code, 200)

    def test_missing_detail_pages_return_404(self):
        urls = [
            reverse("workdetail", args=[999999]),
            reverse("projectsdetail", args=[999999]),
        ]

        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url, secure=True)
                self.assertEqual(response.status_code, 404)

    def test_bootstrap_assets_are_current_and_loaded_once(self):
        response = self.client.get(reverse("top"), secure=True)
        self.assertContains(response, "bootstrap@5.3.8", count=2)
        self.assertNotContains(response, "/docs/5.2/dist/js/bootstrap.bundle.min.js")

    def test_http_requests_redirect_to_https(self):
        response = self.client.get(reverse("top"))
        self.assertRedirects(
            response,
            "https://testserver/",
            status_code=301,
            fetch_redirect_response=False,
        )
