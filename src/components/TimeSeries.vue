<template>
  <div class="center-screen">
    <v-col>
    <apexchart ref="realtimeChart" type="line" :height="height" :width="width" :options="chartOptions" :series="series"></apexchart>
    </v-col>
    <v-col style="margin-top: 60px">
      <v-row>
        <v-btn @click="showAllSeries" block small>Show all</v-btn>
        <v-btn @click="showMainSeries" block small>One per region</v-btn>
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
        },
        dataLabels: {
          enabled: false
        },
        colors: ["#FED842",'#FC6835','#FFED7D','#30FF40',
          "#38FFE9", "#4C72FF","#B24DFF","#ACFF83",
          "#25D3FF", "#FB001A","#5141FF",'#5000FF',
          '#FC6F37', '#28FF80','#0800FF',"#BEE7FF",
          "#FEFF0B",'#F44336', '#E91E63', '#9C27B0',
          "#0F750E","#247072","#713D33","#726D30",
          "#FDA9FE","#65FF07"], //allowing multiple colors
        stroke: {
          curve: 'straight',
          width:0.8,
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
        },
        yaxis:{
          title: {
            text: '%',
            offsetX: 0,
            offsetY: 0,
            style: {
              color: undefined,
              fontSize: '12px',
              fontFamily: 'Helvetica, Arial, sans-serif',
              fontWeight: 600,
              cssClass: 'apexcharts-xaxis-title',
            },
          },
        }
      },
    }
  },
  //on mounted, we want to keep only the timeseries for each region
  mounted () {
    const initial_cantons = ["Ticino","Zurich","Vaud"]
    let to_keep = this.dataEnergies.filter(item => !(initial_cantons.includes(item.name))).map(x=>x.name)
    to_keep.forEach((x) => this.$refs.realtimeChart.hideSeries(x))
  },
  methods:{
    /**
     Function that shows all the time series for each canton
     */
    showAllSeries(){
      console.log("boh")
      let to_keep = this.dataEnergies.map(x=>x.name)
      to_keep.forEach(x=>this.$refs.realtimeChart.showSeries(x))
    },
    /**
     Function that hides all the series apart from one for each region (italian, german, french)
     */
    showMainSeries(){
      const initial_cantons = ["Ticino","Zurich","Vaud"]
      let to_keep = this.dataEnergies.filter(item => !(initial_cantons.includes(item.name))).map(x=>x.name)
      to_keep.forEach((x) => this.$refs.realtimeChart.hideSeries(x))
    },
  },
}
</script>

<style scoped>
.center-screen {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
  text-align: center;
  max-width: 1000px;
  height: 500px;
  margin-left: auto;
  margin-right: auto;
  overflow: hidden;
}

</style>

