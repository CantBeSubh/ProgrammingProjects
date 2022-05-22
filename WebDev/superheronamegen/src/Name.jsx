import React from 'react'
import {useState} from 'react'

function Name() {
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

    return (
    <div id='name'>
        Hello {data.name}!
        <div onClick={fetchData}>Click ME</div>
    </div>

  )
}

export default Name