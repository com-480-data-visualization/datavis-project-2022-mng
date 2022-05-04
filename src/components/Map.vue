<template>
  <div>
  <h2 v-if="province" class="province-title">{{province.name}}</h2>
    <h2 v-if="currentProvince" class="province-title">{{currentProvince.name}}</h2>
    <div class="center-screen" id='chart' ></div>
  </div>
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
      communes: json2,
      province: undefined,
      currentProvince: undefined,
    };
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
    createSvg(){
    // get extent of switzerland as x, y coordinates

      var zoomed = false
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

      const color = d3.scaleLinear()
          .domain([1, 20])
          .clamp(true)
          .range(['#08304b', '#08304b']);
      let centered = undefined;
      const size = {
        height: height,
        width: width,
      };


      const svg = d3.select("#chart").append("svg")
          .attr('width',1000)
          .attr('height',1000);
      const that = this;

      svg.append("g")
          .selectAll("path")
          .data(this.geoJsonObj.features)
          .enter()
          .append("path")
          .attr("class", "feature")
          .style("fill", "steelblue")
          .attr("d", path)
          .on("mouseover",function (e,d){
            // gives me the correct values
            console.log(d.properties)
            d3.select(this).style('fill', '#1483ce');
            that.selectProvince(d.properties)
          })
          .on('mouseout', function () {
            that.selectProvince(undefined);
            // Reset province color
            svg.selectAll('path')
                .style('fill', (d) => {
                  console.log("ciao")
                  console.log(d)
                  console.log(centered)
                  return centered && d===centered ? '#D5708B' : fillFn(d);
                });
          })
          .on('click', clicked);
      function clicked(e,d) {
        var x, y, k;

        // Compute centroid of the selected path
        if (d && centered !== d) {
          //TODO: fix this
          var centroid = path.centroid(d);
          x = centroid[0];
          y = centroid[1];
          k = 4;
          centered = d;
          that.openInfo(d.properties);
        } else {
          x = size.width / 2;
          y = size.height / 2;
          k = 1;
          centered = null;
          that.closeInfo();
        }

        // Highlight the clicked province
        svg.append('g').selectAll('path')
            .style('fill', function(d){
              return centered && d===centered ? '#D5708B' : fillFn(d);
            });
        // Zoom
        //TODO: needs to be fixed
        if(!zoomed) {
          svg.transition()
              .duration(750)
              .attr('transform', 'translate(' + size.width / 2 + ',' + size.height / 2 + ')scale(' + k + ')translate(' + -x + ',' + -y + ')');

          zoomed = true
        }
        else{
          svg.transition()
              .duration(750)
              //undefined allows for faster zoomed out.
              .attr('transform',0)
          zoomed = false
        }

      }

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
