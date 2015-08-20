var datapoolFilters = {
    'keywords': ['',''],
    'to': '',
    'totime': '',
    'from': '',
    'fromtime': '',
    'excludeUsers': [],
}

if(! $('#heatmap').length == 0){
    var dollymap = new DatapoolMap();
    dollymap.filters = datapoolFilters;
    dollymap.set_map('heatmap');
}

if(! $('#linechart').length == 0){
    var linechart = new DatapoolLinechart();
    linechart.filters = datapoolFilters;
    linechart.init();
}
if(! $('#barchart').length == 0){

    var barchart = new DatapoolBarchart();
    barchart.filters = datapoolFilters;
    barchart.init();
}

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