import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import React, { useState,useEffect }  from "react";
import { useNavigate } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import Tables from './Tables';
import LoadingDots from './Loading'
import { Spinner } from 'react-bootstrap';
//import { MDBSpinner } from 'mdb-react-ui-kit';
//import 'bootstrap/dist/css/bootstrap.min.css';

let anchorsMap = new Map()
let x1 = 0 , y1 = 0;
let acnhors_data;

const FinalResult = () => {
    
    const navigate = useNavigate();
    const [isLoading, setLoading] = useState(false);
    const [anchorNumber, setAnchorNumber] = useState(1);
    const [numbersOfAnchors, setNumbersOfAnchors] = useState(localStorage.getItem("numbersOfAnchors"));
    const height = localStorage.getItem("height");
    const width = localStorage.getItem("width");
    const angle = localStorage.getItem("angle");
    const [strategyType, setStrategyType] = useState(localStorage.getItem("optimizationType2"));
    const [optimizationType, setOptimizationType] = useState(localStorage.getItem("strategyType2"));
    const [dimensionalType, setDimensionalType] = useState(localStorage.getItem("dimensionalType2"));
    useEffect(() => {
        
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              
              
            }),
          };
        fetch("/api/start", requestOptions)
        .then((response) => response.json())
        .then((data) => {
            //acnhors_data= data
            anchorsMap = new Map(Object.entries(JSON.parse(data)))
            acnhors_data= Array.from(anchorsMap);
            setLoading(true)
                //console.log(data)
        });
    },[])


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
                            <h5>Optimization : {optimizationType}</h5>
                            <h5>Strategy : {strategyType}</h5>
                            <h5>Dimensional : {dimensionalType}</h5>    
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
                   {  isLoading && (<Tables acnhors_data={acnhors_data} style={{textAlign:'-webkit-center',}}/>)}
                   { !isLoading && <LoadingDots/>}
                </div>
                
                
            </div>      
      </div>
    );
}

export default FinalResult;
