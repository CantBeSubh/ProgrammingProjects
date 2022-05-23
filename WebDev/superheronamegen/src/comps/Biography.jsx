import React from 'react'

function Biography(props) {
  let bio=props.biography
  return (
    <div>
      Biography
      {bio && 
      <div>
        <p>Your name is {bio.fullName}.</p>
        <p>Your birth place is {bio.placeOfBirth=='-'?'unknown': bio.placeOfBirth}.</p>You first appeared in {bio.firstAppearance}.
      </div>
      }
    </div>
  )
}

export default Biography