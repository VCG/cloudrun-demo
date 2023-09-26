import "./App.css";
import React, { useEffect, useState } from "react";

function App() {
  const [text, setText] = useState("");

  useEffect(() => {
    let url = `${process.env.REACT_APP_API_PROTOCOL}://${process.env.REACT_APP_API_URL}/`;
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setText(data);
      })
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <h1>{text + " - This was loaded dynamically through an endpoint!"}</h1>
  );
}

export default App;
