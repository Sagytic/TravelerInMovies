<script>
import {Radar} from 'vue-chartjs'
// import {mapState} from 'vuex'
export default {
  extends: Radar,
  props: {
    dataset: Object
  },
  data () {
    return {
      dataCollection: {
        labels: Object.keys(this.dataset),
        datasets: [
          {
              label: 'Numbers',
              data: Object.values(this.dataset),
              fill: true,
              backgroundColor: "rgba(54, 162, 235, 0.2)",
              borderColor: "rgb(54, 162, 235)",
              // backgroundColor: 'blue', //'#f87979',
              pointBackgroundColor: 'white',
              // borderColor: "rgb(54, 162, 235)",
              // fillColor: "rgba(102,45,145,.1)",
              // strokeColor: "rgba(102,45,145,1)",
              // pointColor : "rgba(220,220,220,1)",
              // pointStrokeColor : "#fff",
              spanGaps: true,
              pointHoverBackgroundColor: "pink",
              pointHoverBorderColor: 'blue',
              pointHoverBorderWidth: 2,
              pointHoverRadius: 10,
              borderWidth: 2,
              pointBorderColor: '#249EBF',
              
          }
        ]
      },
      chartOptions: {
        tooltips: {
          callbacks: {
            title: (tooltipItem, data) => data.labels[tooltipItem[0].index]
          }
        },
        responsive: true,
        legend: {
          display: false,
        },

        scale: {
          pointLabels: {
            label: 'here',
            fontSize: 13,
            fontFamily: "'Raleway', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
          },
          ticks: {
            color: 'red',
          },
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
                display: false,
                min: 0,
                max: 200,
              },
              gridLines: {
                display: false,
              },
              scaleLabel: {
                display: false,
              }
            }
          ],
          xAxes: [
            {
              gridLines: {
                display: false,
              },
              ticks: {
                display: false,
              },
              
            }
          ]
        }
      }
    }
  },

  mounted() {
    this.renderChart(this.dataCollection, this.chartOptions)
  },
}

</script>

<style>

</style>