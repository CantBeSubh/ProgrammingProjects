import React from 'react'

function Biography(props) {
  let bio=props.biography
  return (
    <div>
      {bio && <h1>Biography</h1>}
      {bio && 
      <div>
        <p>Your name is {bio.fullName==''?'unknown':bio.fullName}.</p>
        <p>Your birth place is {bio.placeOfBirth=='-'?'unknown': bio.placeOfBirth}.</p>You first appeared in {bio.firstAppearance}.
      </div>
      }
    </div>
  )
}

export default Biography