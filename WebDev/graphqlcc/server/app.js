const express=require("express")
const {graphqlHTTP}=require('express-graphql')
const schema=require('./scheme/schema')
const mongoose=require('mongoose')

const connectToDB=()=>{
    console.time('[+] Connected to Database')
    mongoose
        .connect('mongodb+srv://holycow:Dec042001BdKp@cluster0.wx51l.mongodb.net/?retryWrites=true&w=majority',
        ()=>{console.timeEnd('[+] Connected to Database')})
        .catch((err)=>{console.log('[!] '+err+'\n[-] Disconnecting...');process.exit(1)})
}


const app=express()
const port=3000

app
    .use('/graphql',graphqlHTTP({schema,graphiql:true}))
    .listen(port,()=>{console.log(`[+] Server stated at port: ${port}`);connectToDB()})