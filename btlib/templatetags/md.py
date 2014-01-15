from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
register = template.Library()

@register.filter(name='markdown')
def markdown(value, arg=''):
    try:
        import markdown2
    except ImportError:
        if settings.DEBUG:
            raise template.TemplateSyntaxError, "Error in {% markdown %} filter: Failed loading markdown2 library. Library isn't installed."
        return force_unicode(value)
    else:
        def parse_extra(extra):
            if ':' not in extra:
                return (extra, {})
            name, values = extra.split(':', 1)
            values = dict((str(val.strip()), True) for val in values.split('|'))
            return (name.strip(), values)

        extras = (e.strip() for e in arg.split(','))
        extras = dict(parse_extra(e) for e in extras if e)

        if 'safe' in extras:
            del extras['safe']
            safe_mode = True
        else:
            safe_mode = False

        return mark_safe(markdown2.markdown(force_unicode(value), extras=extras, safe_mode=safe_mode))