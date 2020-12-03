import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import Homepage from './components/pages/Homepage.js'
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';
import Register from './components/pages/Register';
import './components/API/IGDB.js';
import Search from './components/pages/Search';
import Game from './components/pages/Game';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" exact component={Homepage}/>
          <Route path="/register" exact component={Register} />
          <Route path="/search_game" exact component={Search} />
          <Route path="/game" exact component={Game} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
