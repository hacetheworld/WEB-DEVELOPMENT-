import React from "react"
import {Card} from "../card/card"
import "./cardlist.css"
export const CardList=(props)=>{
return (
<div className="card-list
"> {
    props.monsters.map(monster => (
       <Card key={monster.id} monster={monster} Card/>
    ))}</div>)
}