from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from models import DataConnection,DataSourceFlags,DataSource,DataSourceComment,DataModelClass,DataModelGroup,DataModelSubGroup,DataModelProperty,DataModelEdge,DataModelQuery
# Register your models here.

class DataModelQueryAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')

admin.site.register(DataModelQuery, DataModelQueryAdmin)
admin.site.register(DataConnection)
admin.site.register(DataSourceFlags)
admin.site.register(DataSource)
admin.site.register(DataSourceComment)
admin.site.register(DataModelClass)
admin.site.register(DataModelGroup)
admin.site.register(DataModelSubGroup)
admin.site.register(DataModelProperty)
admin.site.register(DataModelEdge)





