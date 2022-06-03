<template>
  <v-app id="app">
    <!--header-->
    <div class="header">
      <div class="topnav">
        <div class="topnav-right">
          <a href="#introduction" onmouseover="this.style.color='#3b6b3b';" onmouseout="this.style.color='grey'" style="font-weight:500;color:grey;text-transform: uppercase">Introduction</a>
          <a href="#map" onmouseover="this.style.color='#3b6b3b';" onmouseout="this.style.color='grey'" style="font-weight:500;color:grey;text-transform: uppercase">The map</a>
          <a href="#timeseries" onmouseover="this.style.color='#3b6b3b';" onmouseout="this.style.color='grey'" style="font-weight:500;color:grey;text-transform: uppercase">Timeseries</a>
          <a href="#heatmaps" onmouseover="this.style.color='#3b6b3b';" onmouseout="this.style.color='grey'" style="font-weight:500;color:grey;text-transform: uppercase">Heatmap</a>
        </div>
      </div>
    </div> <!--finished header-->
    <Introduction/>
    <Map/>
    <div id="timeseries" style="margin-right: auto; margin-left: auto; padding: 80px 15px 75px; max-width: 850px;">
      <h2>Timeseries data</h2><br>
      Here you can explore how different cantons' 3 different metrics have evolved over time. Just select the cantons that interest you!
    </div>
    <TimeSeries  :data-energies="energyData_car" type="Electric car share"/>
    <TimeSeries :data-energies="energyData_solar" type="Solar panel share"/>
    <TimeSeries :data-energies="energyData_heating" type="Renewable heating usage"/>

    <div id="heatmaps" style="word-wrap: break-word;margin-right: auto; margin-left: auto; padding: 10px 15px 75px; max-width: 850px">
      <h2>Heatmap</h2><br>
      Summarizing all the above data is the map below! Clearly we can see Geneva is doing terribly at using renewable heating. Hopefully, they can improve. If you're from Geneva maybe have a chat new time you see the mayor &#128540;.
    </div>
    <HeatMap/>
    <div style="word-wrap: break-word;margin-right: auto; margin-left: auto; padding: 0px 15px 75px; max-width: 850px">
      We hope this website has given you a better understanding of how Switzerland is doing at sustainability and hope it will encourage you to contribute to Switzerland's sustainability!
    </div>
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
            <div style="text-align: left">Nicolas Baldwin<v-btn class="white--text" icon href="https://www.linkedin.com/in/nicolas-baldwin-75832017b/"><v-icon size="24px">{{linkedin}}</v-icon></v-btn>
              <v-btn class="white--text" icon href="https://github.com/chabala98"><v-icon size="24px">mdi-github</v-icon></v-btn>
              <br></div>
            <div style="text-align: left">Gioele Monopoli<v-btn class="white--text" icon href="https://www.linkedin.com/in/gioele-monopoli"><v-icon size="24px">{{linkedin}}</v-icon></v-btn>
              <v-btn class="white--text" icon href="https://github.com/ogimgio"><v-icon size="24px">mdi-github</v-icon></v-btn>
              <br></div>
            <div style="text-align: left">Michael Roust<v-btn class="white--text" icon href="https://www.linkedin.com/in/michaelroust"><v-icon size="24px">{{linkedin}}</v-icon></v-btn>
              <v-btn class="white--text" icon href="https://github.com/michaelroust"><v-icon size="24px">mdi-github</v-icon></v-btn>
              <br></div>
          </div>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>Data visualization - EPFL</strong><v-btn class="white--text" icon href="https://github.com/com-480-data-visualization/datavis-project-2022-mng"><v-icon size="24px">mdi-github</v-icon></v-btn>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
import Introduction from './components/Introduction.vue'
import Map from "./components/Map.vue";
import HeatMap from "./components/HeatMap";
import TimeSeries from "./components/TimeSeries";
import json from './data/cantons.topo.json';
import * as topojson from "topojson-client";

export default {
  name: 'App',
  components: {
    TimeSeries,
    HeatMap,
    Introduction,Map
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
    //prepare data to be injected in TimeSeries
    this.energyData_car = this.createData("electric_car_share")
    this.energyData_solar = this.createData("solar_potential_usage")
    this.energyData_heating = this.createData("renewable_heating_share")
  },
  methods:{
    /**
     creates the data for a given metric (later used in Timeseries)
     * @param which_energy suistanability indicator
     * @return array with info of indicator
     */
    createData(which_energy){
      var arr_to_pass = []
      this.timeSeriesValues.features.forEach((item) =>
      {
        return arr_to_pass.push({'name':item.properties.name,
          'data': item.properties[which_energy].split(" ").map(x=>(parseFloat(x)*100).toFixed(2)),'timeline': item.properties["energyreporter_date"].split(" ")})
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
.header {
  position: fixed;
  top: 0;
  z-index: 1;
  width: 100%;
}
.topnav {
  overflow: hidden;
  background-color: white;
  box-shadow: 0 2px 4px 0 #3b6b3b;
}
/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}
/* Right-aligned section inside the top navigation */
.topnav-right {
  float: right;
}
ul {
  margin: 0;
}
</style>
