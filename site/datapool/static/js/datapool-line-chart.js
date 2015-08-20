

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
          .axisLabel('test x');

        this.chart.yAxis 
              .axisLabel('test y');

        d3.select('#linechart svg')
            .datum(this.lineData)
            .call(this.chart);

        nv.utils.windowResize(this.chart.update);
        this.refresh()



    }

    this.createUrl = function(){
        
        var url = '/get_queries/'+$('#linechart').attr('data-id')+'/';

        // var parameters = [];


        // var start = 'start='+this.filters.from
        // if (this.filters.fromtime != ''){
        //     start += 'T'+this.filters.fromtime;
        // }
        // parameters.push(start);
        // var end = 'end='+this.filters.to
        // if (this.filters.totime != ''){
        //     end += 'T'+this.filters.totime;
        // }http://datapool.bitofpepper.com/en/add_data

        // parameters.push(end);

        // parameters = parameters.join('&');
        // parameters = encodeURIComponent(parameters);
        // url += parameters;
        return url;
    }

    this.reformatData = function(data){
        var formattedData = [];
        for(var j = 0;j < data.length;j++){
            types = data[j]['property_types_set'];
            data_set = data[j]['data'];
            x_axis = data[j]['x_axis'];
            console.log('x_axis = '+x_axis);
            for(var i = 0; i < data_set.length;i++){
                formattedData.push([data_set[i][x_axis],23]);
            }
        }
        
        return formattedData;
    }

    this.refresh = function(data){
        if(data){
            this.reDraw(data);
        } else{
            this.getData();
        }
    };

    this.getData = function(){
        var url = this.createUrl();
        console.log('url = '+url);
        var that = this;
        jQuery.ajax({
            type: 'GET',
            url: url,
            dataType: 'json',
            success: function(data){
                var formattedData = that.reformatData(data);
                that.refresh(formattedData);
            }
        });
    }

    this.reDraw = function(data){
        
        this.lineData[0]['values'] = data;

        this.loaded++;
        if(this.loaded == 1){

            console.log('in redraw');
            console.log(data);
            d3.select('#linechart svg')
            .datum(this.lineData)
            .call(this.chart);

            this.loaded = 0;
        }

    }

}
