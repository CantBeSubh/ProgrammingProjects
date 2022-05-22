import React from 'react'
import {Bar} from '@samsquatch/react-chartjs-2'
function Powerstat(props) {
    const {powerstats}=props
    console.log(powerstats)
    let labels=[]
    let data=[]
    if(powerstats){
        
        Object.entries(powerstats).forEach(([key, value]) => {
            labels.push(key)
            data.push(value)
         })
    }
    // for(let [i,j] in ){
    //     console.log(i)
    // }
  return (
    <div>
        Powerstat
        {powerstats &&
                <Bar
                data={ {
                    labels,
                    datasets:[{
                        label: '',
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
                        borderWidth: 1
                    }]
                }}
                height={400}
                width={600}
                options={
                    {
                        indexAxis: 'y'
                    }
                    }
                />
        }

    </div>

  )
}

export default Powerstat 