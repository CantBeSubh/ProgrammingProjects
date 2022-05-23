import React from 'react'

function Work(props) {
  let work=props.work
  return (
    <div>
      Work
      {work&&
      <p>You work as {work.occupation}</p>
      }
    </div>
  )
}

export default Work