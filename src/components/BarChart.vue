<template>
  <apexchart ref="realtimeChart" type="bar" :width="width" :height="height" :options="chartOptions" :series="chartData"></apexchart>
</template>



<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  name: 'BarChart',
  components: {
    apexchart: VueApexCharts,
  },
  props:{
    'dataEnergies': Object,
    'width': {
      type: Number,
      default: 400
    },
    'height': {
      type: Number,
      default: 400
    },
    'title':{
      default: 'Title',
      type: String
    },
    'logarithmic':{
      default: false,
      type: Boolean
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Object,
      default: () => {}
    }
  },
  data(){
    return {
      //setup of series later needed for the barcharts
      series: [{
            name: this.dataEnergies.country.label,
            data: [this.dataEnergies.country.data === null ? null : this.dataEnergies.country.data[0]*100,
                                    this.dataEnergies.country.data === null ? null : this.dataEnergies.country.data[0]*100,
                                     null]
          }],
          chartOptions: {
            title:{
              text: this.title,
              align: 'center',
              style: {
                fontSize:  '10px',
                fontWeight:  'bold',
                fontFamily:  undefined,
                color:  '#263238'
              },
            },
            chart: {
              type: 'bar',
              toolbar:{
                show: false
              }
            },
            plotOptions: {
              bar: {
                horizontal: false,
                columnWidth: '55%',
                endingShape: 'rounded'
              },
            },
            legend: {
              fontSize: "10px"
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              show: true,
              width: 2,
              colors: ['transparent']
            },
            xaxis: {
              categories: this.dataEnergies.labels,
            },
            yaxis: {
              tickAmount: 3,
              title: {
                text: 'percentage (%)'
              },

              labels: {
                  formatter: function (value) {
                    return value.toFixed(1) + "%";
                  }
              },
              logarithmic: this.logarithmic
            },
            fill: {
              opacity: 1
            },
            tooltip: {
              y: {
                formatter: function (val) {
                  return val.toFixed(2) + " %"
                }
              }
            }
          }


        }
    },
  methods:{
    /**
     function which reformat data according to the injected data received as prop
     @param data suistanabiltiy indicator data
     */
    reformatData(data){
      return [{
                name: this.dataEnergies.country.label,
                data: this.dataEnergies.country.data.map(x => x == null ? null: x*100)
              },
              {
                name: this.dataEnergies.canton.label,
                data: this.dataEnergies.canton.data.map(x => x == null ?  null: x*100)
              },
              {
                name: this.dataEnergies.commune.label,
                data: this.dataEnergies.commune.data.map(x => x == null ? null: x*100)
              }]
    }
  },
  computed: {
    //listener on computed
    chartData(){
      return  this.reformatData(this.dataEnergies)
    }
  }
}

</script>

<style scoped>

</style>
