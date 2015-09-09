// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

// $(window).on('scroll.fndtn.magellan', function() {
// 	var originalWidth = $('div[data-magellan-expedition-clone]').width();
// 	$('div[data-magellan-expedition="fixed"]').width(originalWidth);
// });
function getLanguageCode(){
  return  location.pathname.split("/")[1];
}

$(function() {
  $( "#from" ).datepicker({
    dateFormat: 'yy-mm-dd',
    defaultDate: new Date(2012, 6, 16),
    changeMonth: true,
    numberOfMonths: 1,
    minDate: new Date(2012, 6, 16),
    maxDate: new Date(2012, 11, 31),
    onClose: function( selectedDate ) {
      $( "#to" ).datepicker( "option", "minDate", selectedDate );
    }
  });
  $( "#to" ).datepicker({
    dateFormat: 'yy-mm-dd',
    defaultDate: new Date(2012, 6, 16),
    changeMonth: true,
    numberOfMonths: 1,
    minDate: new Date(2012, 6, 16),
    maxDate: new Date(2012, 11, 31),
    onClose: function( selectedDate ) {
      $( "#from" ).datepicker( "option", "maxDate", selectedDate );
    }
  });
});


$(document).ready(function(){

    var current_project = null;
    var configureFunc = function(){
      $(this).parents('.panel-header').slideUp().siblings('.panel-content').slideDown();
      return false;
    }
    var closeFunc = function(){
      $.cookie('hide_help', 'true');
      $(this).parents('.panel-content').slideUp().siblings('.panel-header').slideDown();
      return false;
    }

    var killFunc = function(){
      if (confirm('Are you sure?')) {
        console.log($(this).attr('data-project-id'));
        if($(this).attr('data-stream-id') != undefined){
          //console.log('data-stream-id');
          data_id = $(this).attr('data-stream-id');
          url = '/'+getLanguageCode()+"/delete_data_stream/"+data_id+"/"
          parent_id = $(this).attr('stream-parent-id');
          $('#'+parent_id).remove();
          $('#'+parent_id).fadeOut(300,function(){
            $('#'+parent_id).remove();
          });
        }
        if($(this).attr('data-project-id') != undefined){
          //console.log('data-project-id');
          data_id = $(this).attr('data-project-id');
          url = '/'+getLanguageCode()+"/delete_data_project/"+data_id+"/"
        }
        console.log(url);
        $.getJSON( url,function(data){
          return false;
        });
        $(this).parents('.panel').parent().fadeOut(300,function(){
          $(this).remove();
        });
      }
      return false;
    }

    var saveFunc = function(){
      stream_id = $(this).attr('stream-id');
      console.log('.stream_id_'+stream_id);

      $('.stream_id_'+stream_id).each(function () {
        console.log('inloop');
        stream_or_prop = $(this).attr('stream-or-prop');
        console.log(stream_or_prop);
        if(stream_or_prop == 'prop'){
          $(this).ajaxSubmit({url: '/'+getLanguageCode()+'/save_property/', type: 'post'});
        }
        else{
          $(this).ajaxSubmit({url: '/'+getLanguageCode()+'/save_data_set/', type: 'post'});
        }
      });
      return false;

    }

    var saveProjectFunc = function(){
      
      project_id = $(this).attr('project-id');
      console.log(project_id+' is project_id');
      $('#project-form-'+project_id).ajaxSubmit({url: 'save_project/', type: 'post'});
       
      return false;

    }

    var deleteStreamFunc = function(){
        
        return false;

    }

    $("select.flexselect").flexselect({
      allowMismatch: true
    });
    $("input.flexselect").attr("placeholder", "Select keyword");
    $('input.timepicker').timepicker({
      timeFormat: 'HH:mm',
      scrollbar: true
    });

    //basic panel shit
    //doe in css $('.panel-content').hide();
    $(document).on('click','.configure',configureFunc);
    $(document).on('click','.close',closeFunc);
    $('.killbutton').width($('.killbutton .kill').outerWidth());
    $(document).on('click','.kill',killFunc);
    $(document).on('click','.delete-stream-from-project',deleteStreamFunc);
    $(document).on('click','.save',saveFunc);

    $(document).on('click','.save-project',saveProjectFunc);

    //add data scherm
    $('#filter-subgroup').hide();
    $('#filter-group').on('change', function(){
      if ($(this).val()) {
        $('#filter-subgroup').fadeIn(200);
      }
      else {
        $('#filter-subgroup').fadeOut(200);
      }
    });

    $('table.filters select, table.filters input[type=text]').hide();
    $('table.filters input[type=checkbox]:checked').parent().next().children('select').show();
    $('table.filters select:has(option[value="filter"]:selected)').parent().next().children('input').show();
    $(document).on('change','table.filters input[type=checkbox]', function(){
      if ($(this).is(':checked')) {
        $(this).parent().next().children('select').fadeIn(200);
        if ($(this).parent().next().children('select').val() == '7') {
          $(this).parent().nextAll().children('input').fadeIn(200);
        }
      }
      else {
        $(this).parent().next().children('select').fadeOut(200);
        $(this).parent().nextAll().children('input').fadeOut(200);
      }
    });
    $(document).on('change','table.filters select', function(){
      if ($(this).val() == '7') {
        $(this).parent().next().children('input').fadeIn(200);
      }
      else {
        $(this).parent().next().children('input').fadeOut(200);
      }
    });
    $('table.filters select').trigger('change');
    $('table.filters input[type=checkbox]').trigger('change');

    //add project scherm
    //linker kant
    var i = 1;
    $(document).on('change','#datastreams select', function() {
      if ($(this).val() && !$(this).next().is('select')) {
        $('select#datastreams0').clone(true, true).attr('id', 'datastreams'+i).appendTo('#datastreams');
        i++;
      }
      return false;
    });
    //rechter kant
    $(document).on('click','.addstream',function(){
      var streamdiv = $(this).parent().parent().prev();
      streamdiv.children('.stream:eq(0)').clone(true, true).attr('class', 'row stream').appendTo(streamdiv);
      streamdiv.children('.stream:not(:eq(0))').find('.disabled').removeClass('disabled').addClass('delete').on('click',function(){
        $(this).parents('.stream').fadeOut(200, function() {
          $(this.remove());
        });
      });
      return false;
    });
    //select data set category
    $(document).on('change','#cat',function() {
      category_id = $(this).val();
      console.log('category id = '+category_id);
      $.getJSON( '/'+getLanguageCode()+"/get_sub_categories/"+category_id+"/",function(data){
        $('#subcat').empty()
        for(sub_cat_id in data){
          $('#subcat').append($("<option />").val(sub_cat_id).text(data[sub_cat_id]));
        }
        $("#subcat option:first").attr('selected','selected');
        $('#subcat').trigger('change');
      });
     
    }

    );
    //select subcategory
    $(document).on('change','#subcat',function() {
      sub_category_id = $(this).val();
      console.log('sub cat id = '+sub_category_id);
      $.getJSON( '/'+getLanguageCode()+'/get_data_streams/'+sub_category_id+"/",function(data){
        $('#stream').empty()
        for(stream in data){
          console.log(data[stream]);
          $('#stream').append($("<option />").val(stream).text(data[stream]));
        }
      });
    }

    );
    //preselect first option and fire change
    $("#cat option:first").attr('selected','selected');
    $('#cat').trigger('change');

    $(document).on('click','#go',function(){
      stream_id = $("#stream").val();
      console.log('stream id = '+stream_id);projectproject
      if($('#name').val() == ''){
        alert('give data stream a name');
        return false;

      }
      $(this).parents('form:first').submit();

    }
    );
    $(document).on('click','#refresh-data',function(){
        barchart.getData();
        return false;
    });
    $(document).on('click','.visualize',function(){
        project_id = $(this).attr('project-id');
        window.location = '/'+getLanguageCode()+'/visualize_project/'+project_id+'/';
        return false;
    });

    /* nieuwe shizniz; design 2.0 */

    //klikbaarheid op projects page
    $(document).on('click','.project-new-button',function(){
      $('.project-new').toggleClass('expanded');
    });

    $(document).on('click','.submit-project-new',function(){
      language_code = getLanguageCode();
      $('#new-project-form').ajaxSubmit({
          url: '/'+language_code+'/add_project/', 
          type: 'post',
          success: function(responseText, statusText, xhr, $form){  
            $('#new-projects').prepend(responseText);
            $('#new-project-form').trigger("reset");
            $('.project-new').toggleClass('expanded');


            return false;
          }
        });
        return false;

    });

    $(document).on('click','.header.main',function(){
      $(this).parent('.panel').toggleClass('expanded');
    });

    $(document).on('click','button.configure',function(){
      $(this).parents('.header').next('.content').toggleClass('fullvis');
    });

    $(document).on('click','.add-data-stream',function(){
        project_id= $(this).attr('projectid');
        console.log(project_id);
        current_project = project_id;
        $('#choose-stream-'+project_id).append($( ".choose-dataset" ).html());
        $( ".choose-dataset" ).html('');
        // $( ".choose-dataset" ).dialog({
        //   dialogClass: "no-close",
        //   buttons: [
        //     {
        //       text: "OK",
        //       click: function() {
        //         stream_id = $('#stream').val();
        //         name= $('#name').val();
                
        //         console.log(project_id);
        //         csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        //         url = "/"+getLanguageCode()+"/add_dataset_to_project/"
        //         $.ajax({
        //          type: "POST",
        //          url: url,
        //          data: {'name':name,'stream_id':stream_id,'project_id':project_id,'csrfmiddlewaretoken':csrfmiddlewaretoken}, // serializes the form's elements.
        //          success: function(data)
        //          {
        //              $('#new-streams-'+project_id).prepend(data); // show response from the php script.
        //          }
        //        });
        //         $( this ).dialog( "close" );
        //       }
        //     }
        //   ]
        // });

    });
    $(document).on('click','.submit-stream-new',function(){
        stream_id = $('#stream').val();
        name= $('#name').val();
        
        console.log(project_id);
        csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        url = "/"+getLanguageCode()+"/add_dataset_to_project/"
        $.ajax({
         type: "POST",
         url: url,
         data: {'name':name,'stream_id':stream_id,'project_id':project_id,'csrfmiddlewaretoken':csrfmiddlewaretoken}, // serializes the form's elements.
         success: function(data)
         {
             $('#new-streams-'+project_id).prepend(data); // show response from the php script.
         }
       });
      $( ".choose-dataset" ).html($('#choose-stream-'+project_id).html());
      $('#choose-stream-'+project_id).html('');

    });


});