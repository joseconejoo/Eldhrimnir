

/* modal js data from html */
$('#myModal1').on('show.bs.modal', function (e) {
       $(this).find('.modal-content').css({
              width:'auto', //probably not needed
              height:'auto', //probably not needed 
              'max-height':'10%'

       });

       var xadd = $(e.relatedTarget).data('id');
       var valks_action_form = $(e.relatedTarget).data('href');
       var nombre = $(e.relatedTarget).data('nombre');
       var tipo_op = $(e.relatedTarget).data('tipo');
       var pestana = $(e.relatedTarget).data('pestana_nom');
       

       if (nombre && tipo_op) {
        document.getElementById("text-mod1").innerHTML = "Confirmar "+tipo_op +" del usuario "+ nombre+"";
       }
       if (pestana) {
        document.getElementById("text-mod1").innerHTML = pestana;
       }
       //document.getElementById("pr1").innerHTML = x12[3];
       //var xsd = document.getElementById("Fbs1").acat;
       var oForm = document.forms["ProblemForm"];
       //problemform2 if modal 2
       oForm.action=valks_action_form;


       //var xsd = document.getElementById("Fbs1").acat;
       //alert(oForm.action);

       //alert(JSON.stringify(valks_action_form, null, 4));
       //accesKey o className puede significar cualquier clase de html
       //xasd=$('#abrirpop2').val(this.id);
       //alert(JSON.stringify(xasd, null, 4));
       //document.getElementById("pr1").innerHTML = xadd;
       //document.getElementById("pr1").innerHTML = "xaddT";

       //window.print("hola")

});
$('#myModal2').on('show.bs.modal', function (e) {
       $(this).find('.modal-content').css({
              width:'auto', //probably not needed
              height:'auto', //probably not needed 
              'max-height':'10%'

       });

       var xadd = $(e.relatedTarget).data('id');
       var valks_action_form = $(e.relatedTarget).data('href');
       var nombre = $(e.relatedTarget).data('nombre');
       var tipo_op = $(e.relatedTarget).data('tipo');
       var pestana = $(e.relatedTarget).data('pestana_nom');
       

       if (nombre && tipo_op) {
        document.getElementById("text-mod2").innerHTML = "Confirmar "+tipo_op +" del usuario "+ nombre+"";
       }

       if (pestana) {
        document.getElementById("text-mod2").innerHTML = pestana;
       }

       //document.getElementById("pr1").innerHTML = x12[3];
       //var xsd = document.getElementById("Fbs1").acat;

       var oForm = document.forms["ProblemForm2"];
       oForm.action=valks_action_form;
       

});


$('#myModal3').on('show.bs.modal', function (e) {
       $(this).find('.modal-content').css({
              width:'auto', //probably not needed
              height:'auto', //probably not needed 
              'max-height':'10%'

       });

       var xadd = $(e.relatedTarget).data('id');
       var valks_action_form = $(e.relatedTarget).data('href');
       var nombre = $(e.relatedTarget).data('nombre');
       var tipo_op = $(e.relatedTarget).data('tipo');
       var pestana = $(e.relatedTarget).data('pestana_nom');


       if (nombre && tipo_op) {
        document.getElementById("text-mod3").innerHTML = "Confirmar "+tipo_op +" del usuario "+ nombre+"";
       }

       if (pestana) {
        document.getElementById("text-mod3").innerHTML = pestana;
       }

       var oForm = document.forms["ProblemForm3"];
       oForm.action=valks_action_form;


});



/*

$('.container-modal .title').each(function (idx, item) {
    var winnerId = "winner-" + idx;
     this.id = winnerId;
     $(this).click(function(){
       var btn = $("#winner-" + idx);
       var span = $(".close");
       var popId = $('#win-'+ idx);
       btn.click(function() {
          $(popId).addClass('on');
          $('body').addClass('lorem');
        }); 
        span.click(function() {
           $(popId).removeClass('on');
           $('body').removeClass('lorem');
         });
       
        
     
     });
 });
  
document.getElementById('id').scrollIntoView();



  
*/
/* end modal data*/