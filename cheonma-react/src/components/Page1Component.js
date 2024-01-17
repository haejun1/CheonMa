import React, { useState, useEffect } from "react";

function Page1Component() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const dummyData = {
      message: "Data from Page 1",
      content: "This is the content of Page 1.",
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

export default Page1Component;
