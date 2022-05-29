const graphql=require('graphql')
const _=require('lodash')
const Book=require('../model/book')
const Author=require('../model/author')

const {
    GraphQLObjectType,
    GraphQLString,
    GraphQLSchema,
    GraphQLID,
    GraphQLInt,
    GraphQLList,
    GraphQLNonNull
}=graphql

// var books = 
// [
//     { "name": "Name of the Wind", "genre": "Fantasy", "authorId": "62932aa2a272b91b38198b61" },
//     { "name": "The Final Empire", "genre": "Fantasy", "authorId": "62932aa2a272b91b38198b62" },
//     { "name": "The Long Earth", "genre": "Sci-Fi", "authorId": "62932aa2a272b91b38198b63" },
//     { "name": "The Hero of Ages", "genre": "Fantasy", "authorId": "62932aa2a272b91b38198b62" },
//     { "name": "The Colour of Magic", "genre": "Fantasy", "authorId": "62932aa2a272b91b38198b63" },
//     { "name": "The Light Fantastic", "genre": "Fantasy", "authorId": "62932aa2a272b91b38198b63" }
// ];

// var authors = 
// [
//     { "name": 'Patrick Rothfuss', "age": 44 },
//     { "name": 'Brandon Sanderson', "age": 42 },
//     { "name": 'Terry Pratchett', "age": 66 }
// ]


const BookType=new GraphQLObjectType({
    name:'Book',
    fields:()=>({
        id:{type:GraphQLID},
        name:{type:GraphQLString},
        genre:{type:GraphQLString},
        author:{
            type:AuthorType,
            resolve(parent,args){
                    // return  _.find(authors,{id:parent.authorId})
                    return Author.findById(parent.authorId)
                }
            }
    })
})

const AuthorType=new GraphQLObjectType({
    name:'Author',
    fields:()=>({
        id:{type:GraphQLID},
        name:{type:GraphQLString},
        age:{type:GraphQLInt},
        books:{
            type:new GraphQLList(BookType),
            resolve(parent,args){
                // return _.filter(books,{authorId:parent.id})
                return Book.find({authorId:parent.id})
            }
        }
    })
})

const RootQuery=new GraphQLObjectType({
    name:'RootQueryType',
    fields:{
        book:{
            type:BookType,
            args:{id:{type:GraphQLID}},
            resolve(parent,args){
                // return _.find(books, { id: args.id })
                return Book.findById(args.id)
            }
        },
        author:{
            type:AuthorType,
            args:{id:{type:GraphQLID}},
            // resolve:(parent,args)=>_.find(authors,{id:args.id})
            resolve:(parent,args)=>Author.findById(args.id)
        },
        books:{
            type: new GraphQLList(BookType),
            resolve:(parent,args)=>Book.find()

        },
        authors:{
            type: new GraphQLList(AuthorType),
            resolve:(parent,args)=>Author.find()

        }
    }
})

const Mutation=new GraphQLObjectType({
    name:'Mutation',
    fields:{
        addAuthor:{
            type:AuthorType,
            args:{
                name:{type:new GraphQLNonNull(GraphQLString)},
                age:{type:new GraphQLNonNull (GraphQLInt)}
            },
            resolve:(parent,args)=>{
                let author=new Author({
                    name:args.name,
                    age:args.age
                })
                return author.save()
            }
        },
        addBook:{
            type:BookType,
            args:{
                name:{type:new GraphQLNonNull(GraphQLString)},
                genre:{type:new GraphQLNonNull(GraphQLString)},
                authorId:{type:new GraphQLNonNull(GraphQLID)}
            },
            resolve:(parent,args)=>{
                let book=new Book({
                    name:args.name,
                    genre:args.genre,
                    authorId:args.authorId
                })
                return book.save()
            }
        }
    }
})

module.exports=new GraphQLSchema({
    query:RootQuery,
    mutation:Mutation
})