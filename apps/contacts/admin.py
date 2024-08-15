from django.contrib import admin
from .models import Contact, SocialMedia

class SocialMediaInline(admin.StackedInline):
    model = SocialMedia
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    inlines = (SocialMediaInline, )

admin.site.register(Contact, ContactAdmin)
admin.site.register(SocialMedia)

