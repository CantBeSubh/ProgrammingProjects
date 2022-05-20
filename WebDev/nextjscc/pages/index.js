import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import Navbar from '../comps/Navbar'
import Footer from '../comps/Footer'

export default function Home() {
  return (
    <div >
      <Navbar />
      <h1>Hello!</h1>
      <p>Magna commodo nostrud ad amet nulla culpa esse tempor qui aute. Cillum est do eu adipisicing minim commodo cupidatat occaecat ipsum exercitation et ea amet irure. Aliquip duis qui velit esse voluptate nulla reprehenderit excepteur eiusmod.</p>
      <p>Magna commodo nostrud ad amet nulla culpa esse tempor qui aute. Cillum est do eu adipisicing minim commodo cupidatat occaecat ipsum exercitation et ea amet irure. Aliquip duis qui velit esse voluptate nulla reprehenderit excepteur eiusmod.</p>
      <Footer />
    </div>
  )
}
