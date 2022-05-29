const mongoose=require('mongoose')
const {Schema,model}=mongoose

const authorSchema=new Schema({
    name:String,
    age:String,
})

module.exports=model('Author',authorSchema)