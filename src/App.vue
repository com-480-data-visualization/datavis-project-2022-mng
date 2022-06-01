<template>
  <v-app id="app">
    <HelloWorld/>
    <Map/>
    <TimeSeries :data-energies="energyData_car" type="Electric car share"/>
    <TimeSeries :data-energies="energyData_solar" type="Solar panel share"/>
    <TimeSeries :data-energies="energyData_heating" type="Renewable heating usage"/>
    <HeatMap/>
    <v-footer
        dark
        padless
    >
      <v-card
          flat
          tile
          class=" lighten-1 white--text text-center flex justify-center"
          style="min-width: 100%; background-color: #3b6b3b"
      >
        <v-card-text>
        </v-card-text>

        <v-card-text class="white--text pt-0" style="text-align: center">
          <div style="display: inline-block;">
            <div style="font-style: italic;">Authors:<br></div>
            <div style="text-align: left">Michael Roust<v-btn class="white--text" icon href="https://www.linkedin.com/in/michaelroust"><v-icon size="24px">{{linkedin}}</v-icon></v-btn>
              <v-btn class="white--text" icon href="https://github.com/michaelroust"><v-icon size="24px">mdi-github</v-icon></v-btn>
              <br></div>
            <div style="text-align: left">Nicolas Baldwin<v-btn class="white--text" icon href="https://www.linkedin.com/in/nicolas-baldwin-75832017b/"><v-icon size="24px">{{linkedin}}</v-icon></v-btn>
              <v-btn class="white--text" icon href="https://github.com/chabala98"><v-icon size="24px">mdi-github</v-icon></v-btn>
              <br></div>
            <div style="text-align: left">Gioele Monopoli<v-btn class="white--text" icon href="https://www.linkedin.com/in/gioele-monopoli"><v-icon size="24px">{{linkedin}}</v-icon></v-btn>
              <v-btn class="white--text" icon href="https://github.com/ogimgio"><v-icon size="24px">mdi-github</v-icon></v-btn>
              <br></div>
          </div>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>Data visualization - EPFL</strong><v-btn class="white--text" icon href="https://github.com/epfl-ada/ada-2021-project-mmng"><v-icon size="24px">mdi-github</v-icon></v-btn>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Map from "./components/Map.vue";
import HeatMap from "./components/HeatMap";
import TimeSeries from "./components/TimeSeries";
import json from './data/cantons.topo.json';
import * as topojson from "topojson-client";
//import * as d3 from 'd3'

export default {
  name: 'App',
  components: {
    TimeSeries,
    HeatMap,
    HelloWorld,Map
  },
  data(){
    return{
      linkedin: 'mdi-linkedin',
      timeSeriesValues: topojson.feature(json,json.objects.cantons),
      energyData_solar: null,
      energyData_heating: null,
      energyData_car: null
    }
  },
  created() {
    this.energyData_car = this.createData("electric_car_share")
    this.energyData_solar = this.createData("solar_potential_usage")
    this.energyData_heating = this.createData("renewable_heating_share")
  },
  methods:{
    createData(which_energy){
      var arr_to_pass = []
      this.timeSeriesValues.features.forEach((item) =>
      {
        return arr_to_pass.push({'name':item.properties.name,
          'data': item.properties[which_energy].split(" ").map(parseFloat),'timeline': item.properties["energyreporter_date"].split(" ")})
      })

      return arr_to_pass
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #31502c;
  font-size: 1.25rem;
}
</style>
