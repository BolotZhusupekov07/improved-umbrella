from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Course, Contact, Category, Branch


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['type', 'value']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'imgpath']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longitude', 'address']


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description',
                  'category', 'logo', 'contacts', 'branches']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')

        category = Category.objects.get_or_create(name=category_data['name'],
                                                  imgpath=category_data['imgpath'])
        category_id = Category.objects.filter(
            name=category_data['name'], imgpath=category_data['imgpath']).first().id
        courses = Course.objects.create(
            category_id=category_id, **validated_data)

        contacts = []
        for contact_data in contacts_data:
            contact, _ = Contact.objects.get_or_create(type=contact_data['type'],
                                                       value=contact_data['value'],
                                                       defaults=contact_data)
            contacts.append(contact)
        courses.contacts.add(*contacts)

        branches = []
        for branch_data in branches_data:
            branch, _ = Branch.objects.get_or_create(latitude=branch_data['latitude'],
                                                     longitude=branch_data['longitude'],
                                                     address=branch_data['address'],
                                                     defaults=branch_data)
            branches.append(branch)
        courses.branches.add(*branches)

        return courses
