from rest_framework import serializers

from .models import Contact, SocialMedia


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('link',)


class ContactSerializer(serializers.ModelSerializer):
    social_media = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ('id', 'phone_number', 'email', 'address', 'social_media',)

    def get_social_media(self, obj):
        social_media = SocialMedia.objects.filter(
            contact=obj
        )
        return SocialMediaSerializer(social_media, many=True).data
