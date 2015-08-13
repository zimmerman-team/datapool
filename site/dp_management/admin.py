from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from models import DataModelScript,DataConnection,DataSourceFlags,DataSource,DataSourceComment,DataModelClass,DataModelGroup,DataModelSubGroup,DataModelProperty,DataModelEdge,DataModelQuery,DataSourceCategory,DataSourceSubCategory
from django.conf.urls import patterns
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


# Register your models here.

class DataModelQueryAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')

class DataSourceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','parse_status','django_models','orient_models']
    def get_urls(self):
        urls = super(DataSourceAdmin, self).get_urls()
        extra_urls = patterns('',
            (r'^parse-source/$', self.admin_site.admin_view(self.parse_source)),
            (r'^create-django-schema/$', self.admin_site.admin_view(self.create_django_schema)),
            (r'^create-orient-schema/$', self.admin_site.admin_view(self.create_orient_schema)),
        )
        return extra_urls + urls
    def parse_source(self, request):
        source_id = request.GET.get('source_id')
        obj = get_object_or_404(DataSource, id=source_id)
        obj.process()
        return HttpResponse('Success')

    def create_django_schema(self, request):
        source_id = request.GET.get('source_id')
        obj = get_object_or_404(DataSource, id=source_id)
        obj.create_django_schema()
        return HttpResponse('Success')

    def create_orient_schema(self, request):
        source_id = request.GET.get('source_id')
        obj = get_object_or_404(DataSource, id=source_id)
        obj.create_orient_schema()
        return HttpResponse('Success')




class DataModelPropertyInline(admin.TabularInline):
    model = DataModelProperty

class DataModelClassAdmin(admin.ModelAdmin):
    inlines = [DataModelPropertyInline]
    list_display = ['__unicode__', ]
    change_form_template_extends = 'admin/hvad/change_form.html'

admin.site.register(DataModelQuery, DataModelQueryAdmin)
admin.site.register(DataConnection)
admin.site.register(DataSourceFlags)
admin.site.register(DataSource,DataSourceAdmin)
admin.site.register(DataSourceComment)
admin.site.register(DataModelClass, DataModelClassAdmin)
admin.site.register(DataModelGroup)
admin.site.register(DataModelSubGroup)
admin.site.register(DataModelProperty,)
admin.site.register(DataModelEdge)
admin.site.register(DataSourceCategory)
admin.site.register(DataSourceSubCategory)
admin.site.register(DataModelScript)






