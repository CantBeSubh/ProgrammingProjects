import Link from "next/link";
import { useRouter } from 'next/router';
import { useEffect } from "react";

const NotFound = () => {
    const router = useRouter();
    setTimeout(()=>router.push('/'),3000)

    return ( 
        <div  className="not-found">
            <h1>Error!</h1>
            {/* <h2>Page <a>{router.asPath}</a> found.</h2> */}
            <p>Going to <Link href='/'><a>Home</a></Link></p>
        </div>
     );
}
 
export default NotFound;