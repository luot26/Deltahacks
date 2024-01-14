import React, { useEffect, useState } from 'react';

const JsonDisplay = () => {

  const outputBox = document.getElementById("outputBox");

  useEffect(() => {

    fetch("/api/data")
      .then(response => response.json())
      .then(data => {

        outputBox.textContent = JSON.stringify(data);
      })
      .catch(error => {
        console.error("Error fetching JSON data:", error);
      });
  }, []); 

  return (
    <div>
      <h2>JSON Data</h2>
      {/* Your other JSX elements */}
    </div>
  );
};

export default JsonDisplay;
