import Link from 'next/link'
import ninja from '../../styles/Ninjas.module.css'
export const getStaticProps=async ()=>{
    const res=await fetch('https://jsonplaceholder.typicode.com/users')
    const data=await res.json()

    return {
        props:{ninjas:data}
    }
}


const Ninjas = (props) => {
    const {ninjas}=props
    return ( 
        <>
            <h1>Ninja Listing</h1>
            {ninjas.map(({name,id})=>(
                <Link href={'/ninjas/'+id} key={id}>
                    <a className={ninja.single}>
                        <h3>{name}</h3>
                    </a>
                </Link >
            ))}
        </>
     );
}
 
export default Ninjas;