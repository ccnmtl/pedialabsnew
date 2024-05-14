from django.test import TestCase
from django.test.client import Client

from pedialabsnew.exercises.models import Lab, Test


class ViewsTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_delete_test_get(self):
        lab = Lab.objects.create()
        t = Test.objects.create(lab=lab)
        r = self.c.get("/exercises/delete_test/%d/" % t.id)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "<form")

    def test_delete_test_post(self):
        lab = Lab.objects.create()
        t = Test.objects.create(lab=lab)
        r = self.c.post("/exercises/delete_test/%d/" % t.id, dict())
        self.assertEqual(r.status_code, 302)
        self.assertEqual(Test.objects.all().count(), 0)

    def test_reorder_tests(self):
        lab = Lab.objects.create()
        t1 = Test.objects.create(lab=lab, ordinality=1)
        t2 = Test.objects.create(lab=lab, ordinality=2)
        r = self.c.post(
            "/exercises/reorder_tests/%d/" % lab.id,
            {
                "test_1": t2.id,
                "test_2": t1.id,
            })
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content, b"ok")
