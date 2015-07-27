function DatapoolMap(){
    this.map = null;
    this.basemap = "zimmerman2014.hmpkg505";
    this.tl = null;
    this.filters = null;

    this.countTweets = 0;
    this.countRetweets = 0;
    this.countMentions = 0;
    this.countUsers = {};
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
        this.map = L.map('heatmap', mapoptions).setView([-1.292066, 36.821946], 11);

        if (zoomposition){
            new L.Control.Zoom({ position: zoomposition }).addTo(this.map);
        }

        this.tl = L.tileLayer('https://{s}.tiles.mapbox.com/v3/'+this.basemap+'/{z}/{x}/{y}.png', {
            maxZoom: 15
        }).addTo(this.map);

        this.heat = [];

        this.heat[0] = L.heatLayer([], {
            minOpacity: .5,
            radius: 3,
            blur: 1,
            gradient: {0.5: 'rgba(0,255,255,0.1)', 0.7: 'rgba(0,153,255,0.1)', 1: 'rgba(51,102,255,0.1)'}
        }).addTo(this.map);

        this.heat[1] = L.heatLayer([], {
            minOpacity: .5,
            radius: 3,
            blur: 1,
            gradient: {0.5: 'rgba(204,204,0,0.1)', 0.7: 'rgba(255,102,0,0.1)', 1: 'rgba(204,0,0,0.1)'}
        }).addTo(this.map);
    };

    this.resetData = function(){
        this.countTweets = 0;
        this.countRetweets = 0;
        this.countMentions = 0;
        this.countUsers = {};

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
            this.getData(data, 1);
        }
    };

    this.createUrl = function(heatmapId){

        var url = 'get_tweets.php?parameters=';

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


    this.getData = function(url, heatmapId){
        var url = this.createUrl(heatmapId);
        var that = this;
        jQuery.ajax({
            type: 'GET',
            url: url,
            dataType: 'json',
            success: function(data){
                that.refresh(data, heatmapId);
            }
        });
    };

    this.reDraw = function(data, heatmapId){

        for (var i = 0;i< data.length;i++){
            this.heat[heatmapId].addLatLng([data[i]['fields']['latitude'], data[i]['fields']['longitude']]);

            this.countTweets++;


            if (data[i]['fields']['text'].substring(0, 2) == "RT") {
                this.countRetweets++;
            }

            if (data[i]['fields']['text'].charAt(0) == "@") {
                this.countMentions++;
            }

            this.countUsers[data[i]['fields']['u_id']] = true;
        }

        this.loaded++;
        if(this.loaded == 2){

            jQuery('#count-tweets').text(this.countTweets);
            jQuery('#count-retweets').text(this.countRetweets);
            jQuery('#count-mentions').text(this.countMentions);
            jQuery('#count-users').text(Object.keys(this.countUsers).length);

            loading = false;
        }
    }

}