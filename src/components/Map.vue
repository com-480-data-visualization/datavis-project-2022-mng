

<template>
  <div>
    <div class="center-screen" id="main-div">
      <div
          class="map-div"
          id='chart' >
      </div>
      <div v-if="currentProvince" class="province-info">
        <h3 class="text-center">{{currentProvince.state}}</h3>
        <ul>
          <li>Informations: {{province.name}}</li>
        </ul>
        <BarChart :dataEnergies="energyData_solar" :width=500 :height=170 ></BarChart>
        <BarChart :dataEnergies="energyData_heating" :width=500 :height=170></BarChart>
        <BarChart :dataEnergies="energyData_car" :width=500 :height=170></BarChart>
      </div>
    </div>
    <br><br>
    <div class="center-screen" style="width: 100%;margin: 0 auto;">
      <iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plotly.com/~ogim/81.embed" height="525" width="100%"></iframe>
    </div>
     <div class="center-screen" ></div>
  </div>
 <!-- <svg-map :map="Taiwan"></svg-map> -->
</template>

<script>

//import { SvgMap } from "vue-svg-map";
import Taiwan from "@svg-maps/taiwan";
import bbox from "@turf/bbox";
import * as d3 from 'd3'
import json from '../data/cantons.topo.json';
import json2 from '../data/communes.topo.json';
import Pie from "./Pie";
import BarChart from "./BarChart";
//import * as topojson from 'topojson-server';
import * as topojson from "topojson-client";
export default {
  name: "Map",
  components: {BarChart},
  data() {
    return {
      Taiwan,
      cantons: topojson.feature(json,json.objects.cantons),
      communes: topojson.feature(json2,json2.objects.communes),
      province: {name: 'Switzerland'},
      currentProvince: {name: 'Switzerland'},
      default_canton_energy_data : {
                                      data: null,
                                      label: 'canton'
                                    },
      default_commune_energy_data: {
                                      data: null,
                                      label: 'commune'
                                    },
      default_country_energy_data: {
                                      solar: {label: 'Switzerland',data: [0.054933]},
                                      electric_car: {label: 'Switzerland',data: [0.017949]},
                                      heating: {label: 'Switzerland',data: [0.326350]}
                                    },

      energyData_solar:  {
                              labels: ['Solar potential usage'],
                              country: {data: null, label: 'Switzerland'},
                              canton:  {data: null, label: 'canton'},
                              commune: {data: null, label: 'commune'}
                            },
      energyData_car:
                            {
                              labels: ['Electric car'],
                              country: {data: null, label: 'Switzerland'},
                              canton:  {data: null, label: 'canton'},
                              commune: {data: null, label: 'commune'}
                            },
      energyData_heating:
                            {
                              labels: ['Renewable heating'],
                              country: {data: null, label: 'Switzerland'},
                              canton:  {data: null, label: 'canton'},
                              commune: {data: null, label: 'commune'}
                            }

     
                  
      }
  },
  created() {
  },
  methods:{
    selectProvince(province) {
      this.province = province;
    },
    openInfo(province) {
      this.currentProvince = province;
    },
    closeInfo() {
      this.currentProvince = undefined;
    },
    not_valid_statistic(stat){
      return stat == 'null'
    },
    get_latest_energy_data(region){
      let electric_car_share_time_series = region.electric_car_share.split(' ')
      
      var el_car_share_most_recent = electric_car_share_time_series[electric_car_share_time_series.length -1]
     
      //check if it's a valid statistic
   
      if(this.not_valid_statistic(el_car_share_most_recent))
        el_car_share_most_recent = null

      let renewable_heating_share_time_series = region.renewable_heating_share.split(' ')
      var ren_heat_share_most_recent = renewable_heating_share_time_series[renewable_heating_share_time_series.length -1]
      //check if it's a valid statistic
      if(this.not_valid_statistic(ren_heat_share_most_recent))
        ren_heat_share_most_recent = null


      let solar_potential_usage_time_series = region.solar_potential_usage.split(' ')
      var sol_pot_usage_most_recent = solar_potential_usage_time_series[solar_potential_usage_time_series.length -1]
      //check if it's a valid statistic
      if(this.not_valid_statistic(sol_pot_usage_most_recent))
        sol_pot_usage_most_recent = null


      return {
              heating: {data: [ren_heat_share_most_recent],label: region.name},
              solar: {data: [sol_pot_usage_most_recent],label: region.name},
              electric_car: {data: [el_car_share_most_recent],label: region.name}
            }
    },

    change_bar_plot_canton_data(canton_data){

      //change canton data on bar plot (if nothing is stated set everythin to null)
      if (canton_data == null) {
        this.energyData_solar.canton = this.default_canton_energy_data
        this.energyData_heating.canton = this.default_canton_energy_data
        this.energyData_car.canton = this.default_canton_energy_data
      }
      else{
        this.energyData_solar.canton = canton_data.solar
        this.energyData_heating.canton = canton_data.heating
        this.energyData_car.canton = canton_data.electric_car
      }
      console.log(this.energyData_solar)
      console.log(this.energyData_heating)
      console.log(this.energyData_car)
    },

    change_bar_plot_commune_data(commune_data = null){

      if(commune_data == null){
        this.energyData_solar.commune = this.default_commune_energy_data
        this.energyData_heating.commune = this.default_commune_energy_data
        this.energyData_car.commune = this.default_commune_energy_data
      }
      else{
        this.energyData_solar.commune = commune_data.solar
        this.energyData_heating.commune = commune_data.heating
        this.energyData_car.commune = commune_data.electric_car
      }
    },

    createSvg(){
    
      const width=750
      const rect_width = 900
      const [minX, minY, maxX, maxY] = bbox(this.cantons);

      // calculate aspect ratio and derive height
      const height = ((maxY - minY) / (maxX - minX)) * width;
      const rect_height = ((maxY - minY) / (maxX - minX)) * rect_width;

      const delta_width = rect_width - width
      const delta_height = rect_height - height

      document.getElementById('chart').style.width = rect_width+"px";
      document.getElementById('chart').style.height = rect_width+"px";
      document.getElementById('main-div').style.maxHeight = rect_height+"px";
      const x = d3.scaleLinear()
          .range([delta_width/2, delta_width/2 + width])
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
      const canton_color = 'rgb(0,128,0)' //green !!!! colors must be in rgb and not just name of color (to compare colors)
      const commune_color = "rgb(255,165,0)" //orange !!!! colors must be in rgb and not just name of color (to compare colors)
      const commune_selected_color = "rgb(255,0,0)" //red !!!! colors must be in rgb and not just name of color (to compare colors)
      const canton_stroke = "rgb(0,0,0)"//black !!!! colors must be in rgb and not just name of color (to compare colors)
      const commune_stroke = "rgb(0,0,0)" //black !!!! colors must be in rgb and not just name of color (to compare colors)
      const canton_stroke_width = 1
      const commune_stroke_width = 1
      const canton_color_mouse_on = "rgb(144,238,144)" // !!!! colors must be in rgb and not just name of color (to compare colors)
      const commune_color_mouse_on = "rgb(255,204,153)" // !!!! colors must be in rgb and not just name of color (to compare colors)
      const commune_selected_color_mouse_on = "rgb(255,105,97)" // !!!! colors must be in rgb and not just name of color (to compare colors)

      const rect_background_color = "#042800"

     


      let zoom_translation_to_map_center = {tx: rect_width / 2,ty:  rect_height / 2,scale:  1}
      let current_canton_info = {zoom_info: zoom_translation_to_map_center, canton_number: 0, canton_selected: false}


      let centered = undefined;
      const size = {
        height: rect_height,
        width: rect_width,
      };


      const svg = d3.select("#chart").append("svg")
          .attr('width',rect_width)
          .attr('height',rect_height);
      const that = this;


      svg
        .append("rect")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", rect_width)
        .attr("height", rect_height)
        .attr("fill", rect_background_color)
        .on('click', clickedBox);

      svg.append("g")
          .selectAll("path")
          //.data(topojson2.feature(this.cantons,this.communes.objects.cantons).features)
          .data(this.cantons.features)
          .enter()
          .append("path")
          .attr("class", "cantons")
          .style("fill", canton_color)
          .attr("stroke-width", canton_stroke_width)
          .attr("stroke", canton_stroke)
          .attr("d", path)
          .attr("id", function(d, i) {
            return "canton" + d.properties.canton_number
          })
          .on("mouseover",function (e,d){
            // gives me the correct values
            this.style.fill =  canton_color_mouse_on;
            that.selectProvince(d.properties);
            //that.selectProvince(d.properties)
          })
          .on('mouseout', function () {
            that.selectProvince({name: 'Switzerland'});
            // Reset province color
            this.style.fill = canton_color
          })
          .on('click', clickedCanton);

      svg.append("g")
          .selectAll("path")
          //.data(topojson2.feature(this.communes,this.communes.objects.communes).features)
          .data(this.communes.features)
          .enter()
          .append("path")
          .attr("class", "communes")
          .style("fill", commune_color)
          .attr("stroke-width", commune_stroke_width)
          .attr("stroke", commune_stroke)
          .attr("d", path)
          .attr("id", function(d, i) {
            return "communes" + d.properties.commune_number +"-" + d.properties.canton_number
          })
          .attr("hidden",true)
          .on("mouseover",function (e,d){
            // gives me the correct values
            if (this.style.fill.replace(/\s+/g, '') != commune_selected_color.replace(/\s+/g, '') &&
                this.style.fill.replace(/\s+/g, '') != commune_selected_color_mouse_on.replace(/\s+/g, ''))
              this.style.fill = commune_color_mouse_on;
            else
              this.style.fill = commune_selected_color_mouse_on
            that.selectProvince(d.properties);
            //that.selectProvince(d.properties)
          })
          .on('mouseout', function () {
            that.selectProvince({name: 'Switzerland'});
            // Reset province color
            
          

            if (this.style.fill.replace(/\s+/g, '') != commune_selected_color.replace(/\s+/g, '') &&
                this.style.fill.replace(/\s+/g, '') != commune_selected_color_mouse_on.replace(/\s+/g, ''))
              this.style.fill = commune_color;
            
            else
              this.style.fill = commune_selected_color
            
          })
          .on('click', clickedCommune);


      function force_zoom_to_center(){
        var x ,  y,  k

        x = zoom_translation_to_map_center.tx;
        y = zoom_translation_to_map_center.ty;
        k = zoom_translation_to_map_center.scale;
        svg.transition()
          .duration(750)
          .attr('transform', 'scale(' + k + ')' + 'translate(' + size.width / 2 + ',' + size.height / 2  +')translate(' + -x + ',' + -y + ')' );
      }

      function zoom_to_region(d, default_zoom_and_translation,canton_zoom = true){
        var x, y, k;

        //let {max_x_coord,max_y_coord,min_x_coord,min_y_coord} = getBoundingBox(d)
        let [[min_x_coord,min_y_coord],[max_x_coord,max_y_coord]] = path.bounds(d)

        // Compute centroid of the selected path
        if (d && centered !== d) {
          var centroid = path.centroid(d);
          x = centroid[0];
          y = centroid[1];


          var scale_x = size.width / Math.abs(max_x_coord - min_x_coord)
          var scale_y = size.height / Math.abs(max_y_coord - min_y_coord)

          k =  scale_x < scale_y ? scale_x : scale_y;
          k = k - 0.5

          if (canton_zoom){
            current_canton_info.zoom_info = {tx: x, ty:y, scale: k}
          }
          centered = d;
          that.openInfo(d.properties);
        } else {
          x = default_zoom_and_translation.tx;
          y = default_zoom_and_translation.ty;
          k = default_zoom_and_translation.scale;
          centered = null;
          that.closeInfo();
        }

        svg.transition()
            .duration(750)
            .attr('transform',  'scale(' + k + ')'+'translate(' + size.width / 2 + ',' + size.height / 2  +')translate(' + -x + ',' + -y + ')' );

      }
      function clickedBox(){
        svg.selectAll(".communes")
              .attr("hidden",true)
        svg.selectAll(".cantons")
              .attr("hidden",null)
        force_zoom_to_center()
        that.change_bar_plot_canton_data(null)
        current_canton_info.canton_selected = false
      }
      function clickedCommune(e,d){
        that.change_bar_plot_commune_data(that.get_latest_energy_data(d.properties))
        

        svg.selectAll(".communes").filter(function(d2) {
                return this.style.fill.replace(/\s+/g, '') == commune_selected_color.replace(/\s+/g, '') &&
                       d.properties != d2.properties
              })
              .style('fill', commune_color);
     
        this.style.fill = commune_selected_color
       

        //zoom_to_region(d,current_canton_info.zoom_info, false)
      }

      function clickedCanton(e,d) {
        if(! current_canton_info.canton_selected){
          svg.selectAll(".communes")
              .attr("hidden",true)

          svg.selectAll(".communes").filter(function(d2) {
                return d.properties.canton_number === d2.properties.canton_number
              })
              .attr("hidden",null)

          svg.selectAll(".cantons")
              .attr("hidden",null)

          svg.selectAll(".cantons").filter(function(d2) {
                return d.properties.canton_number === d2.properties.canton_number
              })
              .attr("hidden",true)

          that.change_bar_plot_canton_data(that.get_latest_energy_data(d.properties))

          current_canton_info.canton_selected = true

          zoom_to_region(d,zoom_translation_to_map_center,true)
        }
        else{
          svg.selectAll(".communes")
              .attr("hidden",true)
          svg.selectAll(".cantons")
              .attr("hidden",null)
          force_zoom_to_center()
          that.change_bar_plot_canton_data(null)
          that.change_bar_plot_commune_data(null)
          current_canton_info.canton_selected = false
        }
      }

/*
// Get province name length
      function nameLength(d){
        const n = nameFn(d);
        return n ? n.length : 0;
      }

// Get province name
      function nameFn(d){
        return d && d.properties ? d.properties.name : null;
      }

// Get province color
      function fillFn(d){
        return color(nameLength(d));
      }
      */
    },
  },
  mounted(){
    this.energyData_solar.country = this.default_country_energy_data.solar 
    this.energyData_heating.country = this.default_country_energy_data.heating 
    this.energyData_car.country = this.default_country_energy_data.electric_car 
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
  max-width: 1000px; /* or whatever width you want. */
  max-height: 1000px; /* or whatever width you want. */
  margin-left: auto;
  margin-right: auto;
  overflow: hidden;
}
.center-screen {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  text-align: center;
  column-gap: 40px;
  width: 1400px;
  height: 1000px;
  max-width: 2000px;

 /* or whatever width you want. */
  margin-left: auto;
  margin-right: auto;
  overflow: hidden;
}

.province-info {
  margin-left: auto;
  order: 2;
  background: #F5F5F7;
  padding: 10px;
}
.pie-info{
  width: 450px;
}
</style>
