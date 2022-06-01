<template>
  <div class="center-screen">
    <v-col>
    <apexchart ref="realtimeChart" type="line" :height="height" :width="width" :options="chartOptions" :series="series"></apexchart>
    </v-col>
    <v-col>
    <v-row>
    <v-btn @click="hideAllSeries" block>Show all</v-btn>
    <v-btn @click="showMainSeries" block>One per region</v-btn>
    </v-row>
    </v-col>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  name: 'TimeSeries',
  components:{
    apexchart: VueApexCharts
  },
  props:{
    'dataEnergies': Array,
    'type': String,
    'width': {
      type: Number,
      default: 750
    },
    height: {
      type: Number,
      default: 400
    },
  },
  data(){
    return{
      clicked: false,
      name_cantons: this.dataEnergies.map((x) => x.name).sort(),
      time_series_values: null,
      series: this.dataEnergies,
        colors: ['#775DD0', '#546E7A', '#26a69a', '#D10CE8'],
      chartOptions: {
        chart: {
          height: 350,
          type: 'line',
          zoom: {
            enabled: false
          },
          toolbar:{
            show:false
          },
          animations: {
            enabled: false,
          },
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight',
          width:0.5,
        },
        title: {
          text: this.type,
          align: 'left'
        },
        grid: {
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.5
          },
        },
        xaxis: {
          categories: this.dataEnergies[0].timeline,
        }
      },
    }
  },
  mounted () {
    const initial_cantons = ["Ticino","Zurich","Vaud"]
    let to_keep = this.dataEnergies.filter(item => !(initial_cantons.includes(item.name))).map(x=>x.name)
    to_keep.forEach((x) => this.$refs.realtimeChart.hideSeries(x))
  },
  methods:{
    updateSeriesLine(cantons_selected) {
      var arr_1 = []
      function myFunction(item) {
        return arr_1.push({'name': item,"data" : Array.from({length: 8}, () => Math.floor(Math.random() * 100))})
      }
      //cantons_selected.forEach(myFunction)
      //this.$refs.realtimeChart.updateSeries(arr_1, false, true);
      this.$refs.realtimeChart.hideSeries(cantons_selected)
    },
    hideAllSeries(){
      const initial_cantons = ["Ticino","Zurich","Vaud"]
      let to_keep = this.dataEnergies.map(x=>x.name)
      to_keep.forEach(x=>this.$refs.realtimeChart.showSeries(x))
    },
    showMainSeries(){
      const initial_cantons = ["Ticino","Zurich","Vaud"]
      let to_keep = this.dataEnergies.filter(item => !(initial_cantons.includes(item.name))).map(x=>x.name)
      to_keep.forEach((x) => this.$refs.realtimeChart.hideSeries(x))
    }
  }
}
</script>

<style scoped>
.center-screen {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  text-align: center;
  width: 1000px;
  height: 500px;

  /* or whatever width you want. */
  margin-left: auto;
  margin-right: auto;
  overflow: hidden;
}

</style>

