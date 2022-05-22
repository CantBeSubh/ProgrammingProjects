import React from 'react'
import {useState,useEffect} from 'react'
import Powerstat from './comps/Powerstat'
import Appearance from './comps/Appearance'
import Biography from './comps/Biography'
import Connections from './comps/Connections'
import Work from './comps/Work'

function Hero() {
    let [data,setData]=useState([])
    const rand=()=>Math.floor(Math.random()*730)+1

    const fetchData=async ()=>{
        const id =rand()
        const res=await fetch(
            `https://akabab.github.io/superhero-api/api/id/${id}.json`
        )
        let data = await res.json()
        setData(data)
    }

    let {name,powerstats,appearance,biography,work,connections,images} = data
    
    return (
    <div>
        <div className="name">Hello {name}!</div>
        <img src={images && images.sm} className='image'/>

        <div>Details</div>
        <Powerstat powerstats={powerstats}/>
        <Appearance appearance={appearance}/>
        <Biography biography={biography}/>
        <Work work={work}/>
        <Connections connections={connections}/>
        <div onClick={fetchData} id='btn'>Click ME</div>
    </div>

  )
}

export default Hero