import React from "react"
import "./card.css"
export const Card=(props)=>{
    const { id,name,email} = props.monster;

return (
<div className="card-container
">
    <img src={`https://robohash.org/${id}?set=set1&size=180x180`} alt="robot" />
    <h2>{name}</h2>
    <p>{email}</p>
</div>

)
}