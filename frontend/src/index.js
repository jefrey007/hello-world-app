import React from 'react';
import ReactDOM from 'react-dom/client';  // Make sure to import from 'react-dom/client'
import './index.css';  // Optional, if you want to add some styles
import App from './App';  // Import your main component

// Create a root and render your app inside it
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
