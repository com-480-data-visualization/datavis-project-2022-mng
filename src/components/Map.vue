

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
        <h4 class="text-center">Electricity Car share</h4>
        <Pie class="pie-info"/>
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
import json from '../data/cantons.json';
import json2 from '../data/communes.json';
import Pie from "./Pie";
export default {
  name: "Map",
  components: {
    Pie
  },
  data() {
    return {
      Taiwan,
      geoJsonObj: json,
      communes: json2,
      province: {name: 'Switzerland'},
      currentProvince: {name: 'Switzerland'},
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


      const width=750
      const rect_width = 900
      const [minX, minY, maxX, maxY] = bbox(this.geoJsonObj);

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
      const canton_color = "green" //previously was steelblue
      const commune_color = "orange" //previously was steelblue
      const canton_stroke = "black"
      const commune_stroke = "black"
      const canton_stroke_width = 1
      const commune_stroke_width = 1
      const canton_color_mouse_on = "lightgreen" // previously was: #1483ce
      const commune_color_mouse_on = "#ffc87c" // previously was: #1483ce

      const rect_background_color = "#042800"




      let zoom_translation_to_map_center = {tx: rect_width / 2,ty:  rect_height / 2,scale:  1}
      let current_canton_info = {zoom_info: zoom_translation_to_map_center, canton_number: 0, canton_selected: false}




     // const color = d3.scaleLinear()
       //   .domain([1, 20])
         // .clamp(true)
          //.range(['green', 'lightgreen']);
          //.range(['#08304b', '#08304b']);
      let centered = undefined;
      const size = {
        height: rect_height,
        width: rect_width,
      };


      const svg = d3.select("#chart").append("svg")
          .attr('width',rect_width)
          .attr('height',rect_height);
      const that = this;

     // const groupData = [this.geoJsonObj, this.communes];
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
          .data(this.geoJsonObj.features)
          .enter()
          .append("path")
          .attr("class", "cantons")
          .style("fill", canton_color)
          .attr("stroke-width", canton_stroke_width)
          .attr("stroke", canton_stroke)
          .attr("d", path)
          .attr("id", function(d, i) {
            console.log(i)
            return "canton" + d.properties.canton_number
          })
          .on("mouseover",function (e,d){
            // gives me the correct values
            //console.log(d.properties)
            console.log(d.properties.canton_number)
            this.style.fill =  canton_color_mouse_on;
            that.selectProvince(d.properties);
            //that.selectProvince(d.properties)
          })
          .on('mouseout', function () {
            that.selectProvince({name: 'Switzerland'});
            // Reset province color
            this.style.fill = canton_color
            /*
            //svg.selectAll('path')
              //  .style('fill', 'green' /*(d) => {
                  return centered && d===centered ? canton_color : fillFn(d);

                });*/
          })
          .on('click', clickedCanton);

      svg.append("g")
          .selectAll("path")
          .data(this.communes.features)
          .enter()
          .append("path")
          .attr("class", "communes")
          .style("fill", commune_color)
          .attr("stroke-width", commune_stroke_width)
          .attr("stroke", commune_stroke)
          .attr("d", path)
          .attr("id", function(d, i) {
            console.log(i)
            return "communes" + d.properties.commune_number +"-" + d.properties.canton_number
          })
          .attr("hidden",true)
          .on("mouseover",function (e,d){
            // gives me the correct values
            //console.log(d.properties)
            console.log(d.properties.canton_number)
            this.style.fill = commune_color_mouse_on;
            that.selectProvince(d.properties);
            //that.selectProvince(d.properties)
          })
          .on('mouseout', function () {
            that.selectProvince({name: 'Switzerland'});
            // Reset province color
            this.style.fill = commune_color;
            /*
           // svg.selectAll('path')
             //   .style('fill', commune_color /*(d) => {
                  return centered && d===centered ? canton_color : fillFn(d);

                });*/
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


      function clickedBox(e,d){
        console.log(d)
        svg.selectAll(".communes")
              .attr("hidden",true)
        svg.selectAll(".cantons")
              .attr("hidden",null)
        force_zoom_to_center()
        current_canton_info.canton_selected = false
      }
      function clickedCommune(e,d){
        zoom_to_region(d,current_canton_info.zoom_info, false)
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


          //this.style.display = "none";
          current_canton_info.canton_selected = true

          zoom_to_region(d,zoom_translation_to_map_center,true)
        }
        else{
          svg.selectAll(".communes")
              .attr("hidden",true)
          svg.selectAll(".cantons")
              .attr("hidden",null)
          force_zoom_to_center()
          current_canton_info.canton_selected = false
        }

          //or to hide the all svg
          //document.getElementById("mySvg").style.display = "none";



        //}
        /*
        else{
          svg.transition()
              .duration(750)
              //undefined allows for faster zoomed out.
              .attr('transform',undefined)
          zoomed = false
        }
*/
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
