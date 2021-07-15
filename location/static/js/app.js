$(".pt-form-adding-client").hide();

$(".pt-btn-add").on("click",
   function() {
     $(".pt-form-adding-client").show(400);
   });

$(".pt-submit-adding-client").on("click",
   function() {
     $(".pt-form-adding-client").hide(400);
   });

$(".pt-form-updating-client").hide();

$(".pt-edit-client").on("click",
   function() {
     $(".pt-form-updating-client").show(400);
   });

$(".pt-submit-updating-client").on("click",
   function() {
     $(".pt-form-updating-client").hide(400);
   });