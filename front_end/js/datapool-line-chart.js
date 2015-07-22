

var DatapoolLinechart = function(){

    this.filters = null;
    this.chart = null;
    this.lineData = [
        {'key': 'First series', 'values': [], 'color': '#4fbdbe'},
        {'key': 'Second series', 'values': [], 'color': '#ee3b24'}
    ];

    this.loaded = 0;

    this.init = function(){

        this.chart = nv.models.lineChart();
        this.chart.x(function(d) { return d[0] })  
        this.chart.y(function(d) { return d[1] }) 
        this.chart.margin({left: 60, right: 20})
        this.chart.useInteractiveGuideline(true)
        this.chart.showLegend(true)
        this.chart.showYAxis(true)
        this.chart.showXAxis(true)
        this.chart.interpolate("basis")
      
        this.chart.xAxis    
          .axisLabel('')
          .tickFormat(function(d) {
            return d3.time.format('%Y-%m-%d')(new Date(d))
          });

        this.chart.yAxis 
              .axisLabel('Amount of tweets per day')
              .tickFormat(d3.format(',r'));

        d3.select('#linechart svg')
            .datum(this.lineData)
            .call(this.chart);

        nv.utils.windowResize(this.chart.update);



    }

    this.createUrl = function(heatmapId){
        
        var url = 'get_tweets_by_day.php?parameters=';

        var parameters = [];

        parameters.push('search='+this.filters.keywords[heatmapId]);

        var start = 'start='+this.filters.from
        if (this.filters.fromtime != ''){
            start += 'T'+this.filters.fromtime;
        }
        parameters.push(start);
        var end = 'end='+this.filters.to
        if (this.filters.totime != ''){
            end += 'T'+this.filters.totime;
        }

        parameters.push(end);

        parameters = parameters.join('&');
        parameters = encodeURIComponent(parameters);
        url += parameters;
        return url;
    }

    this.reformatData = function(data){
        var formattedData = [];
        for(var i = 0; i < data.length;i++){
            var curdate = new Date(data[i].date);
            curdate = curdate.getTime();
            formattedData.push([curdate, data[i].tweets]);
        }
        return formattedData;
    }

    this.refresh = function(data, heatmapId){
        if(data){
            this.reDraw(data, heatmapId);
        } else{
            this.getData(0);
            this.getData(1);
        }
    };

    this.getData = function(heatmapId){
        var url = this.createUrl(heatmapId);
        var that = this;
        jQuery.ajax({
            type: 'GET',
            url: url,
            dataType: 'json',
            success: function(data){
                var formattedData = that.reformatData(data);
                that.refresh(formattedData, heatmapId);
            }
        });
    }

    this.reDraw = function(data, heatmapId){
        
        this.lineData[heatmapId]['values'] = data;

        this.loaded++;
        if(this.loaded == 2){

            this.lineData[0]['key'] = datapoolFilters.keywords[0];
            this.lineData[1]['key'] = datapoolFilters.keywords[1];

            d3.select('#linechart svg')
            .datum(this.lineData)
            .call(this.chart);

            this.loaded = 0;
        }

    }

}
