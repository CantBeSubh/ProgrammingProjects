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
      {appearance && <h1>Appearance</h1>}
        {gender && gender!='-' && <div>Gender: {gender}</div>}
        {race && <div>Race: {race}</div>}
        {height && height[0]!=0 && <div>Height: {height}</div>}
        {weight && weight[0]!=0 && <div>Weight: {weight}</div>}
    </div>
  )
}

export default Appearance