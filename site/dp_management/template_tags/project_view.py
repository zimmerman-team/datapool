from django import template

register = template.Library()

@register.inclusion_tag('show_project.html')
def show_project(project):
	return {'project': project}