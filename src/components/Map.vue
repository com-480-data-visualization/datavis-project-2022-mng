<template>
  <div style="margin-top:75px;padding-top: 75px" id="map">
    <div class="in-center">
    <ul  v-if="energyData_solar.canton.label === 'canton'">
        <li class="list-region"> <span style="font-weight: 900">Country: </span> {{'Switzerland'}} </li>
        <li class="list-region"><span style="font-weight: 900"> | Hovered Region: </span> {{province.name}} </li>
    </ul>
    <ul  v-else-if="energyData_solar.commune.label !== 'commune'">
        <li class="list-region"> <strong>Country: </strong>{{'Switzerland'}}, </li>
        <li class="list-region"> <strong>Canton: </strong>{{energyData_solar.canton.label}}, </li>
        <li class="list-region"> <strong>Commune: </strong>{{energyData_solar.commune.label}} </li>
        <li class="list-region"> <strong> | Hovered Region: </strong>{{province.name}} </li>
    </ul>
    <ul v-else>
        <li class="list-region"> <strong>Country: </strong>{{'Switzerland'}}, </li>
        <li class="list-region"> <strong>Canton: </strong>{{energyData_solar.canton.label}} </li>
        <li class="list-region"> <strong> | Hovered Region: </strong>{{province.name}} </li>
    </ul>
    </div>
    <div class="center-screen" id="main-div" style="border-color: black;border-style: solid;border-width: thin;">
      <div
          class="map-div"
          id='chart' >
      </div>
      <div  class="province-info">
        <h3 class="text-center">{{currentProvince.state}}</h3>
        <BarChart :dataEnergies="energyData_solar" :width=250 :height=135 title='Solar Potential Usage' ></BarChart>
        <BarChart :dataEnergies="energyData_heating" :width=250 :height=135 title="Renewable Heating Share"></BarChart>
        <BarChart :dataEnergies="energyData_car" :width=250 :height=135 title="Electric Car Share"></BarChart>
      </div>
      <div  class="province-info">
        <h3 class="text-center">{{currentProvince.state}}</h3>
        <BarChart :dataEnergies="energyData_solar_perc_contr" :width=300 :height=135 title='Solar Potential Usage Relative Contribution (log scale)' :logarithmic=true></BarChart>
        <BarChart :dataEnergies="energy_Data_heating_perc_contr" :width=300 :height=135 title="Renewable Heating Share Relative Contribution (log scale)" :logarithmic=true></BarChart>
        <BarChart :dataEnergies="energyData_car_perc_contr" :width=300 :height=135 title="Electric Car Share Relative Contribution (log scale)" :logarithmic=true></BarChart>
      </div>
    </div>
  </div>
</template>

<script>
import bbox from "@turf/bbox";
import * as d3 from 'd3'
import json from '../data/cantons.topo.json';
import json2 from '../data/communes.topo.json';
import Pie from "./Pie";
import BarChart from "./BarChart";
import mapHelpers from "../helpers/map_helpers";

