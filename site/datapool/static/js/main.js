var datapoolFilters = {
    'keywords': ['',''],
    'to': '',
    'totime': '',
    'from': '',
    'fromtime': '',
    'excludeUsers': [],
}


$('.barchart').each(function(){
    project_id = $(this).attr('data-id');
    console.log('project_id '+project_id);
    var barchart = new DatapoolBarchart();
    barchart.filters = datapoolFilters;
    barchart.project_id = project_id;
    barchart.init()
});

var loading = false;

jQuery("#go").click(function(e){
    e.preventDefault();
    if(loading){
        return false;
    }
    loading = true;

    datapoolFilters.keywords[0] = jQuery("#keyword-0").val();
    datapoolFilters.keywords[1] = jQuery("#keyword-1").val();
    datapoolFilters.from = jQuery("#from").val();
    datapoolFilters.fromtime = jQuery("#fromtime").val();
    datapoolFilters.to = jQuery("#to").val();
    datapoolFilters.totime = jQuery("#totime").val();
    
    //dollymap.refresh();
    //linechart.refresh();
});