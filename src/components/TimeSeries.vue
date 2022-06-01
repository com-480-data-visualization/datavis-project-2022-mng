<template>
  <div class="center-screen">
    <Line :chart-data="chartData" :chart-options="chartOptions" :width="width" :height="height" />
  </div>
</template>

<script>
import { Line } from 'vue-chartjs/legacy'
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale)
// this.chartData is created in the mixin.
// If you want to pass options please create a local options object


export default {
  name: 'TimeSeries',
  components:{
    Line
  },
  props:{
    'dataEnergies': Object,
    'width': {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    },
  },
  computed: {
    chartData() {
      return {
        labels: ["2021-03-31","2021-04-31","2021-05-31","2021-06-31"],
        datasets: [{
          label: 'My First Dataset',
          data: [65, 59, 80, 81],
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          //tension: 0.1
        }]
      }
      },
    chartOptions() {
      return {
        chartOptions: {responsive: true}
      }
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
  column-gap: 40px;
  width: 1400px;
  height: 1000px;
  max-width: 2000px;

  /* or whatever width you want. */
  margin-left: auto;
  margin-right: auto;
  overflow: hidden;
}

</style>

