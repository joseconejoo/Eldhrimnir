from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):

    return value.as_widget(attrs={'class': arg})

"""
def addcss(value, arg):
    css_classes = value.field.widget.attrs.get('class', '').split(' ')
    if css_classes and arg not in css_classes:
        css_classes = '%s %s' % (css_classes, arg)
    return value.as_widget(attrs={'class': css_classes})
"""

@register.filter(name='addplaceh')
def addclass(value, arg):
    return value.as_widget(attrs={'placeholder': arg})


@register.filter(name='login1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,'placeholder': "Cédula"})
@register.filter(name='login2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Contraseña"})

@register.filter(name='login3')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Confirmar Contraseña"})



@register.filter(name='login1v2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,'placeholder': "Usuario ( Cédula )"})


@register.filter(name='datosF1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Nombre"})


@register.filter(name='datosF2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Apellido"})


@register.filter(name='datosF3')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Lugar de Residencia"})


@register.filter(name='carreraF1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Nombre"})

@register.filter(name='seccionF1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Número de sección"})

@register.filter(name='materiaF1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Nombre de la materia"})
