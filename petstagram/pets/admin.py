from django.contrib import admin

from petstagram.pets.models import Pet, Like


class PetAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'age', 'description','likes_count')
    list_filter = ('type', )

    def likes_count(self, obj):
        return obj.like_set.count()


class LikeAdmin(admin.ModelAdmin):
    list_display = ('pet', )



admin.site.register(Pet, PetAdmin)
admin.site.register(Like,LikeAdmin)
