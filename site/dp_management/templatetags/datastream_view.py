from django import template

register = template.Library()

@register.inclusion_tag('show_datastream.html')
def show_datastream(data_stream):
	return {'data_stream': data_stream}