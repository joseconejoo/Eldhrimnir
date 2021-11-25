

/* modal js data from html */
//$('[data-toggle = "modal"]').on('show.bs.modal', function (e) {
    $('[data-toggle = "modal"]').click(function(){
       /*
       $(this).find('.modal-content').css({
              width:'auto', //probably not needed
              height:'auto', //probably not needed 
              'max-height':'10%'

       });
       */
       var xadd = $(this).data('id');
       var valks_action_form = $(this).data('href');
       //var nombre = $(this).data('nombre');
       //var tipo_op = $(this).data('tipo');
       var pestana = $(this).data('pestana_nom');
       to_modal = $(this).data('target');

       if ($(to_modal)) {

          console.log(to_modal, pestana)
          to_modal = $(to_modal);


              /*
              if (nombre && tipo_op) {
              document.getElementById("text-mod1").innerHTML = "Confirmar "+tipo_op +" del usuario "+ nombre+"";
              }
              */

              if (pestana) {

               //console.log(pestana)
               $(".modal-title", to_modal).eq(0).text(pestana);
               } 

           form_action_modal = $('form', to_modal);
              //console.log(url_form_action);
              form_action_modal.eq(0).attr('action', valks_action_form);
              //console.log(form_action_modal.eq(0).attr('action'));

              //console.log(title_modal);
          }

          console.log($(this))


       //document.getElementById("pr1").innerHTML = x12[3];
       //var xsd = document.getElementById("Fbs1").acat;
       //var oForm = document.forms["ProblemForm"];
       //problemform2 if modal 2
       //oForm.action=valks_action_form;


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
    // tooltip help text
    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    })

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