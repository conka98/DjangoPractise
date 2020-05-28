from django import template

register = template.Library()

def slic(value):
	"""
	This filter is used to remove first and last character of a string
	"""

	return value[1:-1]


register.filter('slic',slic)