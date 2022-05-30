import { getBookQuery } from "../queries";
import {useQuery} from '@apollo/client'


function BookDetails({bookId}) {
    const { loading, error, data } = useQuery(getBookQuery,{variables:{id:bookId}})
    const book=data?data.book:''

    return (
        <div id="book-details">
            {loading && <p>Loading...</p>}
            {error && bookId && <p>Error!</p>}
            {book &&
                <div>
                <h2>{ book.name }</h2>
                <p>{ book.genre }</p>
                <p>{ book.author.name }</p>
                <p>All books by this author:</p>
                <ul className="other-books">
                    { book.author.books.map(item => {
                        return <li key={item.id}>{ item.name }</li>
                    })}
                </ul>
            </div>
            }
        </div>
    )
}

export default BookDetails