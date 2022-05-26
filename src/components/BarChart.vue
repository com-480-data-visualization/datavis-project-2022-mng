<!-- <template>
  <Bar
      :chart-options="chartOptions"
      :chart-data="chartData"
      :chart-id="chartId"
      :dataset-id-key="datasetIdKey"
      :plugins="plugins"
      :css-classes="cssClasses"
      :styles="styles"
      :width="width"
      :height="height"
  />
</template> -->
<template>
  <Bar :chart-data="chartData" :chart-options="chartOptions" />
</template>



<script>
import { Bar } from 'vue-chartjs/legacy'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
export default {
  name: 'BarChart',
  components: {Bar},
  props:{
    'dataEnergies': Object
  },
  computed: {
    chartData() {
      return {
              labels: [ 'Renewable heating', 'Electric car', 'Solar potential usage' ],
              datasets: [ 
                            { data: this.dataEnergies.country.data,
                              backgroundColor: '#7272FE',
                              label: this.dataEnergies.country.label
                            },
                            { data: this.dataEnergies.canton.data,
                              backgroundColor: '#98fb98',
                              label: this.dataEnergies.canton.label
                            },
                            { data: this.dataEnergies.commune.data,
                              backgroundColor: '#fd5e53',
                              label: this.dataEnergies.commune.label
                            }
                         ]
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

</style>
