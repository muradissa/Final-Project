import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import React, { useState,useEffect }  from "react";
import { useNavigate } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import Tables from './Tables';
import Table1d from './Table1d';
import LoadingDots from './Loading'
import { Spinner } from 'react-bootstrap';
//import { MDBSpinner } from 'mdb-react-ui-kit';
//import 'bootstrap/dist/css/bootstrap.min.css';

let anchorsMap = new Map()
let x1 = 0 , y1 = 0;
let acnhors_data;

const FinalResult = () => {
    
    // const navigate = useNavigate();
    const [isLoading, setLoading] = useState(false);
    const [dimensional2d, setDimensional2d] = useState(false);
    const [anchorNumber, setAnchorNumber] = useState(1);
    const [numbersOfAnchors, setNumbersOfAnchors] = useState(localStorage.getItem("numbersOfAnchors"));
    const height = localStorage.getItem("height");
    const width = localStorage.getItem("width");
    const angle = localStorage.getItem("angle");
    const [strategyType] = useState(localStorage.getItem("strategyType2"));
    const [optimizationType] = useState(localStorage.getItem("optimizationType2"));
    const [dimensionalType] = useState(localStorage.getItem("dimensionalType2"));
    const [quality, setQuality] = useState("0");
    
    
    useEffect(() => {  
        if(dimensionalType == '2'){
            setDimensional2d(true)
        }    
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
            }),
          };
        fetch("/api/start", requestOptions)
        .then((response) => response.json())
        .then((data) => {
            anchorsMap = new Map(Object.entries(JSON.parse(data)))
            acnhors_data= Array.from(anchorsMap);
            setLoading(true)
        });
        
    },[])
    useEffect(() => {
        if(isLoading){
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({       
                }),
            };
            fetch("/api/quality", requestOptions)
            .then((response) => response.json())
            .then((data) => {
                setQuality(data)
            });
        }      
    },[isLoading])


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
                            {dimensional2d && 
                                <h5>Width : {width}m</h5> 
                            }
                            <h5>Angle : {angle}<sup style={{color:'white'}}>o</sup></h5> 
                            
                            <h5>I , second moment : 104 </h5>   
                            <h5>E , young modulus : 30 </h5>
                            <h5>C , sand is liquidish : 1 </h5>
                            <h5>V , poisson ratio 0.1 </h5>
                              
                    </div>
                    <div className='row' style={{paddingTop:'20px',textAlign:'center',}}>
                        <h3 style={{color:'white'}}>Cost : <b style={{color:'white'}}>{numbersOfAnchors*2178} $</b></h3>
                        { !isLoading && dimensional2d &&<h3 style={{color:'white'}}>Quality : <b style={{color:'white'}}>Loading..</b></h3>}
                        { isLoading && dimensional2d && <h3 style={{color:'white'}}>Quality : <b style={{color:'white'}}>{quality} %</b></h3>}     
                    </div>                                                  
                </div>
                <div className="col-8 center-Table">
                    {  dimensional2d && (<Tables acnhors_data={acnhors_data} style={{textAlign:'-webkit-center',}}/>)}
                    { !isLoading && <LoadingDots/>}
                    { !dimensional2d && isLoading &&
                        <Table1d acnhors_data={acnhors_data} style={{textAlign:'-webkit-center'}}/>}
                </div>
                
                
            </div>      
      </div>
    );
}

export default FinalResult;
