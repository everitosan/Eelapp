import React from 'react';
import logo from './logo.svg';
import './App.css';

import {sayHello} from './Infrastructure/rpc/python/Client'

function App() {

  const [pyRes, setPyRes] = React.useState(0)


  setTimeout(() => {
    sayHello({name: 'Ever'}, (res)=> {
      setPyRes(res)
    })
  }, 2000)

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
        Python says  { pyRes }
        </a>
      </header>
    </div>
  );
}

export default App;
