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
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;
  const {books}=data

  return (
    <div className="Booklist">
      {books.map(({id,name,author})=><div key={id}>
        {name} by {author.name}
        </div>)}
    </div>
  );
}
  
export default Booklist;  