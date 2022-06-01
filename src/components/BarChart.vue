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
  <Bar :chart-data="chartData" :chart-options="chartOptions" :width="width" :height="height" />
</template>



<script>
import { Bar } from 'vue-chartjs/legacy'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
export default {
  name: 'BarChart',
  components: {Bar},
  props:{
    'dataEnergies': Object,
    'width': {
      type: Number,
      default: 400
    },
    'height': {
      type: Number,
      default: 400
    }
  },
  computed: {
    chartData() {
      return {
              labels:  this.dataEnergies.labels ,
              datasets: [ 
                            { data: [this.dataEnergies.country.data === null ? null : this.dataEnergies.country.data[0]*100,
                                    this.dataEnergies.country.data === null ? null : this.dataEnergies.country.data[0]*100,
                                     null],
                              backgroundColor: '#7272FE',
                              label: this.dataEnergies.country.label
                            },
                            { data: [(this.dataEnergies.canton.data === null ?
                                        null :
                                        this.dataEnergies.canton.data[0]*100),
                                     (this.dataEnergies.canton.data === null  ?
                                        null :
                                        this.dataEnergies.canton.data[0]*this.dataEnergies.canton.population/this.dataEnergies.country.population*100),
                                     (this.dataEnergies.canton.data === null ? null : this.dataEnergies.canton.data[0]*100)],
                              backgroundColor: '#98fb98',
                              label: this.dataEnergies.canton.label
                            },
                            { data: [ (this.dataEnergies.commune.data === null ? 
                                        null :
                                        this.dataEnergies.commune.data[0]*100),
                                      null,
                                      (this.dataEnergies.commune.data === null && this.dataEnergies.commune.population === null?
                                        null :
                                        this.dataEnergies.commune.data[0] * this.dataEnergies.commune.population/this.dataEnergies.canton.population)*100],
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
