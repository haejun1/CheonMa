import React, { useState, useEffect } from "react";

function Page4Component() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const dummyData = {
      message: "Data from Page 4",
      content: "This is the content of Page 4.",
    };

    setData(dummyData);
  }, []);

  return (
    <div>
      {data ? (
        <div>
          <h2>{data.message}</h2>
          <p>{data.content}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default Page4Component;
