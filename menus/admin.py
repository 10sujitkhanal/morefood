from django.contrib import admin
from .models import Menu, FoodItem
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# Register your models here.


class FoodItemInline(admin.TabularInline):
    model = FoodItem
    fields = ['name', 'price', 'image', 'image_preview']
    readonly_fields = ['image_preview']  # Add readonly fields as needed

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" height="50" />'.format(obj.image.url))
        return None

class MenuAdmin(admin.ModelAdmin):
    model = Menu
    inlines = [FoodItemInline]
    list_display = ['get_list_display',]
    
    def get_fieldsets(self, request, obj=None):
        if request.user.is_restaurant_user:
            return (
                ('Menu', {
                    'fields': ('name', 'icon'),
                }),
            )
        elif request.user.is_superuser:
            return super().get_fieldsets(request, obj)
        

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_restaurant_user:
            return qs.filter(menu__restaurant=request.user.restaurant)
        elif request.user.is_superuser:
            return qs.all()

    def get_list_display(self, request):
        def image(obj):
            if obj.icon == '':
                return format_html(
                    """<i class="fas fa-plus-circle"></i>"""
                )
            else:
                return format_html(
                    """<img src="{}" height="100px" width="100px">&nbsp;&nbsp;""",
                    obj.icon.url,
                )
        if request.user.is_restaurant_user == True:
            return ['id', 'name', image,]
        elif request.user.is_superuser == True:
            return ['id', 'name', image, 'restaurant',]

    def save_model(self, request, obj, form, change):
        if not obj.pk and request.user.is_restaurant_user:
            obj.restaurant = request.user.restaurant

        super().save_model(request, obj, form, change)
        
admin.site.register(Menu, MenuAdmin)
