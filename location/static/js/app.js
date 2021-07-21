$(".pt-form-client").hide();

$('.pt-add-client').on(
  'click', function() {
    $('.pt-form-client').show(400);
  }
  );
  
$('.pt-add-client').on(
  'dblclick', function() {
    $('.pt-form-client').hide(400);
  }
  );
  


/** Update Client Event **/
$('.pt-update-client').hide();

$('.pt-edit').on(
  'click', function () {
    $('pt-update-client').show(400);
  }
  );
  
$('.pt-edit').on(
  'dblclick', function() {
    $('.pt-update-client').hide(400);
  }
  );