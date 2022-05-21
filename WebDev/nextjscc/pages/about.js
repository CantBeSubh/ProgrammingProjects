import Head from "next/head";
import styles from '../styles/Home.module.css'
const about = () => {
    return (
    <>
        <Head>
            <title>Ninja List | About</title>
        </Head>
        <div>
            <h1 className={styles.title}>About!</h1>
            <p className={styles.text}>Magna commodo nostrud ad amet nulla culpa esse tempor qui aute. Cillum est do eu adipisicing minim commodo cupidatat occaecat ipsum exercitation et ea amet irure. Aliquip duis qui velit esse voluptate nulla reprehenderit excepteur eiusmod.</p>
            <p className={styles.text}>Magna commodo nostrud ad amet nulla culpa esse tempor qui aute. Cillum est do eu adipisicing minim commodo cupidatat occaecat ipsum exercitation et ea amet irure. Aliquip duis qui velit esse voluptate nulla reprehenderit excepteur eiusmod.</p>
        </div>
    </>
    );
}
 
export default about;