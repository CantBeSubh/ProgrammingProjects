import {gql,useQuery} from '@apollo/client'

const getBooksQuery=gql`
  {
    books{
      name
      id
      author{
        name
      }
    }
  }
`

function Booklist() {
  const { loading, error, data } = useQuery(getBooksQuery)
  if (loading) return <p>Loading...</p>
  if (error) return <p>Error!</p>

  const {books}=data

  const displayBooks=()=>{
    return books.map(({id,name,author})=><li key={id}>{name} by {author.name}</li>)
  }
  

  return (
    <div className="Booklist">
      <ul>
      {displayBooks()}
      </ul>
    </div>
  );
}
  
export default Booklist;  