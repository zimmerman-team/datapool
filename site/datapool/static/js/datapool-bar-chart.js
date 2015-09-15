

var DatapoolBarchart = function(){
    this.colors = ["#737b35","#f57b20","#cbb778","#717174","#3a6f8f",'#4fbdbe','#ee3b24'];  
    this.filters = null;
    this.chart = null;
    this.barchartData = [
        {'key': 'First series', 'values': [], 'color': '#4fbdbe'},
        {'key': 'Second series', 'values': [], 'color': '#ee3b24'}
    ];

    this.loaded = 0;
    this.search_boxes_loaded = false;
    this.project_id = 0
    this.init = function(){

        //console.log('in init barchart');
        this.chart = nv.models.multiBarChart();
        this.chart.x(function(d) { return d[0] })  
        this.chart.y(function(d) { return d[1] }) 
        this.chart.margin({left: 100})
        //this.chart.useInteractiveGuideline(true)
        //this.chart.showLegend(true)
        this.chart.showYAxis(true)
        this.chart.showXAxis(true)
        this.chart.height(500)
        // this.chart.interpolate("basis")
      
        this.chart.xAxis    
          .axisLabel('');

        //this.chart.yAxis.axisLabel('test y');

        d3.select('#barchart_'+this.project_id+' svg')
            .datum(this.barchartData)
            .call(this.chart);

        nv.utils.windowResize(this.chart.update);
        this.refresh();



    }

    this.createUrl = function(){
        
        var url = '/get_project_chart_data/'+$('#barchart_'+this.project_id).attr('data-id')+'/bar_chart/';
      
        return url;
    }

    this.reformatData = function(data){
        var formattedData = {};
        for(var j = 0;j < data.length;j++){


            data_set = data[j]['data'];
            x_axis = data[j]['x_axis'];
            this.search_boxes = data[j]['search_boxes'];
            this.chart.xAxis.axisLabel(x_axis);//set x axis label
            console.log('x_axis = '+x_axis);
            types = data[j]['property_type_set'];
            console.log(data[j]);
            for(type in types){
                //console.log(types);
                if(type != x_axis){
                    formattedData[type] = [];
                }
            }
            for(var i = 0; i < data_set.length;i++){
                for(type in types){
                    if(type != x_axis){
                        formattedData[type].push([data_set[i][x_axis],data_set[i][type]]);
                    }
                }
            }
        }
        return_arr = []
        i = 0;
        for(type in formattedData){
            if(type != x_axis){
                return_arr.push({'key': type, 'values': formattedData[type], 'color': this.colors[i]});
                i++;
            }
        }
        //console.log(return_arr);
        return return_arr;
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
        //console.log('url = '+url);
        var that = this;
        console.log($("#all-data").serialize());
        jQuery.ajax({
            type: 'GET',
            url: url,
            dataType: 'json',
            data:$("#all-data").serialize(),
            success: function(data){
                var formattedData = that.reformatData(data);
                if(that.search_boxes_loaded == false){
                    that.addSearchBoxes()
                }
                that.refresh(formattedData);
            }
        });
    }

    this.reDraw = function(data){
        
        this.barchartData = data;

        this.loaded++;
        if(this.loaded == 1){

            d3.select('#barchart_'+this.project_id+' svg')
            .datum(this.barchartData)
            .call(this.chart);

            this.loaded = 0;
        }

    }

    this.addSearchBoxes = function(){
        for(box_id in this.search_boxes){
            $('.bar_chart_search').append("<div>"+this.search_boxes[box_id]['name']+"<input type='text' name='"+box_id+"' id='"+box_id+"'/></div>");
        }
        this.search_boxes_loaded = true;
    }

}
