from django import forms
from django.core.exceptions import ValidationError
from django.forms.formsets import BaseFormSet

# datos basicos del proyecto Arquetype, artifact, etc
class FieldsForm( forms.Form ):
    organizacion = forms.CharField(
            required = True,
            max_length = 20,
            widget = forms.TextInput( attrs = {
                'placeholder':'Nombre de la Organizacion',
                } ),
            )
    proyecto = forms.CharField(
            required = True,
            max_length = 20,
            widget = forms.TextInput( attrs = {
                'placeholder':'Nombre del Proyecto',
                } ),
            )
    servicio = forms.CharField(
            required = True ,
            max_length = 20,
            widget = forms.TextInput( attrs = {
                'placeholder':'Nombre del servicio',
                } ),
            )
    dominio = forms.CharField(
            required = True ,
            max_length = 20,
            widget = forms.TextInput( attrs = {
                'placeholder':'Direccion del dominio',
                } ),
            )
# Operaciones
class OperationsForm( forms.Form ):
    operacion = forms.CharField(
            required = True,
            max_length = 20,
            widget = forms.TextInput( attrs = {
                'placeholder':'Nombre de operacion'
                } ),
            )
# Tipos de datos
class DataTypesForm( forms.Form ):
    operacion = forms.CharField(
            required = True,
            widget = forms.TextInput( attrs = {
                'type':'number',
                'min':'1' ,
                'size': 1,
                } ),
    )
    CHOICES = ( ( '1', 'Request' ), ( '2', 'Response' ) )
    mensaje = forms.ChoiceField(
            required = True,
            widget = forms.RadioSelect,
            choices = CHOICES,
    )

    id_dato = forms.CharField(
            required = True,
            max_length = 20,
            widget = forms.TextInput( attrs = {
                'placeholder':'Nombre del dato'
            } ),
    )
    TYPES = ( ( 'integer', 'Integer' ),
        ( 'decimal', 'Decimal' ),
        ( 'string', 'String' ),
        ( 'token', 'Token' ),
        ( 'date', 'Date' ),
        ( 'time', 'Time' ),
        ( 'dateTime', 'Date Time' ),
        ( 'boolean', 'Boolean' ),
        ( 'anyURI', 'Any URI' ),
        ( 'complex', 'Complex' ),
     )
    tipo = forms.ChoiceField(
            required = True,
            choices = TYPES,
    )
