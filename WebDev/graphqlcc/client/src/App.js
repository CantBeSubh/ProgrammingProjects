import Booklist from "./comps/BookList";

import {ApolloClient,ApolloProvider,InMemoryCache} from "@apollo/client";
import AddBook from "./comps/AddBook";

const client=new ApolloClient({
  uri:'http://localhost:3001/graphql',
  cache:new InMemoryCache()
})
function App() {
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <h1>My Reading List</h1>
        <Booklist/>
        <AddBook/>
      </div>
    </ApolloProvider>
  );
}

export default App;