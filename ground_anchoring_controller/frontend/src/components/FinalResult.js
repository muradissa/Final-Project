import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import React, { useState,useEffect }  from "react";
import { useNavigate } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import Tables from './Tables';



let anchorsMap = new Map()
let x1 = 0 , y1 = 0;

const FinalResult = () => {
    
    const navigate = useNavigate();
    const [isLoading, setLoading] = useState(false);
    const [anchorNumber, setAnchorNumber] = useState(1);
    const [numbersOfAnchors, setNumbersOfAnchors] = useState(localStorage.getItem("numbersOfAnchors"));
    const height = localStorage.getItem("height");
    const width = localStorage.getItem("width");
    const angle = localStorage.getItem("angle");
   


    return (
      <div className="manually">
            <div className="row">

                <div className="col-3" >
                    <div style={{
                        padding:'10px',
                        marginLeft:'50px',
                        color:'white',
                        border: '2px solid #ccc',
                        borderRadius:'15px'}}>
                            <h5>Number of Anchors : {numbersOfAnchors}</h5>
                            <h5>Strategy : Manually</h5>
                            <h5>Dimensional : 1</h5>    
                            <h5>Heigth : {height}m</h5>
                            <h5>Width : {width}m</h5>  
                            <h5>Angle : {angle}<sup style={{color:'white'}}>o</sup></h5> 
                            <h5>E : 30 </h5>
                            <h5>I : 104 </h5> 
                            <h5>V : 0.1 </h5>
                            <h5>C : 1 </h5>    
                    </div>
                    <div className='row' style={{paddingTop:'20px',textAlign:'center',}}>
                        <h3 style={{color:'white'}}>Cost : <b style={{color:'white'}}>{numbersOfAnchors*2178} $</b></h3>
                        <h3 style={{color:'white'}}>Quality : <b style={{color:'white'}}>90 %</b></h3>
                        
                    </div>                                 
                    
                </div>
                <div className="col-8 center-Table">
                    <Tables style={{textAlign:'-webkit-center',}}/>
                </div>
            </div>
            
            
      </div>
    );
  }
   
  export default FinalResult;
