import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {
	Streamlit,
	withStreamlitConnection
} from "streamlit-component-lib";

function App() {
  const [count, setCount] = useState(0)

  useEffect(() => {
	Streamlit.setComponentValue("test value");
	Streamlit.setFrameHeight();
  }, []);

  return (
    <>
      <h1>About App</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          This is Seolynn Streamlit Project
        </p>
      </div>
    </>
  )
}

export default withStreamlitConnection(App);
