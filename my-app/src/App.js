import React , {Component} from "react"
import {CardList} from "./components/card-list/cardlist"
import './App.css';
import { SearchBox } from "./components/searchBox/searchBox";

class App extends Component{
  constructor(){
    super()
    this.state={
      monsters:[],
      searchField:""
    }
    // this.handleChange=this.handleChange.bind(this)
  }
  componentDidMount(){
    fetch('https://jsonplaceholder.typicode.com/users')
    .then(response => response.json())
    .then(users =>this.setState({monsters:users}))
    }

    handleChange=(e)=>{
      this.setState({searchField:e.target.value})
    }
  render(){
    // console.log(this,"sdfs","saaa");
    const {monsters,searchField} =this.state
    const filteredMonsters=monsters.filter((monster)=>
    monster.name.toLowerCase().includes(searchField.toLowerCase())
    )
    return (
      <div className="App">
        <h1>Monsters Rolodox</h1>
      <SearchBox
      placeHolder="Search Monster"
      handleChange={this.handleChange}
      />
      <CardList monsters={filteredMonsters}></CardList>
      </div>
    );
  }
}

export default App;
