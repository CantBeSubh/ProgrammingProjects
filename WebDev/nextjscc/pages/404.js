import Link from "next/link";
import { useRouter } from 'next/router';

const NotFound = () => {
    const { asPath } = useRouter();
    return ( 
        <div  className="not-found">
            <h1>Error!</h1>
            <h2>Page <a>{asPath}</a> found.</h2>
            <p>Go to <Link href='/'><a>Home</a></Link></p>
        </div>
     );
}
 
export default NotFound;