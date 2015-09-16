from django import template

register = template.Library()

@register.inclusion_tag('show_project.html')
def show_project(project):
	chart_types = {}
	for data_set in project.data_streams.all():
		chart_types[data_set.get_chart_type_display()] = True

	return {'project': project,'chart_types':chart_types}