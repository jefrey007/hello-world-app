import React, { useEffect, useState } from 'react';

function App() {
  const [greeting, setGreeting] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000')
      .then(response => response.text())
      .then(data => setGreeting(data))
      .catch(err => console.error('Error fetching greeting:', err));
  }, []);

  return (
    <div className="App">
      <h1>{greeting}</h1>
    </div>
  );
}

export default App;
