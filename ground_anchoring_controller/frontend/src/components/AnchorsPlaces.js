import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import React, { useState,useEffect }  from "react";
import { useNavigate } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import Tables from './Tables';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

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
function simulateNetworkRequest() {
    return new Promise((resolve) => setTimeout(resolve, 2000));
  }

let anchorsMap = new Map()
let x1 = 0 , y1 = 0;

const AnchorsPlaces = () => {
    
    const navigate = useNavigate();
    const [isLoading, setLoading] = useState(false);
    const [anchorNumber, setAnchorNumber] = useState(1);
    const [numbersOfAnchors, setNumbersOfAnchors] = useState(localStorage.getItem("numbersOfAnchors"));
    const height = localStorage.getItem("height");
    const width = localStorage.getItem("width");
    const angle = localStorage.getItem("angle");
    //using for popup
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

   

    const anchorssRequest =() =>{
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            anchors: convertMapToJsonString(),         
             
          }),
        };
        fetch("/api/create-anchors", requestOptions)
          .then((response) => response.json())
          .then((data) => {
            console.log(data)
            
          });
    }

    const convertMapToJsonString = () => {
        // ✅ Convert to JSON string
        const jsonStr = JSON.stringify(Object.fromEntries(anchorsMap));
        console.log(jsonStr);
        return jsonStr ;      
    }

    useEffect(() => {
        if (isLoading) {
            // if(numbersOfAnchors == anchorsMap.size)
            if(checkAnchorPlacing() && (anchorsMap.size >= numbersOfAnchors-1)){  
                anchorsMap.set(anchorNumber ,{code:anchorNumber,x:x1 , y:y1}) 
                simulateNetworkRequest().then(() => {
                    setLoading(false);
                    //convertMapToJsonString();
                    anchorssRequest();
                    navigate('/finalResult');
                });
            }else{
                setLoading(false);
                setOpen(true);
            }
        }
    }, [isLoading]);


    const handleClick = () => {    
        setLoading(true);
    };

    


    const handleClickNext = ( ) => {
        if(checkAnchorPlacing() ){  
            anchorsMap.set(anchorNumber ,{code:anchorNumber,x:x1 , y:y1}) 
            if(anchorNumber < numbersOfAnchors){ 
                setAnchorNumber(anchorNumber+1);
            }
            if(anchorsMap.get(anchorNumber+1) !== undefined){
                x1 = anchorsMap.get(anchorNumber+1).x;
                y1 = anchorsMap.get(anchorNumber+1).y;
                document.getElementById('FormControl1').value = x1;
                document.getElementById('FormControl2').value = y1;
            }else{
                
                document.getElementById('FormControl1').value = 0;
                document.getElementById('FormControl2').value = 0; 
                x1 =0 ;
                y1=0;
            }
        }else{
            setOpen(true);
        }    
    };


    const handleClickPrevious = ( ) => {
        if(checkAnchorPlacing()){
            anchorsMap.set(anchorNumber ,{code:anchorNumber,x:x1 , y:y1}) 
            if(anchorNumber > 1){
                setAnchorNumber(anchorNumber-1);        
            } 
            if(anchorsMap.get(anchorNumber-1) !== undefined && anchorNumber != 1){
                x1 = anchorsMap.get(anchorNumber-1).x;
                y1 = anchorsMap.get(anchorNumber-1).y;
                document.getElementById('FormControl1').value = x1;
                document.getElementById('FormControl2').value = y1; 
            }
        }else{
            setOpen(true);
        }             
    };


    function handleChangeX(event) {     
        x1 = parseFloat (event.target.value);  
    }


    function handleChangeY(event) {      
        y1 = parseFloat (event.target.value);
    }

    const checkAnchorPlacing = (x,y) =>{
        if( 0 < x1 && x1 <=width && 0 <y1 && y1 <=height){
            return true;
        }else{
            return false;
        }
    }

    return (
      <div className="manually">
            <div className="row">
                <div className="col-12 col-sm-12 col-lg-12">
                    <h2>Anchor {anchorNumber}/{numbersOfAnchors}</h2>                             
                    <div className="row">
                        <div className="col-3">  
                        </div>
                        <div className="col-6">  
                            <InputGroup className="mb-3" >
                                <InputGroup.Text id="basic-addon2">X</InputGroup.Text>
                                <Form.Control id="FormControl1" type="number" placeholder="0" aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeX}>                        
                                </Form.Control>
                            </InputGroup>
                        </div>           
                    </div>
                    <div className="row"> 
                        <div className="col-3">  
                        </div>
                        <div className="col-6">                           
                            <InputGroup className="mb-3" >
                                <InputGroup.Text id="basic-addon4">Y</InputGroup.Text>
                                <Form.Control id="FormControl2" type="number" placeholder="0" aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeY}>  
                                </Form.Control>
                            </InputGroup>
                        </div>                    
                    </div>
                    <div className="row" > 
                    <div className="col-4">  
                        </div>
                        <div className="col-2" style={{float:'right'}}>
                            <button class="btn-anchorP" onClick={(e) => handleClickPrevious()}>
                                Previous
                            </button>  
                        </div>
                        
                        
                        <div className="col-2" style={{float:'left'}}>
                            <button class="btn-anchorP" onClick={(e) => handleClickNext()}>
                                Next
                            </button>   
                        </div>
                       
                    </div>
                </div>
                <div className="col-12 col-sm-12 col-lg-6">
                    {/* <Tables/> */}
                </div>
            </div>
            <div className="btn-container">
                <Button className="btn-primary"  disabled={isLoading} onClick={!isLoading ? handleClick : null}>
                    {isLoading ? 'Loading…' : 'Calaulate'}
                </Button>
            </div>
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
                        * The maximum width is {width}m
                    </Typography>
                    <Typography id="modal-modal-description" sx={{ mt: 1 }} style={{color:"white"}}>
                        * The maximum height is {height}m
                    </Typography>
                    {anchorsMap.size != numbersOfAnchors && 
                        <Typography id="modal-modal-description" sx={{ mt: 1 }} style={{color:"white"}}>
                        * Fill places all the anchors ,You have {numbersOfAnchors-anchorsMap.size} anchors left
                        </Typography>
                    }
                    
                    <Button variant="secondary" style={{float:'right'}} onClick={e => setOpen(false)}>Close</Button>

                </Box>
            </Modal>
      </div>
    );
  }
   
  export default AnchorsPlaces;
