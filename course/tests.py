from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
from django.urls import reverse
from .models import Branch, Category, Contact, Course


client = Client()


class CourseListTests(APITestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)

    def test_get_list(self):
        """
        Ensure we can get list of courses.
        """
        url = reverse('courses')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CourseTests(APITestCase):
    def test_create_course(self):
        """
        Ensure we can create a new course object.
        """
        url = reverse('courses')
        data = {
            "name": "Udemy",
            "description": "Udemy, Inc. is an American massive open online course provider aimed at professional adults and students. It was founded in May 2010 by Eren Bali, Gagan Biyani, and Oktay Caglar.",
            "category": {
                    "name": "programming course",
                            "imgpath": "media/courses_img/udemy.png"
            },
            "logo": "media/courses_logo/udemy.png",
            "contacts": [
                    {
                        "type": "FA",
                        "value": "@Udemy"
                    },
                {
                        "type": "EM",
                        "value": "udemy@gmail.com"
                    }
            ],
            "branches": [
                {
                    "latitude": "556556238",
                    "longitude": "895656223",
                    "address": "San Francisco, CA 94107"
                },
                {
                    "latitude": "565421788",
                    "longitude": "8956562573",
                    "address": "Denver, CO 80202"
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CourseDetailListTests(APITestCase):
    def setUp(self):
        Category.objects.get_or_create(name='programming',
                                       imgpath='media/category_img/programming.png')
        category_id = Category.objects.filter(name='programming',
                                              imgpath='media/category_img/programming.png').first().id
        self.course = Course.objects.create(name='Neobis',
                                            description='This is a programming course',
                                            category=Category(category_id),
                                            logo='media/coures_img/neobis.png')
        contacts = []
        contact = Contact.objects.create(type='PH', value='521321065')
        contact2 = Contact.objects.create(type='FA', value='@neobis')
        contacts.append(contact)
        contacts.append(contact2)
        branches = []
        branch = Branch.objects.create(latitude='645312123',
                                       longitude='652623526',
                                       address='Bishkek, green street 56')
        branches.append(branch)
        self.course.contacts.add(*contacts)
        self.course.branches.add(*branches)

    def test_get_detail_view(self):
        """
        Ensure we can get detail view of a course.
        """

        url = reverse('course_detail', kwargs={'pk': self.course.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_detail_view(self):
        """
        Ensure we can get detail view of a course.
        """

        url = reverse('course_detail', kwargs={'pk': 5})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_course_delete(self):

        url = reverse('course_detail', kwargs={'pk': self.course.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.get_or_create(name='programming',
                                       imgpath='media/category_img/programming.png')
        category_id = Category.objects.filter(name='programming',
                                              imgpath='media/category_img/programming.png').first().id
        course = Course.objects.create(name='Neobis',
                                            description='This is a programming course',
                                            category=Category(category_id),
                                            logo='media/coures_img/neobis.png')
        contacts = []
        contact = Contact.objects.create(type='PH', value='521321065')
        contact2 = Contact.objects.create(type='FA', value='@neobis')
        contacts.append(contact)
        contacts.append(contact2)
        branches = []
        branch = Branch.objects.create(latitude='645312123',
                                       longitude='652623526',
                                       address='Bishkek, green street 56')
        branches.append(branch)
        course.contacts.add(*contacts)
        course.branches.add(*branches)

    def test_name(self):
        course = Course.objects.last()
        name = course._meta.get_field('name').verbose_name
        self.assertEqual(name, 'name')

    def test_description(self):
        course = Course.objects.last()
        description = course._meta.get_field('description').verbose_name
        self.assertEqual(description, 'description')

    def test_category(self):
        course = Course.objects.last()
        category = course._meta.get_field('category').verbose_name
        self.assertEqual(category, 'category')

    def test_logo(self):
        course = Course.objects.last()
        logo = course._meta.get_field('logo').verbose_name
        self.assertEqual(logo, 'logo')

    def test_contacts(self):
        course = Course.objects.last()
        contacts = course._meta.get_field('contacts').verbose_name
        self.assertEqual(contacts, 'contacts')

    def test_branches(self):
        course = Course.objects.last()
        branches = course._meta.get_field('branches').verbose_name
        self.assertEqual(branches, 'branches')

    def test_count(self):
        count_of_courses = len(Course.objects.all())
        self.assertEqual(1, count_of_courses)
