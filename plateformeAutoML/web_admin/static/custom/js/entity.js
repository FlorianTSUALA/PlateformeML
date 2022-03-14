$(function () {

    /* FUNCTIONS */
    var load_form = function () {
        btn = $(this)
        $.ajax({
            url: btn.attr("data-url"), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
              $("#modal-entity").modal("show")
            },
            success: function (data) {
              $("#modal-entity .modal-content").html(data.html_form)
            }
        })
    }

    var save_form = function () {
        var form = $(this)
        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
              $("#entity-table tbody").html(data.html_entity_list)
              $("#modal-entity").modal("hide")
            }
            else {
              $("#modal-entity .modal-content").html(data.html_form)
            }
          }
        })
        return false
    }

    /* EVENTS */

    //CREATE
    $("#modal-entity").on("submit", ".js-entity-create-form", save_form)
    $(".js-create-entity").click(load_form)

    //UPDATE
    $("#entity-table").on("click", ".js-update-entity", load_form)
    $("#modal-entity").on("submit", ".js-entity-update-form", save_form)

    //DELETE
    $("#entity-table").on("click", ".js-delete-entity", load_form)
    $("#modal-entity").on("submit", ".js-entity-delete-form", save_form)

      /* INIT */
      $('#entity-table').DataTable({
          autoWidth: false,
          lengthChange: false,
          "bPaginate": false,
          language: lang_fr,
      })
});