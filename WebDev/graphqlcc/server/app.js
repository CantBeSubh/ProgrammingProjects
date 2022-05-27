const express=require("express")
const {graphqlHTTP}=require('express-graphql')
const schema=require('./scheme/schema')

const app=express()
const port=3000

app.use('/graphql',graphqlHTTP({schema}))
app.listen(port,()=>console.log(`[+] Server stated at port: ${port}`))