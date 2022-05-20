import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import Link from 'next/link'

export default function Home() {
  return (
    <>
      <Head>
        <title>Ninja List | Home</title>
      </Head>
      <div >
        <h1 className={styles.title}>Homepage</h1>
        <p className={styles.text}>Magna commodo nostrud ad amet nulla culpa esse tempor qui aute. Cillum est do eu adipisicing minim commodo cupidatat occaecat ipsum exercitation et ea amet irure. Aliquip duis qui velit esse voluptate nulla reprehenderit excepteur eiusmod.</p>
        <p className={styles.text}>Magna commodo nostrud ad amet nulla culpa esse tempor qui aute. Cillum est do eu adipisicing minim commodo cupidatat occaecat ipsum exercitation et ea amet irure. Aliquip duis qui velit esse voluptate nulla reprehenderit excepteur eiusmod.</p>
        <Link href='/ninjas'>
          <a className={styles.btn}>See Ninjas list</a>
        </Link>
      </div>
    </>
  )
}
