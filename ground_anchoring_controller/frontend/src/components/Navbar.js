import React, {Component,useState,useEffect} from "react";

import { Link } from "react-router-dom";
import { BsFillQuestionCircleFill } from "react-icons/bs";

const Navbar = () => {

  clearThelocalStorage=()=>{
    localStorage.clear();
  }
  return (
    <div>
      
      <nav className="navbar">
        <h1>Optimization of the ground wall anchoring</h1>
        <div className="links">
          {/* <Link to="/">Home</Link> */}
          <Link variant="primary" to="/" onClick={clearThelocalStorage} style={{ 
            color: 'white', 
            backgroundColor: '#0080FF',
            borderRadius: '8px' 
          }}>New Senrio </Link>
        </div>
        <BsFillQuestionCircleFill style={{ padding:'5px',cursor: 'pointer'}} size={27} />
      </nav> 
    </div>
  );
}
 
export default Navbar;