import React, { useState } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Switch, useHistory } from 'react-router-dom';
import './App.css';  // Import the custom CSS file

const backendURL = window.REACT_APP_BACKEND_URL || 'http://localhost:5000';
function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const history = useHistory();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${backendURL}/login`, { username, password }, {
        headers: { 'Content-Type': 'application/json' }
      });
      if (response.data.message === 'Login successful!') {
        setMessage('');
        history.push('/welcome');
      } else {
        setMessage('Invalid credentials');
      }
    } catch (error) {
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

function Welcome() {
  return (
    <div className="dashboard">
      <h1>Welcome to the Dashboard!</h1>
      <p>This is a simple dashboard after login.</p>
    </div>
  );
}

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
