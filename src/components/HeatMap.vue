<template>
  <div class="heatmap-div" >
    <v-select style="width:400px;max-width: 400px; margin-bottom: 25px;" v-model="selected_option" :items="['Electric car','Solar potential','Renewable heating']" label="Indicator to compare"/>
  <div id="heatmap"/>
  </div>
</template>

<script>
import * as d3 from "d3";
import json from '../data/cantons.topo.json';
import * as topojson from "topojson-client";
import bbox from "@turf/bbox";
import legend from 'd3-svg-legend'
import { legendColor } from 'd3-svg-legend'


export default {
  name: "HeatMap",
  data(){
    return{
      cantons: topojson.feature(json,json.objects.cantons),
      selected_option: "Electric car"
    }
  },
  watch:{
    //Watch on the selected option form the user, in order to change heatmap depending on the indicator
    selected_option(){
      //remove it and change it
      d3.select("#heatmap").selectAll('*').remove()
      this.loadHeatmap(this.selected_option)
    }
  },
  methods:{
    /**
    create the according heatmap depending on the suistanability indicator
     * @param selected_option suistanability indicator
     */

    loadHeatmap(selected_option){
      const heatmap_width = 700
      const [minX, minY, maxX, maxY] = bbox(this.cantons);
      // calculate aspect ratio and derive height
      const height = ((maxY - minY) / (maxX - minX)) * heatmap_width;
      const x = d3.scaleLinear()
          .range([0, heatmap_width])
          .domain([minX, maxX]);
      const y = d3.scaleLinear()
          .range([0, height])
          .domain([maxY, minY]);

      const projection = d3.geoTransform({
        point: function(px, py) {
          this.stream.point(x(px), y(py));
        },
      });

      //crete svg
      const svg = d3.select("#heatmap").append("svg")
          .attr('width',heatmap_width)
          .attr('height',height);
      const that = this;

      const canton_stroke_width = 0.2
      const canton_stroke = "rgb(0,0,0)"
      const path = d3.geoPath().projection(projection);
      //select color scale
      var colorScale = d3.scaleSequential(d3.interpolateRdYlGn)

      //filter infos of the according indicator
      let el_cs = null
      if(selected_option === "Electric car"){
        el_cs = this.cantons.features.map(x => x.properties.electric_car_share.split(' '))
      }
      else if(selected_option === "Solar potential"){
        el_cs = this.cantons.features.map(x => x.properties.solar_potential_usage.split(' '))
      }
      //renewable energy
      else{
        el_cs = this.cantons.features.map(x => x.properties.renewable_heating_share.split(' '))
      }
      //min-max normalisation
      const values = el_cs.map(x => x[x.length -1])
      const min_val = Math.min.apply(Math, values)
      const max_val = Math.max.apply(Math, values)

      colorScale = colorScale.domain([min_val,max_val])

      //append data to csv
      svg.append("g")
          .selectAll("path")
          .data(this.cantons.features)
          .enter()
          .append("path")
          .attr("class", "cantons")
          .attr("stroke-width", canton_stroke_width)
          .attr("stroke", canton_stroke)
          .attr("d", path)
          .attr("fill", function (d) {
            //for each canton, get its suinstability indicator
            var energy_array = []
            if(selected_option === "Electric car"){
              energy_array = d.properties.electric_car_share.split(" ")
            }
            else if(selected_option  === "Solar potential"){
              energy_array = d.properties.solar_potential_usage.split(" ")
            }
            //renewable energy
            else{
              energy_array = d.properties.renewable_heating_share.split(" ")
            }
            //get the most recent value for the indicator
            var energy_recent_value = parseFloat(energy_array[energy_array.length - 1])
            return colorScale(energy_recent_value);
          })
      //append abbreviation of cantons as text in the middle of each canton
      svg.append("g")
          .selectAll("text")
          .data(this.cantons.features)
          .enter()
          .append("text")
          .attr("fill", "black")
          .attr("font-weight", 700)
          .attr("transform", function(d) {
            var centroid = path.centroid(d);
            return "translate(" + centroid[0] + "," + centroid[1] + ")"
          })
          .attr("text-anchor", "middle")
          .attr("dy", ".35em")
          .text(function(d) {
            return d.properties.abbreviation;
          });

      // append legend
      var g = svg.append("g")
          .attr("class", "legendThreshold")
          .attr("transform", "translate(20,70)");
      g.append("text")
          .attr("class", "caption")
          .attr("x", 0)
          .attr("y", -10)
          .text("%");
      var labels = ['Worst', 'na', 'na', 'na','Best'];
      var legend = legendColor()
          .labels(function (d) {
            //we only display the worst and best color
            if(labels[0] === labels[d.i] || labels[labels.length - 1] === labels[d.i]){
              return labels[d.i]
            }})
          .shapePadding(1)
          .scale(colorScale);
      svg.select(".legendThreshold")
          .style("font-size", "14px")
          .call(legend);
    }
  },
  //on mount of the component we want to load the default heatmap
  mounted(){
    this.loadHeatmap(this.selected_option);

  }
}
</script>

<style scoped>
.heatmap-div{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
  text-align: center;
  max-width: 1000px;
  max-height: 700px;
  margin-bottom: 100px;
  margin-left: auto;
  margin-right: auto;
  overflow: hidden;
}

</style>
