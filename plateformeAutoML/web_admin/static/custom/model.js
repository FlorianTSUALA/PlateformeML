import { lang_fr } from './js/lang.js'


var BASE_URL = ""

$(document).ready(function(){	

	var model_data = $('#dt-model').DataTable({
		"lengthChange": false,
		"processing":true,
		"serverSide":false,
		"order":[],
		"ajax":{
			url: BASE_URL,
			type: "GET",
			cache: true,
			dataType: 'json',
			"dataSrc": function (d) {
				return d['resutats']
			 }
		},
		language: lang_fr,
		"columns": [
			{ "data": null},
			{ "data": "codemag" ,"searchable":true},
			{ "data": "desigmag" ,"searchable":true},
			{ "data": "desigmag" ,"searchable":true},
			/*{ "data": "datecreate" ,"searchable":false},
			{ "data": "dateupdate" ,"searchable":false},*/
			{
				mRender: function (data, type, row) {
					// console.log(row)
					let id = row['idmag'];
					var bindHtml = '<div class=" " role="group" aria-label=" ">';
					bindHtml += '<a href="./RayonsMagasinView.php?id='+id+'" style="text-decoration: none; color: black;"><i title="Lister les... rayons de ce magasin" class="fa fa-low-vision" aria-hidden="true"></i></a>';
					bindHtml += '<a name="update" title="Modifier ce magasin" class="update" id="' + id + '" style="margin: 0 0 0 20px; text-decoration: none; color: black;"><i class="bi bi-pencil-square"></i></a>';
					bindHtml += '<a name="delete" title="Supprimer ce magasin" class="delete" id="' + id + '" style="margin: 0 0 0 20px; text-decoration: none; color: black;"><i class="bi bi-trash"></i></a></div>';
					return bindHtml;
				}
			},
			
		],
		"columnDefs": [ {
            "searchable": false,
            "orderable": false,
            "targets": 0
        } ],
		"pageLength": 10
	});		
	model_data.on( 'order.dt search.dt', function () {
        model_data.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();

	$('#addModel').click(function(){
		$('#form_model')[0].reset();
		$('#modal_model').modal('show');
		$('.modal-title').html(" Ajouter un nouveau magasin");
		$('#action').val('addApplication');
		$('#save').val('Enregistrer');
	});		

	$("#dt-model").on('click', '.update', function(){
		var idmag = $(this).attr("id");
		$.ajax({
			url: BASE_URL + idmag,
			method:"GET",
			dataType:"json",
			success:function(d){
				if(d['Nombre'] != 1)
					return 
				let data = d['resutats'][0]
				console.log(data.codemag)
				$('#modal_model').modal('show');
				$('#codemag').val(data.codemag);
				$('#desigmag').val(data.desigmag);
			
				$('#id').val(data.idmag);
				$('.modal-title').html(" Modifier magasin");
				$('#action').val('updateApplication');
				$('#save').val('Sauvegarder');
			}
		})
	});

	$("#modal_model").on('submit','#form_model', function(event){
		event.preventDefault();
		$('#save').attr('disabled','disabled');
		var formData = $(this).serialize();
		if(  $('#action').val() == 'addApplication'){
			$.ajax({
				url: BASE_URL,
				method:"POST",
				data:formData,
				success:function(data){				
					$('#form_model')[0].reset();
					$('#modal_model').modal('hide');				
					$('#save').attr('disabled', false);
					model_data.ajax.reload();
					displaySuccessMessage("Ajout effectué avec succès")
				}
			})
		}else{
			var idmag = $("input[name='id']").val();
			let data = {
				codemag: $('#codemag').val(),
				desigmag: $('#desigmag').val(),
			}
			
			$.ajax({
				url: BASE_URL + idmag,
				method:"PUT",
				data: JSON.stringify(data),
				headers: {
					"content-type": "text/plain;charset=UTF-8" 
				},
				success:function(data){				
					$('#form_model')[0].reset();
					$('#modal_model').modal('hide');				
					$('#save').attr('disabled', false);
					model_data.ajax.reload();
					displaySuccessMessage("Mise à jour effectué avec succès")
				}
			})
		}
	});	

	$("#dt-model").on('click', '.delete', function(){
		var idmag = $(this).attr("id");		
		if(confirm("Voulez-vous supprimer ce magasin?")) {
			$.ajax({
				url: BASE_URL + idmag,
				method:"DELETE",
				success:function(data) {					
					model_data.ajax.reload();
				}
			})
		} else {
			return false;
		}
	});	
});

