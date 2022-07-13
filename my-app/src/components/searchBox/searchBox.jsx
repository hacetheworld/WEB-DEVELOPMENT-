import React from "react"
import "./searchBox.css"
export const SearchBox=({placeHolder,handleChange})=>{
return (
<input
       type="search"
       name="search"
       id="1"
       placeholder={placeHolder}
       className="search"
       onChange={handleChange} />
       )
}