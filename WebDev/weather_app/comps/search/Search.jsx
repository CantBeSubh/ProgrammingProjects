import { useState } from "react"
import { AsyncPaginate } from "react-select-async-paginate"

const Search = ({ onSearchChange }) => {
    const [search, setSearch] = useState(null)
    const handleChange = (searchedData) => {
        setSearch(searchedData)
        onSearchChange(searchedData)
    }
    return (
        <AsyncPaginate
            placeholder='Search for city'
            debounceTimeout={600}
            value={search}
            onChange={handleChange}
        />
    )
}

export default Search