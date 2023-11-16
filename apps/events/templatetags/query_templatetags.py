from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def add_request_query_params(context, **params) -> str:
    """Add request query params.

    It's need to keep filtering query params after page switch.

    """
    query_params = context["request"].GET.copy()
    for param_name, param_value in params.items():
        query_params[param_name] = param_value

    return query_params.urlencode()
