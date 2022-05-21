export const getStaticPaths=async ()=>{
    const res =await fetch('https://jsonplaceholder.typicode.com/users')
    const data= await res.json()
    const paths= data.map(elm=>{params:{id:elm.id.toString()}})
    return{paths,fallback:false}
}
export const getStaticProps=async (context)=>{
    const id=context.params.id
    const res=await fetch('https://jsonplaceholder.typicode.com/users'+id)
    const data= await res.json()
    return {
        params:{ninja:data}
    }
}
const Details = ({ninja}) => {
    return ( 
        <div>
            <h1>{ninja.name}</h1>
            <h2>{ninja.email}</h2>
            <h2>{ninja.website}</h2>
            <h2>{ninja.address.city}</h2>
        </div>
     );
}
 
export default Details;