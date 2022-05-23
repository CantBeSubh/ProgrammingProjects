import React from 'react'

function Appearance(props) {
  const {appearance}=props
  let gender,race,height,weight
  if(appearance){
    gender=appearance.gender
    race=appearance.race
    weight=appearance.weight[1]
    height=appearance.height[1]
  }
  return (
    <div>
      <h1>Appearance</h1>
      <ul>
        {gender && gender!='-' && <li>Gender: {gender}</li>}
        {race && <li>Race: {race}</li>}
        {height && height[0]!=0 && <li>Height: {height}</li>}
        {weight && weight[0]!=0 && <li>Weight: {weight}</li>}
      </ul>
    </div>
  )
}

export default Appearance