const PORT=3000
const axios = require('axios').default
const express=require('express')
const cors=require('cors')
require('dotenv').config()
const app=express()
app.use(cors())
app.use(express.json)


app.post('/solve/',(req,res)=>{
    const options = {
        method: 'POST',
        url: 'https://solve-sudoku.p.rapidapi.com/',
        headers: {
            'content-type': 'application/json',
            'x-rapidapi-host': 'solve-sudoku.p.rapidapi.com',
            'x-rapidapi-key': process.env.RAPID_API_KEY
        },
        data: {
            puzzle:'2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
        }
    }
    
    axios.request(options).then(function (response) {
        console.log(response.data);
        res.json(response.data);
    }).catch(function (error) {
        console.error(error);
    })
    console.log('response.data');
})

app.listen(PORT,()=>console.log('Server Started @ 3000'))