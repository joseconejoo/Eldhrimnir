from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):

    return value.as_widget(attrs={'class': arg})





@register.filter(name='subC')
def substract_date(num1,num2):
    return (num1 - num2)


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
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off','placeholder': "Cédula"})
@register.filter(name='login2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Contraseña"})

@register.filter(name='login3')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Confirmar Contraseña"})

@register.filter(name='login4')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Nueva Contraseña"})

@register.filter(name='login1v2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off','placeholder': "Usuario ( Cédula )"})


@register.filter(name='datosF1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Nombre"})


@register.filter(name='datosF2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Apellido"})


@register.filter(name='datosF3')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Lugar de Residencia"})


@register.filter(name='carreraF1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Nombre"})

@register.filter(name='seccionF1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Número de sección"})

@register.filter(name='materiaF1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Nombre de la materia"})

@register.filter(name='datosAddF1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Nombre",'id':'name1'})


@register.filter(name='datosAddF2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Apellido",'id':'lastname1'})


@register.filter(name='datosTeachAddF1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Nombre",'id':'name2'})


@register.filter(name='datosTeachAddF2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Apellido",'id':'lastname2'})


@register.filter(name='teachereval1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Descripción"})

@register.filter(name='teachereval2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Ponderación"})

@register.filter(name='teachereval3')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg, 'autocomplete' : 'off',"placeholder": "Fecha"})

