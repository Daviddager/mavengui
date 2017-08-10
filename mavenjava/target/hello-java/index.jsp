<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Generar Un Proyecto Telefonica</title>
        <link rel="stylesheet" href="resources/css/styles.css">
        <link href='https://fonts.googleapis.com/css?family=Alegreya Sans' rel='stylesheet'>
        <link rel="icon" href="resources/images/icon.png" >
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
            <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
      <div id="wrapper">
        <div class="page-header">
          <h1><a href="google.com"><img class="logo" src="resources/images/company_logo.png" height="42"></a></h1>
        </div>
        <div class="content container">
          <div class="row">
            <div class="col-md-8">
                <h1>Argumentos del proyecto</h1>
	<form method = "post" >
		<div class="fields">
			{% csrf_token%}
			{{ form.as_table }}
		</div>
		</br>
		<div class="maven-arguments">
			<div class="row">
				<div class="operations">
					<h1>Operaciones del proyecto</h1>
					{% for f_form in operations_formset %}
						<div class="operation-formset">
							{{ f_form.as_table }}
						</div>
					{% endfor %}
					{{ operations_formset.management_form }}
				</div>

				<div class="data">
					<h1>Datos</h1>
					{% for d_form in data_formset %}
						<div class="data-formset">
							<label> Número de Operacion</label>
							{{ d_form.operacion }}<br/>
							<label> Tipo de Operación </label>
							{{ d_form.mensaje }}
							<label>Id Dato</label>
							{{ d_form.id_dato }}
							<label>Tipo</label>
							{{ d_form.tipo }}
							<!-- {{ d_form.as_table }} -->
						</div>
					{% endfor %}
					{{ data_formset.management_form }}
				</div>
		</div>
	</div>
	</br>
		<button types='submit' value='generate'>Generar</button>
	</form>

            </div>
          </div>
        </div>
        <div class="footer">
        </div>
      </div>
    </body>
</html>
