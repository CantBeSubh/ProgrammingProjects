import {useQuery} from '@apollo/client'
import { useState } from 'react'
import { getBooksQuery } from '../queries'
import BookDetails from './BookDetails'



function Booklist() {
  const { loading, error, data } = useQuery(getBooksQuery)
  const [selected,setSelected]=useState('')
  if (loading) return <p>Loading...</p>
  if (error) return <p>Error!</p>

  const {books}=data

  const displayBooks=()=>{
    return books.map(({id,name,author})=><li key={id} onClick={e=>setSelected(id)}>{name} by {author.name}</li>)
  }
  

  return (
    <div className="Booklist">
      <ul>
      {displayBooks()}
      </ul>
      <BookDetails bookId={selected}/>
    </div>
  );
}
  
export default Booklist;  