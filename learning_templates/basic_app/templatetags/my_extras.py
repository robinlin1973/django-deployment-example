from django import tempalte

register = template.Library()

@register.filter(name='cut)
def cut(value,arg):
    """
    this cuts out all values of "arg" from the string!
    """
    return.replace(arg,'')

# register.filter('cut',cut)
