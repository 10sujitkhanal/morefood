from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.html import format_html
from django.urls import (
    path,
    reverse,
)
from .models import Order, OrderItem
from django.template.response import TemplateResponse


class OrderFilter(SimpleListFilter):
    title = 'Order Status'
    parameter_name = 'order_status'
    
    def lookups(self, request, model_admin):
        return (
            ('Pending', 'Pending'),
            ('Cooked', 'Cooked'),
            ('Delivered', 'Delivered'),
            ('Cancalled', 'Cancalled'),
        )
    def queryset(self, request, queryset):
        if self.value() == 'Pending':
            return queryset.filter(order_status='Pending')
        elif self.value() == 'Cooked':
            return queryset.filter(order_status='Cooked')
        elif self.value() == 'Delivered':
            return queryset.filter(order_status='Delivered')
        elif self.value() == 'Cancalled':
            return queryset.filter(order_status='Cancalled')
        else:
            return queryset.filter(order_status='Pending')

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline]
    list_editable = ('order_status',)
    list_display_links = None
    list_display = ('id', 'full_name', 'email', 'phone_no', 'restaurant', 'order_status','_invoice',)
    # filter_horizontal = ('food_items',)
    list_filter = (OrderFilter,'full_name','email', 'phone_no')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<order_id>/invoice/',
                self.admin_site.admin_view(self.invoice),
                name='order_invoice',
            ),
        ]
        return custom_urls + urls
    

    def _invoice(self, obj):
        return format_html(
            '''
            <a class="el-button el-button--light" href="{}">
            <i class="fas fa-file-invoice"></i>
            </a>''',
            reverse('admin:order_invoice', args=[obj.id]),
        )

    _invoice.short_description = 'Invoice'
    _invoice.allow_tags = True

    def invoice(self, request, order_id, *args, **kwargs):
        return self._process_invoice(request=request, order_id=order_id, action_title='View Invoice')
    
    def _process_invoice(self, request, order_id, action_title):
        order = self.get_object(request, order_id)
        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['order_items'] = OrderItem.objects.filter(order=order)
        context['order'] = order
        context['title'] = action_title
        return TemplateResponse(
            request,
            'orders/invoice.html',
            context,
        )


admin.site.register(Order, OrderAdmin)