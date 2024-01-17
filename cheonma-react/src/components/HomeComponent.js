import React, { useState, useEffect } from "react";

function HomeComponent() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/home/");
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return <div>{data ? <p>{data.message}</p> : <p>Loading...</p>}</div>;
}

export default HomeComponent;
