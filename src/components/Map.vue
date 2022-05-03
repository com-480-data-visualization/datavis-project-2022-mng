<template>
    <div class="center-screen" id='chart' ></div>
 <!-- <svg-map :map="Taiwan"></svg-map> -->
</template>

<script>
//import { SvgMap } from "vue-svg-map";
import Taiwan from "@svg-maps/taiwan";
import bbox from "@turf/bbox";
import * as d3 from 'd3'
import json from '../data/cantons.json';
import json2 from '../data/communes.json';
export default {
  name: "Map",
  components: {
    //SvgMap
  },
  data() {
    return {
      Taiwan,
      geoJsonObj: json,
      communes: json2
    };
  },
  created() {
  },
  methods:{
    createSvg(){
    // get extent of switzerland as x, y coordinates
      const width=1000
      const [minX, minY, maxX, maxY] = bbox(this.geoJsonObj);

      // calculate aspect ratio and derive height
      const height = ((maxY - minY) / (maxX - minX)) * width;

      const x = d3.scaleLinear()
          .range([0, width])
          .domain([minX, maxX]);

      const y = d3.scaleLinear()
          .range([0, height])
          .domain([maxY, minY]);
      const projection = d3.geoTransform({
        point: function(px, py) {
          this.stream.point(x(px), y(py));
        },
      });
      const path = d3.geoPath().projection(projection);


      var svg = d3.select("#chart").append("svg")
          .attr('width',1000)
          .attr('height',1000);

      svg.append("g")
          .selectAll("path")
          .data(this.geoJsonObj.features)
          .enter()
          .append("path")
          .attr("class", "feature")
          .style("fill", "steelblue")
          //definisce la forma
          .attr("d", path);
    },
  },
  mounted(){
    this.createSvg();
  }
}
</script>

<style scoped>
.center-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: 100vh;
}
</style>
