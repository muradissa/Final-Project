import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import React, { useState,useEffect }  from "react";
import { useNavigate } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import WarningPopup from './WarningPopup'
// import * as React from 'react';
import Box from '@mui/material/Box';
// import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';


function simulateNetworkRequest() {
    return new Promise((resolve) => setTimeout(resolve, 500));
}
const Parameters = () => {
    const [dimensionalType, setDimensionalType] = useState(localStorage.getItem("dimensionalType2"));
    const [isLoading, setLoading] = useState(false);
    // const [isLoading2, setLoading2] = useState(false);
    const [dimensional2d, setDimensional2d] = useState(false);
    const navigate = useNavigate();
    const [anchorsPara] =useState({
        numbersOfAnchors:0,
        v:0.0,
        c:0.0,
        e:0,
        i:0
    });
    const [wallPara]= useState({
        height:0,
        width:0 ,
        angle:0 
    });

    useEffect(() => {
        if(dimensionalType == '2'){
            setDimensional2d(true)
        }
    },[]);


    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const style = {
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 400,
        bgcolor: 'background.paper',
        border: '3px solid #ff0000',
        borderRadius:'15px',
        boxShadow: 24,
        p: 4,
      };

      async function wallParametersRequest () {
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            height: wallPara.height, 
            width: wallPara.width,
            angle: wallPara.angle,
            number_of_anchors: anchorsPara.numbersOfAnchors ,
          }),
        };
        await fetch("/api/create-wall", requestOptions)
          .then((response) => response.json())
          .then((data) => {
            // setLoading2(true)
            console.log(data)
        });
    }

    function checkValues(){
        console.log("checkValues");
        if(anchorsPara.numbersOfAnchors >= 0 && anchorsPara.numbersOfAnchors <= 100 && 
            wallPara.height <= 30 && wallPara.height > 0 &&
            wallPara.width <= 150 && wallPara.width > 0 &&
            wallPara.angle >= 90 && wallPara.angle <= 150){
                wallParametersRequest();
                return true;        
        }
        
        setOpen(true);
        return false;
    }

    useEffect(() => {
        if (isLoading) {
            simulateNetworkRequest().then(() => {
                setLoading(false);
                if(checkValues())
                    if(enterTheAnchorsManaul()){
                        navigate('/anchorsPlaces');
                    }else{
                        navigate('/finalResult');
                    }
                    
                else
                    console.log("Wrong parameters");
            });
        }
        if (dimensionalType == '1'){
            if(wallPara.angle !=90){
                localStorage.setItem("angle", wallPara.angle);
            }else{
                document.getElementById('FormControlAngel').value = '90';
                wallPara.angle=90;
                localStorage.setItem("angle", wallPara.angle);
            }
              
        }
        

    }, [isLoading]);

    const handleClick = () => {
        console.log('handleClick');    
        setLoading(true);
        // setLoading2(true);
    };

    function handleChangeNumberOfAnchors(event) {        
        anchorsPara.numbersOfAnchors = +event.target.value ;
        localStorage.setItem("numbersOfAnchors", anchorsPara.numbersOfAnchors);    
    }

    function handleChangeV(event) {    
        anchorsPara.v = parseFloat(event.target.value);
    }

    function handleChangeC(event) {
        anchorsPara.c = parseFloat(event.target.value);
    }

    function handleChangeE(event) {
        anchorsPara.e = parseFloat(event.target.value);
    }
    function handleChangeI(event) {
        anchorsPara.i = parseFloat(event.target.value);
    }
    function handleChangeHeight(event) {
        wallPara.height = parseFloat (event.target.value);
        localStorage.setItem("height", wallPara.height); 
        if(!dimensional2d){
            wallPara.width = 2.0
        } 
    }
    function handleChangeWidth(event) {   
        wallPara.width = parseFloat (event.target.value);
        localStorage.setItem("width", wallPara.width);  
    }
    function handleChangeAngle(event) {
        wallPara.angle = parseFloat (event.target.value);
        localStorage.setItem("angle", wallPara.angle);  
    }

    const enterTheAnchorsManaul = () =>{      
        if(localStorage.getItem("strategyType") === "1"){
            return true;
        }else{
            return false;
        }
    }
    

    return (
      <div className="manually">
            <div className="row">
                <div className="col-12 col-sm-12 col-lg-2" ></div>
                <div className="col-12 col-sm-12 col-lg-3" >
                    <h2 className="anchors-parameters" style={{ justifyContent:'center',textAlign:'center'}}>
                        Anchors parameters
                    </h2>                    
                    <InputGroup className="mb-3" >
                        <InputGroup.Text className="input-group-text" id="basic-addon1">Number of anchors</InputGroup.Text>
                        <Form.Control type="number" placeholder="0-100" aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeNumberOfAnchors} />
                    </InputGroup>
                    <div className="row ">  
                        


                        <div className="col-12 col-sm-12 col-lg-12">  
                            <InputGroup className="mb-3" >
                                <InputGroup.Text id="basic-addon3">C : sand is liquidish</InputGroup.Text>
                                <Form.Control placeholder="1" value="1" aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeC} />
                            </InputGroup>
                        </div>
                        <div className="col-12 col-sm-12 col-lg-12">  
                            <InputGroup className="mb-3" >
                                <InputGroup.Text id="basic-addon4">E : young modulus</InputGroup.Text>
                                <Form.Control placeholder="30" value="30" aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeE}/>
                            </InputGroup>
                        </div>
                    </div>
                    <div className="row justify-content-sm-between"> 
                        
                        <div className="col-12 col-sm-12 col-lg-12">  
                            <InputGroup className="mb-3">
                                <InputGroup.Text id="basic-addon5">I : second moment</InputGroup.Text>
                                <Form.Control placeholder="104" value="104" aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeI}/>
                            </InputGroup>
                        </div>
                        <div className="col-12 col-sm-12 col-lg-12  ">  
                            <InputGroup className="mb-3" >
                                <InputGroup.Text id="basic-addon2">V : poisson ratio</InputGroup.Text>
                                <Form.Control  placeholder="0.1" value="0.1" aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeV} />
                            </InputGroup>
                        </div>
                    </div>
                </div>
                {/* <div className="col-1"></div> */}
                <div className="col-12 col-sm-12 col-lg-1" ></div>
                <div className="col-12 col-sm-12 col-lg-5 wall-parameters">   
                    <h2>Wall parameters</h2>
                    <div className="row">   
                       <div className="col-12">
                            <InputGroup className="mb-3" >
                                <InputGroup.Text id="basic-addon6">Height( m )</InputGroup.Text>
                                <Form.Control type="number" placeholder="maximum 30m" aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeHeight}/>
                            </InputGroup>
                        </div>
                    </div>
                    {dimensional2d &&
                        <div className="row"> 
                            <div className="col-12">     
                                <InputGroup className="mb-3" >
                                    <InputGroup.Text id="basic-addon7">Width ( m )</InputGroup.Text>
                                    <Form.Control  type="number" placeholder="maximum 150m" aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeWidth}/>
                                </InputGroup>
                            </div>
                        </div>
                    }
                    <div className="row"> 
                        <div className="col-12">  
                    
                            <InputGroup className="mb-3" >
                                <InputGroup.Text id="basic-addon8">Angle(Rad)</InputGroup.Text>
                                <Form.Control id="FormControlAngel" type="number" placeholder="90 - 150" aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeAngle}/>
                            </InputGroup>
                        </div>
                    </div>
                </div>
               
            </div>
            <div className="btn-container">
                <Button className="btn-primary"  disabled={isLoading} onClick={!isLoading ? handleClick : null}>
                    {isLoading ? 'Loading…' : 'Click to Start'}
                </Button>
            </div>
            {/* <WarningPopup/> */}
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
                >
                    
                <Box sx={style} style={{backgroundColor:"mediumpurple"}}>
                    
                    <Typography id="modal-modal-title" variant="h6" component="h2">
                        Wrong Parameters !
                    </Typography>
                    <Typography id="modal-modal-description" sx={{ mt: 1 }} style={{color:"white"}}>
                        * The maximum number of anchors is 100
                    </Typography>
                    <Typography id="modal-modal-description" sx={{ mt: 1 }} style={{color:"white"}}>
                        * The maximum height is 30m
                    </Typography>
                    <Typography id="modal-modal-description" sx={{ mt: 1 }} style={{color:"white"}}>
                        * The maximum width is 150m
                    </Typography>
                    <Typography id="modal-modal-description" sx={{ mt: 1 }} style={{color:"white"}}>
                        * Angle should be betwen 90-150
                    </Typography>
                    <Button variant="secondary" style={{float:'right'}} onClick={e => setOpen(false)}>Close</Button>

                </Box>
            </Modal>
        </div>
    );
  }
   
  export default Parameters;