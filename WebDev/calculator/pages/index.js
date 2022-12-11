import Head from 'next/head'
import { useState } from 'react';
import styles from '../styles/Home.module.css'

export default function Home() {
  const creatDigits = () => {
    const digits = [];
    for (let i = 1; i < 10; i++)
      digits.push(<button
        key={i}
        onClick={() => updateCalc(i.toString())}
      >{i}
      </button>
      )
    return digits;
  }

  const [calc, setCalc] = useState("");
  const [result, setResult] = useState("");
  const ops = ["+", "-", "*", "/", "."];

  const updateCalc = value => {
    if (
      ops.includes(value) && calc === "" ||
      ops.includes(value) && ops.includes(calc.slice(-1))
    ) return;

    setCalc(calc + value);

    if (!ops.includes(value)) {
      setResult(eval(calc + value).toString());
    }
  }

  const calculate = () => {
    if (calc === "") return;
    setCalc(eval(calc).toString());
  }

  const deleteLast = () => {
    if (calc === "") return;
    setCalc(calc.slice(0, -1));
  }

  return (
    <>
      <Head>
        <title>Calculator</title>
        <meta name="description" content="Basic calcultor" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <div className={styles.calculator}>
          <div className={styles.display}>
            {result ? <span>({result}) </span> : ""}
            {calc || "0"}
          </div>

          <div className={styles.operators}>
            <button onClick={() => updateCalc("+")}>+</button>
            <button onClick={() => updateCalc("-")}>-</button>
            <button onClick={() => updateCalc("*")}>*</button>
            <button onClick={() => updateCalc("/")}>/</button>

            <button onClick={() => deleteLast()}>DEL</button>
          </div>

          <div className={styles.digits}>
            {creatDigits()}
            <button onClick={() => updateCalc("0")}>0</button>
            <button onClick={() => updateCalc(".")}>.</button>
            <button onClick={() => calculate()}>=</button>
          </div>
        </div>
      </main>
    </>
  )
}
