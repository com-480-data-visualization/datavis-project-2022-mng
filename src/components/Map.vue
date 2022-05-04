<template>
  <div>
  <h2 v-if="province" class="province-title">{{province.name}}</h2>
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
      province: 'non definito',
      currentProvince: 'non definito',
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
          .attr('width',width)
          .attr('height',height);
      const that = this;

     // const groupData = [this.geoJsonObj, this.communes];
      svg.append("g")
          .selectAll("path")
          .data(this.geoJsonObj.features)
          .enter()
          .append("path")
          .attr("class", "canton")
          .style("fill", "steelblue")
          .attr("d", path)
          .attr("id", function(d, i) {
            console.log(i)
            return "canton" + d.properties.canton_number
          })
          .on("mouseover",function (e,d){
            // gives me the correct values
            //console.log(d.properties)
            console.log(d.properties.canton_number)
            d3.select(this).style('fill', '#1483ce');
            that.selectProvince('non definito');
            //that.selectProvince(d.properties)
          })
          .on('mouseout', function () {
            that.selectProvince('non definito');
            // Reset province color
            svg.selectAll('path')
                .style('fill', (d) => {
                  //console.log("ciao")
                  //console.log(d)
                  //console.log(centered)
                  return centered && d===centered ? '#D5708B' : fillFn(d);
                });
          })
          .on('click', clicked);

      svg.append("g")
          .selectAll("path")
          .data(this.communes.features)
          .enter()
          .append("path")
          .attr("class", "communes")
          .style("fill", "red")
          .attr("d", path)
          .attr("id", function(d, i) {
            console.log(i)
            return "communes" + d.properties.commune_number +"-" + d.properties.canton_number
          })
      //.style("display","none")
      .attr("hidden",true)

      function getMaxCoordinatesFromBorders(d){
        const x_coord = 0
        const y_coord = 1
        var max_x_coord =  d.geometry.coordinates
                                .map((borders)=>
                                                  Math.max.apply(
                                                      Math,
                                                      borders
                                                        .map((border_coordinate) =>
                                                                Math.max.apply(
                                                                          Math,
                                                                          border_coordinate.map(coordinate => coordinate[x_coord])
                                                                )
                                                            )
                                                  )
                                      )
        var max_y_coord =  d.geometry.coordinates
                                .map((borders)=>
                                                  Math.max.apply(
                                                      Math,
                                                      borders
                                                        .map((border_coordinate) =>
                                                                Math.max.apply(
                                                                          Math,
                                                                          border_coordinate.map(coordinate => coordinate[y_coord])
                                                                )
                                                            )
                                                  )
                                      )
        return {max_x_coord,max_y_coord}
      }

      function getMinCoordinatesFromBorders(d){
        const x_coord = 0
        const y_coord = 1
        var min_x_coord =  d.geometry.coordinates
                                .map((borders)=>
                                                  Math.min.apply(
                                                      Math,
                                                      borders
                                                        .map((border_coordinate) =>
                                                              Math.min.apply(
                                                                        Math,
                                                                        border_coordinate.map(coordinate => coordinate[x_coord])
                                                              )
                                                            )
                                                    )
                                      )
        var min_y_coord =  d.geometry.coordinates
                                .map((borders)=>
                                                  Math.min.apply(
                                                      Math,
                                                      borders
                                                        .map((border_coordinate) =>
                                                                Math.min.apply(
                                                                          Math,
                                                                          border_coordinate.map(coordinate => coordinate[y_coord])
                                                                )
                                                            )
                                                  )
                                      )

        return {min_x_coord,min_y_coord}
      }

      function getBoundingBox(d){
        console.log('entered_bbox')

        let {max_x_coord,max_y_coord} = getMaxCoordinatesFromBorders(d)
        let {min_x_coord,min_y_coord} = getMinCoordinatesFromBorders(d)
        console.log('min_x_coord ' + min_x_coord)
        console.log('min_y_coord ' +  min_y_coord)
        console.log('max_x_coord ' + max_x_coord)
        console.log('max_y_coord ' +max_y_coord)

        console.log(minX)
        console.log(minY)
        console.log(maxX)
        console.log(maxY)

        max_x_coord = x(max_x_coord) // rescale coordinates
        max_y_coord = y(max_y_coord)// rescale coordinates
        min_x_coord = x(min_x_coord)// rescale coordinates
        min_y_coord = y(min_y_coord)// rescale coordinates

        console.log('min_x_coord ' + min_x_coord)
        console.log('min_y_coord ' +  min_y_coord)
        console.log('max_x_coord ' + max_x_coord)
        console.log('max_y_coord ' +max_y_coord)
        //var max_x = Math.max(d.geometry.coordinates.forEach((prop)=> Math.min(prop.map((x) => x.map(y => y[0])))));
        //var max_y = Math.max(d.geometry.coordinates.forEach((prop)=> Math.min(prop.map((x) => x.map(y => y[1])))));
        //var min_x = Math.min(d.geometry.coordinates.forEach((prop)=> Math.min(prop.map((x) => x.map(y => y[0])))));
        //var min_y = Math.min(d.geometry.coordinates.forEach((prop)=> Math.min(prop.map((x) => x.map(y => y[1])))));
        //console.log('max: ' + max_x + ',' + max_y)
        //console.log('min: ' + min_x + ',' + min_y)
        return {max_x_coord,max_y_coord,min_x_coord,min_y_coord}
      }


      function clicked(e,d) {
        svg.selectAll(".communes").filter(function(d2) {
              return d.properties.canton_number === d2.properties.canton_number
            })
            .attr("hidden",null)
            .style('fill', '#D5708B')

        this.style.display = "none";
          //or to hide the all svg
          //document.getElementById("mySvg").style.display = "none";
        var x, y, k;

        let {max_x_coord,max_y_coord,min_x_coord,min_y_coord} = getBoundingBox(d)

        console.log(bbox)
        // Compute centroid of the selected path
        if (d && centered !== d) {
          var centroid = path.centroid(d);
          x = centroid[0];
          y = centroid[1];
          console.log(Math.abs(max_x_coord - min_x_coord))
          console.log(Math.abs(max_y_coord - min_y_coord))
          var scale_x = Math.ceil(size.width / Math.abs(max_x_coord - min_x_coord))
          var scale_y = Math.ceil(size.height / Math.abs(max_y_coord - min_y_coord))

          k =  scale_x < scale_y ? scale_x : scale_y;

          centered = d;
          that.openInfo(d.properties);
        } else {
          x = size.width / 2;
          y = size.height / 2;
          k = 1;
          centered = null;
          that.closeInfo();
        }

        console.log('x: '+ x)
        console.log('y: '+ y)

        // Highlight the clicked province
        /*svg.append('g').selectAll('path')
            .data(that.communes.features)
            .enter()
            .append("path")
            .style('fill', function(d){
              return centered && d===centered ? '#D5708B' : fillFn(d);
            });*/
        // Zoom
        //TODO: needs to be fixed
        //if(!zoomed) {

        svg.transition()
            .duration(750)
            .attr('transform', 'scale(' + k + ')' + 'translate(' + size.width / 2 + ',' + size.height / 2  +')translate(' + -x + ',' + -y + ')' );

        zoomed = true
        console.log(zoomed)
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
