import React from 'react'
import {HorizontalBar} from '@samsquatch/react-chartjs-2'
function Powerstat(props) {
    const {powerstats}=props

    let labels=[]
    let data=[]
    let options={
        scales: {
            xAxes: [{
                ticks: {
                    beginAtZero: true
                },
                gridLines: {
                    display: true
                }
            }],
            yAxes: [{
                gridLines: {
                display: false
                }
            }]
            
        },
        maintainAspectRatio:false
    }
    if(powerstats){
        Object.entries(powerstats).forEach(([key, value]) => {
            labels.push(key.toUpperCase())
            data.push(value)
         })
    }

    let datasets=[{
        label: 'Out of 100',
        data,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'],
        borderWidth: 1,
    }]

  return (
    <div>
        <h1>Powerstat</h1>
        {powerstats &&
            <HorizontalBar
            data={{labels,datasets}}
            height={200}
            width={100}
            options={options}
            />
        }

    </div>

  )
}

export default Powerstat 