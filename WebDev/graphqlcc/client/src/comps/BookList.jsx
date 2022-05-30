import {useQuery} from '@apollo/client'
import { useState } from 'react'
import { getBooksQuery } from '../queries'
import BookDetails from './BookDetails'



function Booklist() {
  const { loading, error, data } = useQuery(getBooksQuery)
  const [selected,setSelected]=useState('')
  if (loading) return 
  if (error) return 

  const {books}=data

  const displayBooks=()=>{
    return books.map(({id,name,author})=>
    <li 
    key={id} 
    onClick={e=>setSelected(id)}>
      {name} by {author.name}
    </li>
    )
  }
  
  return (
    <>
      <div id="book-list">
        <ul>
        {displayBooks()}
        </ul>
      </div>
      <BookDetails bookId={selected}/>
    </>
  );
}
  
export default Booklist;  