//import * as topojson from 'topojson-server';
import * as topojson from "topojson-client";
export default {
  name: "Map",
  components: {BarChart},

  //define data
  data() {
    return {

      //canton data
      cantons: topojson.feature(json,json.objects.cantons),
      //communes data
      communes: topojson.feature(json2,json2.objects.communes),
      province: {name: ''},

      currentProvince: {name: 'Switzerland'},

      default_canton_energy_data : {
                                      data: [null],
                                      population: null,
                                      label: 'canton'
                                    },
      default_commune_energy_data: {
                                      data: [null],
                                      population: null,
                                      label: 'commune'
                                    },
      default_country_energy_data: {
                                      solar: {label: 'Switzerland',data: [mapHelpers.swiss_solar], population: mapHelpers.swiss_population},
                                      electric_car: {label: 'Switzerland',data: [mapHelpers.swiss_car], population: mapHelpers.swiss_population},
                                      heating: {label: 'Switzerland',data: [mapHelpers.swiss_heating], population: mapHelpers.swiss_population}
                                    },

      energyData_solar:  {
                              labels: [''],
                              country: {data:  [null], label: 'Switzerland', population: mapHelpers.swiss_population},
                              canton:  {data:  [null], label: 'canton', population: null},
                              commune: {data:  [null], label: 'commune', population: null}
                            },
      energyData_car:
                            {
                              labels: [''],
                              country: {data:  [null], label: 'Switzerland', population: mapHelpers.swiss_population},
                              canton:  {data:  [null], label: 'canton', population: null},
                              commune: {data:  [null], label: 'commune', population: null}
                            },
      energyData_heating:
                            {
                              labels: [''],
                              country: {data:  [null], label: 'Switzerland', population: mapHelpers.swiss_population},
                              canton:  {data:  [null], label: 'canton', population: null},
                              commune: {data:  [null], label: 'commune', population: null}
                            },
      energy_Data_heating_perc_contr: {
                                        labels: ['Swiss %', 'Canton %'],
                                        country: {data:  [null], label: 'Switzerland', population: mapHelpers.swiss_population},
                                        canton:  {data:  [null], label: 'canton', population: null},
                                        commune: {data:  [null], label: 'commune', population: null}
                                      },
      energyData_car_perc_contr: {
                                    labels: ['Swiss %', 'Canton %'],
                                    country: {data:  [null], label: 'Switzerland', population: mapHelpers.swiss_population},
                                    canton:  {data:  [null], label: 'canton', population: null},
                                    commune: {data:  [null], label: 'commune', population: null}
                                  },
      energyData_solar_perc_contr: {
                                      labels: ['Swiss %', 'Canton %'],
                                      country: {data:  [null], label: 'Switzerland', population: mapHelpers.swiss_population},
                                      canton:  {data:  [null], label: 'canton', population: null},
                                      commune: {data:  [null], label: 'commune', population: null}
                                    }
      }
  },
  created() {
  },

  methods:{

    /*
      Function that creates the map and defines all its possible interactions
    */
    createSvg(){

      /*
        Forces a zoo back to the center of the map
      */
      function force_zoom_to_center(){
        var x ,  y,  k
        //x corrdinate to move to
        x = zoom_translation_to_map_center.tx;
        //y corrdinate to move to
        y = zoom_translation_to_map_center.ty;
        //scaling factor (equivalent to zoom)
        k = zoom_translation_to_map_center.scale;
        svg.transition()
          .duration(750)
          .attr('transform', 'scale(' + k + ')' + 'translate(' + size.width / 2 + ',' + size.height / 2  +')translate(' + -x + ',' + -y + ')' );
      }

      /**
        zooms on the selected region
        * @param d region that we want to zoom on. d contains all of the region's info (boundaries and properties)
        * @param default_zoom_and_translation default area to zoom in case parameter d is null
        * @param canton_zoom true if we are zooming in on a canton
      */
      function zoom_to_region(d, default_zoom_and_translation,canton_zoom = true){
          var x, y, k;

          //get the bounding box of the region
          let [[min_x_coord,min_y_coord],[max_x_coord,max_y_coord]] = path.bounds(d)


          if (d) {
            // Compute centroid of the region
            var centroid = path.centroid(d);
            x = centroid[0];
            y = centroid[1];

            //determine scaling factor (zoom)
            var scale_x = size.width / Math.abs(max_x_coord - min_x_coord)
            var scale_y = size.height / Math.abs(max_y_coord - min_y_coord)
            k =  scale_x < scale_y ? scale_x : scale_y;
            k = k * 0.75

            if (canton_zoom){
              current_canton_info.zoom_info = {tx: x, ty:y, scale: k}
            }
            mapHelpers.openInfo(that,d.properties);
          } else {
            x = default_zoom_and_translation.tx;
            y = default_zoom_and_translation.ty;
            k = default_zoom_and_translation.scale;
            mapHelpers.closeInfo(that);
          }
          //translate and zoom to region
          svg.transition()
              .duration(750)
              .attr('transform',  'scale(' + k + ')'+'translate(' + size.width / 2 + ',' + size.height / 2  +')translate(' + -x + ',' + -y + ')' );

      }

      /**
        actions done when user clicks on a commune
        * @param d region that we want to zoom on. d contains all of the region's info (boundaries and properties)
      */
      function clickedCommune(e,d){

        //update data sent to bar plot to the data of the commune we clicked on
        mapHelpers.change_bar_plot_commune_data(that,mapHelpers.get_latest_energy_data(d.properties))

        //change color of the commune we selected and set all other commune to the default color
        svg.selectAll(".communes").filter(function(d2) {
                return this.style.fill.replace(/\s+/g, '') == mapHelpers.commune_selected_color.replace(/\s+/g, '') &&
                       d.properties != d2.properties
              })
              .style('fill', mapHelpers.commune_color);

        this.style.fill = mapHelpers.commune_selected_color
      }

      /**
        actions done when user clicks on a canton
        * @param d region that we want to zoom on. d contains all of the region's info (boundaries and properties)
      */
      function clickedCanton(e,d) {

        //check if a canton has already been selected
        if(! current_canton_info.canton_selected){
          //if canton has not already been selected

          //hide all communes
          svg.selectAll(".communes")
              .attr("hidden",true)
              .style('fill', mapHelpers.commune_color);

          //show all communes in the selected canton
          svg.selectAll(".communes").filter(function(d2) {
                return d.properties.canton_number === d2.properties.canton_number
              })
              .attr("hidden",null)

          //show all cantons
          svg.selectAll(".cantons")
              .attr("hidden",null)

          //hide the selected canton
          svg.selectAll(".cantons").filter(function(d2) {
                return d.properties.canton_number === d2.properties.canton_number
              })
              .attr("hidden",true)

          //update data sent to bar plot to the data of the canton we clicked on
          mapHelpers.change_bar_plot_canton_data(that,mapHelpers.get_latest_energy_data(d.properties))

          //specify that we have selected a canton
          current_canton_info.canton_selected = true

          //zoom on canton
          zoom_to_region(d,zoom_translation_to_map_center,true)

        }
        else{
          //if a canton was already selected

          //hide all communes
          svg.selectAll(".communes")
              .attr("hidden",true)

          //show all cantons
          svg.selectAll(".cantons")
              .attr("hidden",null)

          //zoom back to the center of the map
          force_zoom_to_center()

          //remove data previously selected canton and commune from bar chart
          mapHelpers.change_bar_plot_canton_data(that,null)
          mapHelpers.change_bar_plot_commune_data(that,null)
          current_canton_info.canton_selected = false
        }
      }

      /**
        actions done when user clicks on the box around the map of switzerland
      */
      function clickedBox(){
        //hide all the communes
        svg.selectAll(".communes")
              .attr("hidden",true)
        //show all cantons
        svg.selectAll(".cantons")
              .attr("hidden",null)
              .style('fill', mapHelpers.canton_color);
        //zoom back to the center of the map
        force_zoom_to_center()

        //remove data previously selected canton and commune from bar chart
        mapHelpers.change_bar_plot_canton_data(that,null)
        mapHelpers.change_bar_plot_commune_data(that,null)
        current_canton_info.canton_selected = false
      }

      //get bounding box of switzerland
      const [minX, minY, maxX, maxY] = bbox(this.cantons);

      // calculate aspect ratio and derive height of swiss map (width is defined in map_helpers.js)
      const height = ((maxY - minY) / (maxX - minX)) * mapHelpers.width;
      //rectangle around swiss map
      const rect_height = ((maxY - minY) / (maxX - minX)) * mapHelpers.rect_width;

      const delta_width = mapHelpers.rect_width - mapHelpers.width
      const delta_height = rect_height - height

      const size = {
        height: rect_height,
        width: mapHelpers.rect_width,
      };

      //change size of div
      document.getElementById('chart').style.width = mapHelpers.rect_width+"px";
      document.getElementById('chart').style.height = mapHelpers.rect_width+"px";
      document.getElementById('main-div').style.maxHeight = rect_height+"px";

      //functions used to project coordinates of data onto map
      const x = d3.scaleLinear()
          .range([delta_width/2, delta_width/2 + mapHelpers.width])
          .domain([minX, maxX]);

      const y = d3.scaleLinear()
          .range([delta_height/2,delta_height/2 + height])
          .domain([maxY, minY]);

      const projection = d3.geoTransform({
        point: function(px, py) {
          this.stream.point(x(px), y(py));
        },
      });

      const path = d3.geoPath().projection(projection);

      //info to zoom back to zoom back to map center
      let zoom_translation_to_map_center = {tx: mapHelpers.rect_width / 2,ty:  rect_height / 2,scale:  1}
      //contains the info of the canton that is currently selected
      let current_canton_info = {zoom_info: zoom_translation_to_map_center, canton_number: 0, canton_selected: false}

      //create svg
      const svg = d3.select("#chart").append("svg")
          .attr('width',mapHelpers.rect_width)
          .attr('height',rect_height);
      const that = this;

      //draw rectangle containing swiss map
      svg
        .append("rect")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", mapHelpers.rect_width)
        .attr("height", rect_height)
     . attr("fill", mapHelpers.rect_background_color)
        .on('click', clickedBox);

      //draw swiss canton and define interactions
      svg.append("g")
          .selectAll("path")
          .data(this.cantons.features)
          .enter()
          .append("path")
          .attr("class", "cantons")
          .style("fill", mapHelpers.canton_color)
          .attr("stroke-width", mapHelpers.canton_stroke_width)
          .attr("stroke", mapHelpers.canton_stroke)
          .attr("d", path)
          .attr("id", function(d, i) {  //attribute id to each canton
            return "canton" + d.properties.canton_number
          })
          .on("mouseover",function (e,d){
            // color when hovering canton
            this.style.fill =  mapHelpers.canton_color_mouse_on;
            mapHelpers.selectProvince(that,d.properties);
          })
          .on('mouseout', function () {
            mapHelpers.selectProvince(that,{name: ''});
            // Reset province color
            this.style.fill = mapHelpers.canton_color
          })
          .on('click', clickedCanton);

      //draw swiss communes and define interactions
      svg.append("g")
          .selectAll("path")
          .data(this.communes.features)
          .enter()
          .append("path")
          .attr("class", "communes")
          .style("fill", mapHelpers.commune_color)
          .attr("stroke-width", mapHelpers.commune_stroke_width)
          .attr("stroke", mapHelpers.commune_stroke)
          .attr("d", path)
          .attr("id", function(d, i) {
            return "communes" + d.properties.commune_number +"-" + d.properties.canton_number
          })
          .attr("hidden",true)
          .on("mouseover",function (e,d){
            //define color of commune we are hovering on
            if (this.style.fill.replace(/\s+/g, '') != mapHelpers.commune_selected_color.replace(/\s+/g, '') &&
                this.style.fill.replace(/\s+/g, '') != mapHelpers.commune_selected_color_mouse_on.replace(/\s+/g, ''))
              this.style.fill = mapHelpers.commune_color_mouse_on;
            else
              this.style.fill = mapHelpers.commune_selected_color_mouse_on
            mapHelpers.selectProvince(that,d.properties);
          })
          .on('mouseout', function () {
            mapHelpers.selectProvince(that,{name: ''});
            // Reset commune color
            if (this.style.fill.replace(/\s+/g, '') != mapHelpers.commune_selected_color.replace(/\s+/g, '') &&
                this.style.fill.replace(/\s+/g, '') != mapHelpers.commune_selected_color_mouse_on.replace(/\s+/g, ''))
              this.style.fill = mapHelpers.commune_color;

            else
              this.style.fill = mapHelpers.commune_selected_color

          })
          .on('click', clickedCommune);
    },
  },
  mounted(){
    this.energyData_solar.country = this.default_country_energy_data.solar
    this.energyData_heating.country = this.default_country_energy_data.heating
    this.energyData_car.country = this.default_country_energy_data.electric_car
    this.energy_Data_heating_perc_contr = mapHelpers.calculatePercentageContribution(this.energyData_heating)
    this.energyData_car_perc_contr = mapHelpers.calculatePercentageContribution(this.energyData_car)
    this.energyData_solar_perc_contr = mapHelpers.calculatePercentageContribution(this.energyData_solar)
    this.createSvg();
  }
}
</script>

<style scoped>
.map-div{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
  text-align: center;
  column-gap: 40px;
  margin-left: auto;
  margin-right: auto;
  overflow: hidden;

}
.center-screen {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  text-align: center;
  width: 1400px;
  height: 1000px;
  max-width: 2000px;

 /* or whatever width you want. */
  margin-left: auto;
  margin-right: auto;
  overflow: hidden;
}

.in-center{
  display: flex;
  justify-content: left;
  align-items: flex-start;
  width: 1400px;
  height: 30px;
 /* or whatever width you want. */
  margin-left: auto;
  margin-right: auto;

}


.province-info {
  margin-left: auto;
  order: 2;
  background: #F5F5F7;
  padding: 5px;
}
.list-region{
  display: inline;
  padding-left: 0px;
}

</style>
