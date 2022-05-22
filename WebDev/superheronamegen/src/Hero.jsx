import React from 'react'
import {useState,useEffect} from 'react'

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

    let {name,images} = data
    
    return (
    <div>
        <div className="name">Hello {name}!</div>
        <img src={images && images.sm} className='image'/>
        <div onClick={fetchData}>Click ME</div>
    </div>

  )
}

export default Hero