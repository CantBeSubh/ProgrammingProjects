import { useQuery } from "@apollo/client";
import { getAuthorsQuery } from "../queries";


function AddBook() {
  const { loading, error, data } = useQuery(getAuthorsQuery)
  if (loading) return <p>Loading...</p>
  if (error) return <p>Error!</p>

  const {authors}=data
  console.log(authors)

  const displayAuthors=()=>{
    return authors.map(author=><option key={ author.id } value={author.id}>{ author.name }</option>)
  }
  
  return (
    <form id="add-book">
      <div className="field">
        <label>Book name:</label>
        <input type="text" />
      </div>
      <div className="field">
        <label>Genre:</label>
        <input type="text" />
      </div>
      <div className="field">
        <label>Author:</label>
        <select>
          <option>Select author</option>
          {displayAuthors()}
        </select>
      </div>
      <button>+</button>
    </form>
  );
}

export default AddBook;
