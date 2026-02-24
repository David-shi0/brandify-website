from django import template

register = template.Library()

@register.simple_tag
def meta_tags():
    return {
        'description': 'Brandify - Digital Marketing Agency in Dar es Salaam. We help businesses build powerful, authentic brands that connect with people and drive sales.',
        'keywords': 'digital marketing, branding, social media, advertising, Dar es Salaam, Tanzania',
        'author': 'Brandify',
    }