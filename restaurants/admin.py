from django.contrib import admin
from .models import Restaurant
from django.utils.html import format_html
# Register your models here.


class RestaurantAdmin(admin.ModelAdmin):
    def image(obj):
        if obj.logo == '':
            return format_html(
                """<i class="fas fa-plus-circle"></i>"""
            )
        else:
            return format_html(
                """<img src="{}" height="100px" width="100px">&nbsp;&nbsp;""",
                obj.logo.url,
            )
    model = Restaurant
    list_display = ('name', 'email', 'contact_no', image,)
    fieldsets = (
        (None, {
            "fields": (
                'name', 'email', 'contact_no','logo'
            ),
        }),
    )
    
    search_fields = ('name','email', 'contact_no')

    

admin.site.register(Restaurant, RestaurantAdmin)
