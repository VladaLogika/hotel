from django.contrib import admin

from testing.models import Post, Room

admin.site.register(Post)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'price_per_night')
    search_fields = ('name',)






# Register your models here.
