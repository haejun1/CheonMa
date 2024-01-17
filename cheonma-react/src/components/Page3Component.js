import React, { useState, useEffect } from "react";

function Page3Component() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const dummyData = {
      message: "Data from Page 3",
      content: "This is the content of Page 3.",
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

export default Page3Component;
