var datapoolFilters = {
    'keywords': ['',''],
    'to': '',
    'totime': '',
    'from': '',
    'fromtime': '',
    'excludeUsers': [],
}

var dollymap = new DatapoolMap();
dollymap.filters = datapoolFilters;
dollymap.set_map('heatmap');

var linechart = new DatapoolLinechart();
linechart.filters = datapoolFilters;
linechart.init();

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
    
    dollymap.refresh();
    linechart.refresh();
});