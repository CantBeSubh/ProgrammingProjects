import React from 'react'

function Work(props) {
  let work=props.work
  return (
    <div>
      Work
      {work&&
      <p> {work.occupation=='-'?'Unknown occupation':'You work as '+work.occupation}</p>
      }
    </div>
  )
}

export default Work