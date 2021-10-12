from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import materia_seccion, carrera_seccion, carreras ,NivelesNum, Datos1


class materias_listF(forms.Form):
    choices = forms.ModelMultipleChoiceField(
        queryset = materia_seccion.objects.all(),
        widget  = forms.CheckboxSelectMultiple,
    )

class DatosAddF(forms.ModelForm):
	class Meta:
		model = Datos1
		fields = ('nombre', 'apellido')

class materia_seccion_F(forms.ModelForm):
	class Meta:
		model = materia_seccion
		fields = {'materia_nom','tipo_mate'}
		#field_order = ['tipo_mate','materia_nom']

class carrera_seccion_F(forms.ModelForm):
	class Meta:
		model = carrera_seccion
		fields = {'seccion_num',}
class carreras_add(forms.ModelForm):
	class Meta:
		model = carreras
		fields = {'nombre',}
		


class AuthenticationForm2(AuthenticationForm):
	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    self.fields['username'].widget.attrs.update({'autofocus': False})


class UserCreationForm2(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'autofocus': False})


class NivelesNumF1(forms.ModelForm):
	class Meta:
		model = NivelesNum
		fields = {'ctrl_est1',}
class Datos2rF(forms.ModelForm):
	class Meta:
		model = Datos1
		fields = ('residencia',)

class DatosF(forms.ModelForm):
	class Meta:
		model = Datos1
		fields = ('nombre', 'apellido','residencia')

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    """
	    #pdb.set_trace()

	    if self.data.get('cod_area'):
	    	cod_area2 = self.data.get('cod_area')
	    	cod_area2p = unidad2.objects.get(nom_unidad__exact=cod_area2)
	    	cod_area2 = cod_area2p.pk
	    	_mutable = self.data._mutable
	    	self.data._mutable = True
	    	self.data['cod_area'] = cod_area2
	    	self.data._mutable = _mutable
	    self.fields['nivel_usua'].queryset = NivelesNum.objects.none()
	    #self.fields['sub_area'].queryset = P_opci.objects.none()

	    if 'cod_area' in self.data:
	        try:
	            niveles_id = int(self.data.get('cod_area'))

	            self.fields['nivel_usua'].queryset = NivelesNum.objects.filter().order_by('id')
	            if niveles_id == 16:
	            	pass
	        except (ValueError, TypeError):
	            pass  # invalid input from the client; ignore and fallback to empty City queryset
	    elif self.instance.pk:
	        self.fields['nivel_usua'].queryset = self.instance.cod_area.Niveles_Num_set.order_by('name')
	    """
