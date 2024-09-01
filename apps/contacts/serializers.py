from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'phone_number', 'email', 'address', 'insta_link', 'tg_link', 'whatsapp_link', 'threads_link', 'twitter_link')

