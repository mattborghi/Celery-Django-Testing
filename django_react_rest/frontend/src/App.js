import React, { useState, useEffect } from "react";

// const list = [
//   {
//     id: 1,
//     title: "Learn Python",
//     description: "Learning Python"
//   },
//   {
//     id: 2,
//     title: "Study React",
//     description: "Study React Description"
//   },
//   {
//     id: 3,
//     title: "Third ToDo",
//     description: "Third todo description"
//   }
// ];

function App() {
  const [data, setData] = useState([]);

  async function fetchMyAPI() {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/");
      const todos = await res.json();
      setData(todos);
    } catch (e) {
      console.log(e);
    }
  }

  useEffect(() => {
    fetchMyAPI();
  }, []);

  return (
    <div>
      {data.map(item => (
        <div key={item.id}>
          <h1>{item.title}</h1>
          <span>{item.description}</span>
        </div>
      ))}
    </div>
  );
}

export default App;
