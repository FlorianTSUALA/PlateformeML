$(function() {
	"use strict";

    $(document).ready(function() {
        $('#example').DataTable(
            { 
                autoWidth: false,
                lengthChange: false,
                "bPaginate": false,
                language: { search: "",searchPlaceholder: "Search" }
            }
        );
      } );


      $(document).ready(function() {
        var table = $('#example2').DataTable( {
            lengthChange: false,
            buttons: [ 'copy', 'excel', 'pdf', 'print']
        } );
     
        table.buttons().container()
            .appendTo( '#example2_wrapper .col-md-6:eq(0)' );
    } );


});