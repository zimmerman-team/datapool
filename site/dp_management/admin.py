from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from models import DataConnection,DataSourceFlags,DataSource,DataSourceComment,DataModelClass,DataModelGroup,DataModelSubGroup,DataModelProperty,DataModelEdge,DataModelQuery
from django.conf.urls import patterns
from django.shortcuts import get_object_or_404


# Register your models here.

class DataModelQueryAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')

class DataSourceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','parse_status']
    def get_urls(self):
        urls = super(DataSourceAdmin, self).get_urls()
        extra_urls = patterns('',
            (r'^parse-source/$', self.admin_site.admin_view(self.parse_source)),
            
        )
        return extra_urls + urls
    def parse_source(self, request):
        source_id = request.GET.get('source_id')
        obj = get_object_or_404(DataSource, id=source_id)
        obj.process()
        return HttpResponse('Success')

admin.site.register(DataModelQuery, DataModelQueryAdmin)
admin.site.register(DataConnection)
admin.site.register(DataSourceFlags)
admin.site.register(DataSource,DataSourceAdmin)
admin.site.register(DataSourceComment)
admin.site.register(DataModelClass)
admin.site.register(DataModelGroup)
admin.site.register(DataModelSubGroup)
admin.site.register(DataModelProperty)
admin.site.register(DataModelEdge)





