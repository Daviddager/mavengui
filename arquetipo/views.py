import mimetypes
import os

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.forms.formsets import formset_factory
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from wsgiref.util import FileWrapper

from .forms import FieldsForm, OperationsForm, DataTypesForm
# Create your views here.
def index( request ):
    OperationsFormSet = formset_factory( OperationsForm )
    DataTypesFormSet = formset_factory( DataTypesForm )

    if request.method == 'POST':
        query_form = FieldsForm( request.POST )
        operations_formset = OperationsFormSet( request.POST, prefix='operations' )
        data_formset = DataTypesFormSet( request.POST, prefix='datas' )

        if query_form.is_valid() and operations_formset.is_valid() and data_formset.is_valid():
            group_id = query_form.cleaned_data.get( 'organizacion' )
            artifact_id = query_form.cleaned_data.get( 'proyecto' )
            version = "1.0-SNAPSHOT"
            nameSpace = query_form.cleaned_data.get( 'dominio' )
            service_name = query_form.cleaned_data.get( 'servicio' )

            operations_list = []

            for operation_form in operations_formset:
                operation = operation_form.cleaned_data.get( 'operacion' )
                if operation:
                    operations_list.append( operation )
            operations = ' '.join(operations_list)
            operations = "\"" + operations + "\""

            data_list = []

            for data in data_formset:
                operacion = data.cleaned_data.get( 'operacion' )
                mensaje = data.cleaned_data.get( 'mensaje' )
                dataName = data.cleaned_data.get( 'id_dato' )
                dataType = data.cleaned_data.get( 'tipo' )

                if operacion and mensaje and dataType and dataName:
                    dataToAdd = operacion + '-' + mensaje + '-' + dataName + '-' + dataType
                    data_list.append( dataToAdd )
            datas = ' '.join( data_list )
            datas = "\"" + datas + "\""
            print("%s" % datas)
            os.system( "yes | mvn archetype:generate -DarchetypeGroupId=nl.syntouch.examples.servicebus -DarchetypeArtifactId=MavenArchetypeService-archetype -DarchetypeVersion=1.0-SNAPSHOT -DgroupId=%s -DartifactId=%s -DnameSpace=%s -Dversion=%s -Dfields=%s -Doperations=%s -DserviceName=%s" % ( group_id, artifact_id, nameSpace, version, datas, operations, service_name ) )
            os.system( "zip -r %s.zip %s" % ( artifact_id, artifact_id ) )
            os.system( "rm -rf %s" % artifact_id )
            os.system( "mv %s.zip media" % artifact_id )
            file = 'media/%s.zip' % artifact_id
            filename = os.path.basename( file )
            chunk_size = 8192
            response = HttpResponse( FileWrapper( open( file, 'rb' ), chunk_size ), content_type = mimetypes.guess_type( file )[0] )
            response[ 'Content-Lenght' ] = os.path.getsize( file )
            response[ 'Content-Disposition' ] = 'attachment; filename = %s' % filename
            return response
    else:
        query_form = FieldsForm
        operations_formset = OperationsFormSet( prefix='operations' )
        data_formset = DataTypesFormSet( prefix='datas' )

    context = { 'form': query_form, 'operations_formset': operations_formset, 'data_formset': data_formset }

    return render( request, 'arquetipo/index.html', context )
