import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { 
  Streamlit, 
  withStreamlitConnection,

} from "streamlit-component-lib";

function App() {
  const [count, setCount] = useState(0)

  console.log("hi")
  useEffect(() => {
    Streamlit.setComponentValue("some value");
    Streamlit.setFrameHeight();
  }, []);
  

  return (
    <>
      <h1>Home App</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Welcome to Home reat App!
        </p>
      </div>
    </>
  )
}

export default withStreamlitConnection(App)
