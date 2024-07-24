import { useEffect, useState } from 'react'

import './App.css'

function App() {
  const [data, setData] = useState([])

  const URL = 'http://127.0.0.1:8000/api/jokes/'  
  useEffect(() => {
    async function fetchData() {
      try{
        const response = await fetch(URL);
        const result = await response.json()
        console.log(result)
        setData(result)
        if(response.ok){
          console.log("Success!")
        }
      } catch(error){
        console.log(error.message)
      }
    }

    fetchData()
  },[])


  return (
    <div>
      <h1>My Joke app</h1>

      {data.map((joke,index) =>{
        return(
          <p key={index}>{joke.joke}</p>
        )
      }

      )}
    </div>
  )
}

export default App
