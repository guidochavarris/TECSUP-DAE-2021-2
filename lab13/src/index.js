import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import { Route, Link, BrowserRouter,Routes} from 'react-router-dom'
import App from './App'
import Users from './users'
import Contact from './contact'
import Notfound  from './notfound';
import 'bootstrap/dist/css/bootstrap.css';
const routing = (
  
<div>
    <BrowserRouter>

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/usuarios">Users</a>
      </li>

      <li class="nav-item">
        <a class="nav-link" href="/contacto">contact</a>
      </li>

      
      
      
    </ul>
    
  </div>
</nav>
    

      <Routes>
        <Route exact path="/" element={<App />} />
        < Route path="/usuarios/:id" element={<Users />} />
        <Route path="/contacto" element={<Contact />} />
        <Route path="*" element = {<Notfound />} />
      </Routes>
    </BrowserRouter>
  </div>  
)
ReactDOM.render(routing, document.getElementById('root'))