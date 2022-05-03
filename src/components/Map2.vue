<template>
  <div class="map-wrapper">
    <h2 v-if="province" class="province-title">{{province.state}}</h2>
    <div v-if="currentProvince" class="province-info">
      <h3 class="text-center">{{currentProvince.state}}</h3>
      <ul>
        <li>cartodb_id: {{currentProvince.cartodb_id}}</li>
        <li>slug: {{currentProvince.slug}}</li>
      </ul>
    </div>
    <svg id="Graph svg"></svg>
  </div>
</template>

<script>
import * as d3 from 'd3'
import bbox from "@turf/bbox";
import json from '../data/cantons.json';
export default {
  name: "Map2",
  data() {
    return {
      province: undefined,
      currentProvince: undefined,
      geoJsonObj: json,
    }
  },
  methods: {
    selectProvince(province) {
      this.province = province;
    },
    openInfo(province) {
      this.currentProvince = province;
    },
    closeInfo() {
      this.currentProvince = undefined;
    },
  },
  created() {
    // Set svg width & height
    let centered = undefined;
    const size = {
      height: 700,
      width: 700,
    };
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

    const color = d3.scaleLinear()
        .domain([1, 20])
        .clamp(true)
        .range(['#08304b', '#08304b']);

    const projection = d3.geoTransform({
      point: function(px, py) {
        this.stream.point(x(px), y(py));
      },
    });

    const path = d3.geoPath().projection(projection);

    const svg = d3.select("#Graph svg").append("svg")
        .attr('width', size.width)
        .attr('height', size.height);

// Add background
    svg.append('rect')
        .attr('class', 'background')
        .attr('width', size.width)
        .attr('height', size.height)
        .on('click', clicked);


// Load map data
      var features = this.geoJsonObj.features;

      // Update color scale domain based on data
      color.domain([0, d3.max(features, nameLength)]);

      // Draw each province as a path
    svg.append('g').selectAll('path')
          .data(features)
          .enter().append('path')
          .attr('d', path)
          .attr('vector-effect', 'non-scaling-stroke')
          .style('fill', fillFn)
          .on('mouseover', mouseover)
          .on('mouseout', mouseout)
          .on('click', clicked);

function clicked(d) {
  var x, y, k;

  // Compute centroid of the selected path
  if (d && centered !== d) {
    var centroid = path.centroid(d);
    x = centroid[0];
    y = centroid[1];
    k = 4;
    centered = d;
    this.openInfo(d.properties);
  } else {
    x = size.width / 2;
    y = size.height / 2;
    k = 1;
    centered = null;
    this.closeInfo();
  }

  // Highlight the clicked province
  svg.append('g').selectAll('path')
      .style('fill', function(d){
        return centered && d===centered ? '#D5708B' : fillFn(d);
      });

  // Zoom
  svg.append('g').transition()
      .duration(750)
      .attr('transform', 'translate(' + size.width / 2 + ',' + size.height / 2 + ')scale(' + k + ')translate(' + -x + ',' + -y + ')');
}

function mouseover(d){
  // Highlight hovered province
  d3.select(this).style('fill', '#1483ce');
  if(d) {
    this.selectProvince(d.properties);
  }
}

function mouseout(){
  this.selectProvince(undefined);
  // Reset province color
  svg.append('g').selectAll('path')
      .style('fill', (d) => {
        return centered && d===centered ? '#D5708B' : fillFn(d);
      });
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
}
}
</script>

<style>
.map-wrapper .province-title {
  position: absolute;
  top: 50px;
  left: 150px;
  color: white;
}
.map-wrapper .province-info {
  background: white;
  position: absolute;
  top: 150px;
  right: 20px;
  height: 400px;
  width: 300px;
}
.map-wrapper .background {
  fill: #021019;
  pointer-events: all;
}
.map-wrapper .map-layer {
  fill: #08304b;
  stroke: #021019;
  stroke-width: 1px;
}
</style>
