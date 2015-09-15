function DatapoolMap(){
    this.map = null;
    this.basemap = "zimmerman2014.hmpkg505";
    this.tl = null;
    this.filters = null;
    this.project_id = 0;
    this.loaded = 0;


    if (typeof standard_basemap !== 'undefined') {
        this.basemap = standard_basemap;
    }

    this.set_map = function(div_id, zoomposition, no_dragging){

        var mapoptions = {
            attributionControl: false,
            scrollWheelZoom: false,
            zoom: 11,
            minZoom: 9,
            maxZoom:15,
            continuousWorld: 'false',
            zoomControl: 'true'
        }

        if(no_dragging){
            mapoptions.dragging = false;
        }

        // if(zoomposition || zoomposition == null){
        //     mapoptions.zoomControl = false;
        // }

        jQuery("#"+div_id).css("min-height", "450px");
        jQuery("#"+div_id).css("min-width", "450px");
        this.map = L.map(div_id, mapoptions).setView([-1.292066, 36.821946], 11);

        if (zoomposition){
            new L.Control.Zoom({ position: zoomposition }).addTo(this.map);
        }

        this.tl = L.tileLayer('https://{s}.tiles.mapbox.com/v3/'+this.basemap+'/{z}/{x}/{y}.png', {
            maxZoom: 15
        }).addTo(this.map);

        this.heat = [];

        this.heat[0] = L.heatLayer([], {
            minOpacity: .5,
            radius: 18,
            blur: 25,
            gradient: {0.5: 'rgba(0,255,255,0.1)', 0.7: 'rgba(0,153,255,0.1)', 1: 'rgba(51,102,255,0.1)'}
        }).addTo(this.map);

        this.heat[1] = L.heatLayer([], {
            minOpacity: .5,
            radius: 18,
            blur: 25,
            gradient: {0.5: 'rgba(204,204,0,0.1)', 0.7: 'rgba(255,102,0,0.1)', 1: 'rgba(204,0,0,0.1)'}
        }).addTo(this.map);
        this.refresh(false,0);
    };

    this.resetData = function(){
        

        this.heat[0].setLatLngs([]);
        this.heat[1].setLatLngs([]);
    }

    this.refresh = function(data, heatmapId){
        if(data){
            this.reDraw(data, heatmapId);
        } else{
            this.resetData();
            this.loaded = 0;
            this.getData(data, 0);
        }
    };

    this.createUrl = function(heatmapId){

        var url = '/get_project_chart_data/'+this.project_id+'/heat_map/';
        console.log('get url = '+url);
        return url;
    }


    this.getData = function(url, heatmapId){
        var url = this.createUrl(heatmapId);
        var that = this;
        jQuery.ajax({
            type: 'GET',
            url: url,
            dataType: 'json',
            data:$("#all-data").serialize(),
            success: function(data){
                data = that.formatData(data);
                that.refresh(data, heatmapId);
            }
        });
    };

    this.formatData = function(data){
        var formattedData = {};
        this.heat = [];
        for(var j = 0;j < data.length;j++){

            this.heat[j] = L.heatLayer([], {
            minOpacity: .5,
            radius: 18,
            blur: 25,
            gradient: {0.5: 'rgba(0,255,255,0.1)', 0.7: 'rgba(0,153,255,0.1)', 1: 'rgba(51,102,255,0.1)'}
            }).addTo(this.map);

            data_set = data[j]['data'];
            this.search_boxes = data[j]['search_boxes'];
            types = data[j]['property_type_set'];
            console.log(data[j]);
            lat_field = '';
            long_field = '';
            for(prop in types){
                //console.log(types);
                if (types[prop]['type'] == 'LAT'){
                    lat_field = prop;

                }
                if (types[prop]['type'] == 'LONG'){
                    long_field = prop;

                }

            }
            formattedData[j] = {}
            formattedData[j]['data_set'] = []
            for(var i = 0; i < data_set.length;i++){
                
                    formattedData[j]['data_set'][i] = {}

                    formattedData[j]['data_set'][i]['latitude'] = data_set[lat_field];
                    formattedData[j]['data_set'][i]['latitude'] = data_set[long_field];
                
            }
        }
        
        //console.log(return_arr);
        return formattedData;


    }
    this.reDraw = function(data, heatmapId){
        console.log('formattedData = ');
        console.log(data);
        for (var i = 0;i< data.length;i++){
            data_set = data[i]['data_set']
            for (var j = 0 ;j<data_set.lenght;j++){
                this.heat[i].addLatLng([data_set[j]['latitude'], data_set[j]['longitude']]);
            }

        }

     
    }

}