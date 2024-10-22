import React, { useState } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Switch, useHistory } from 'react-router-dom';

// Use environment variable for backend URL
const backendURL = window.REACT_APP_BACKEND_URL || 'http://localhost:5000';  // Use a default value if the env variable isn't set
// Login component
function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const history = useHistory();  // React Router's hook for navigation

  const handleLogin = async (e) => {
    e.preventDefault();
    console.log('Attempting login...');
    try {
      const response = await axios.post(`${backendURL}/login`, { 
        username, 
        password 
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
  
      console.log('Login response:', response.data);
  
      if (response.data.message === 'Login successful!') {
        console.log('Login successful, redirecting to /welcome...');
        setMessage('');
        history.push('/welcome');
      } else {
        console.log('Login failed, displaying invalid credentials message...');
        setMessage('Invalid credentials');
      }
    } catch (error) {
      console.log('Error during login:', error);
      setMessage('Invalid credentials');
    }
  };
  

  return (
    <div className="App">
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

// Welcome component
function Welcome() {
  return (
    <div>
      <h1>Welcome to the Dashboard!</h1>
      <p>This is a simple dashboard after login.</p>
    </div>
  );
}

// Main App component
function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route path="/welcome" component={Welcome} />
      </Switch>
    </Router>
  );
}

export default App;

