import React , {Component} from "react"
import logo from './logo.svg';

import './App.css';

class App extends Component{
  constructor(){
    super()
    this.state={
      isSet:true,
      name:"Ajay"
    }

  }
  render(){
    return (
      <div className="App">
      <h1>Hello This Is {this.state.name}</h1>
      <button onClick={()=>{this.setState({name:"Vijay"})}}>Change Text</button>
      </div>
    );
  }
}

export default App;
