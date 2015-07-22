// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

// $(window).on('scroll.fndtn.magellan', function() {
// 	var originalWidth = $('div[data-magellan-expedition-clone]').width();
// 	$('div[data-magellan-expedition="fixed"]').width(originalWidth);
// });

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
    $('.configure').on('click',function(){
      $(this).parents('.panel-header').slideUp().siblings('.panel-content').slideDown();
    });
    $('.close').on('click',function(){
      $(this).parents('.panel-content').slideUp().siblings('.panel-header').slideDown();
    });
    $('.killbutton').width($('.killbutton .kill').outerWidth());
    $('.kill').on('click',function(){
      if (confirm('Are you sure?')) {
        $(this).parents('.panel').parent().parent().fadeOut(300,function(){
          $(this).remove();
        });
      }
      return false;
    });

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
    $('table.filters input[type=checkbox]').on('change', function(){
      if ($(this).is(':checked')) {
        $(this).parent().next().children('select').fadeIn(200);
        if ($(this).parent().next().children('select').val() == 'filter') {
          $(this).parent().nextAll().children('input').fadeIn(200);
        }
      }
      else {
        $(this).parent().next().children('select').fadeOut(200);
        $(this).parent().nextAll().children('input').fadeOut(200);
      }
    });
    $('table.filters select').on('change', function(){
      if ($(this).val() == 'filter') {
        $(this).parent().next().children('input').fadeIn(200);
      }
      else {
        $(this).parent().next().children('input').fadeOut(200);
      }
    });

    //add project scherm
    //linker kant
    var i = 1;
    $('#datastreams select').on('change', function() {
      if ($(this).val() && !$(this).next().is('select')) {
        $('select#datastreams0').clone(true, true).attr('id', 'datastreams'+i).appendTo('#datastreams');
        i++;
      }
    });
    //rechter kant
    $('.addstream').on('click',function(){
      var streamdiv = $(this).parent().parent().prev();
      streamdiv.children('.stream:eq(0)').clone(true, true).attr('class', 'row stream').appendTo(streamdiv);
      streamdiv.children('.stream:not(:eq(0))').find('.disabled').removeClass('disabled').addClass('delete').on('click',function(){
        $(this).parents('.stream').fadeOut(200, function() {
          $(this.remove());
        });
      });;
    });

});