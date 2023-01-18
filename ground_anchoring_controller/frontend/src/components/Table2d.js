import React, { useState,useEffect }  from "react";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Switch from '@mui/material/Switch';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import LoadingDots from './Loading'

let anchorsMap ;
let anchorsArray;
let highMoment=0, default_alpha=0.01, default_beta = 1.0 , default_gamma=0.000001;

const Table2d = (acnhors_data) => {
    const height2 = localStorage.getItem("height");
    const [quality,setQuality] = useState(0);
    const [moment,setMoment] = useState(0);
    let n = localStorage.getItem("numbersOfAnchors");
    const label = { inputProps: { 'aria-label': 'Switch demo' } };
    const [switchButton,setSwitchButton] = useState(true);
    const [img, setImg] = useState();
    const [img2, setImg2] = useState();
    const [img3, setImg3] = useState();
    const [img4, setImg4] = useState();
    const [img5, setImg5] = useState();
    const [img6, setImg6] = useState();
    const [img7, setImg7] = useState();
    const [GraphNum, setGraphNum] = useState("1");


    const fetchImage = async () => {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
        }),
      };
      const res1 = await fetch("/api/plot-moment1",requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setImg(data);
      });
      const res2 = await fetch("/api/plot-moment2",requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setImg2(data);
      });
      const res3 = await fetch("/api/plot-moment3",requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setImg3(data);
      });
      const res4 = await fetch("/api/plot-moment4",requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setImg4(data);
      });
      const res5 = await fetch("/api/plot-moment5",requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setImg5(data);
      });
      const res6 = await fetch("/api/plot-moment6",requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setImg6(data);
      });
      const res7 = await fetch("/api/plot-moment7",requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setImg7(data);
      });
      
    };

    useEffect(() => {  
      const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
          }),
        };
      fetch("/api/high-moment2d", requestOptions)
      .then((response) => response.json())
      .then((data) => {
          highMoment = Math.abs(data);
          setMoment(highMoment)
          calcQulaity();
          fetchImage();
      });
    },[])
  
  const calcQulaity =() => { 
      
      const e = Math.E;
      let res = default_alpha*Math.pow(e,-default_beta*n) + (1-default_alpha)*Math.pow(e,-default_gamma*highMoment);
      res = (res*100.0).toFixed(2);
      setQuality(res) ;
  }

  function handleChangeA(event) {
    var val = parseFloat (event.target.value);
    if( 0.0 <= val && val <=1.0){
      default_alpha = val;
      //setAlpha(val);
      calcQulaity();
    }  
  }
  function handleChangeB(event) {  
    var val = parseFloat (event.target.value);
    if( 0.0 <= val){   
      default_beta = val;
      // setBeta(val);
      calcQulaity();
    }
  }
  function handleChangeC(event) {
    var val = parseFloat (event.target.value);
    if( 0.0 <= val){
      default_gamma = val ;
      //  setGamma(val); 
      calcQulaity();
    }
  }
  const handleSwitchChange = () =>{
    setSwitchButton(!switchButton);
  }

    return (
      <div className="App" >
        {moment != 0 &&
          <div className="row">
            <div className="col-6" >
              <div className="row"  style={{alignItems:"center"}}>
                <div className="radio-btn-container" style={{marginBottom:"0"}}>
                  <div className="radio-btn" onClick={() => { setGraphNum("1");}} style={{
                      background: GraphNum === "1" ? '#0080FF' : '#0891b2'}}>
                      <input type="radio" value={GraphNum} name="optimizationType" checked={GraphNum === "1"}/>
                      W
                  </div>
                  <div className="radio-btn" onClick={() => {setGraphNum("2"); }} style={{
                      background: GraphNum === "2" ? '#0080FF' : '#0891b2'}}>
                      <input type="radio" value={GraphNum} name="optimizationType" checked={GraphNum === "2"} />
                      Wxy
                  </div>
                  <div className="radio-btn" onClick={() => { setGraphNum("3");}} style={{
                      background: GraphNum === "3" ? '#0080FF' : '#0891b2'}}>
                      <input type="radio" value={GraphNum} name="optimizationType" checked={GraphNum === "3"}/>
                      Wxx
                  </div>
                  <div className="radio-btn" onClick={() => { setGraphNum("4");}} style={{
                      background: GraphNum === "4" ? '#0080FF' : '#0891b2'}}>
                      <input type="radio" value={GraphNum} name="optimizationType" checked={GraphNum === "4"}/>
                      Wyy
                  </div>   
                </div>
              </div>
              <div className="row"  style={{alignItems:"center"}}>
                <div className="radio-btn-container" style={{marginBottom:"0"}}>
                  <div className="radio-btn" onClick={() => { setGraphNum("5");}} style={{
                      background: GraphNum === "5" ? '#0080FF' : '#0891b2'}}>
                      <input type="radio" value={GraphNum} name="optimizationType" checked={GraphNum === "5"}/>
                      Mxx
                  </div>
                  <div className="radio-btn" onClick={() => { setGraphNum("6");}} style={{
                      background: GraphNum === "6" ? '#0080FF' : '#0891b2'}}>
                      <input type="radio" value={GraphNum} name="optimizationType" checked={GraphNum === "6"}/>
                      Myy
                  </div>
                  <div className="radio-btn" onClick={() => { setGraphNum("7");}} style={{
                      background: GraphNum === "7" ? '#0080FF' : '#0891b2'}}>
                      <input type="radio" value={GraphNum} name="optimizationType" checked={GraphNum === "7"}/>
                      Mxy
                  </div>      
                </div>
              </div>
              <div className="row">
                
                { GraphNum === "1" &&
                  <div >
                  {/* <img src={img} alt="icons" /> */}
                  <img src={`data:image/jpg;base64,${img}`} style={{width:"100%"}} />
                </div>
                }
                
                { GraphNum === "2" &&
                  <div >
                    {/* <img src={img} alt="icons" /> */}
                    <img src={`data:image/jpg;base64,${img2}`} style={{width:"100%"}} />
                  </div>
                }
                { GraphNum === "3" &&
                  <div >
                    {/* <img src={img} alt="icons" /> */}
                    <img src={`data:image/jpg;base64,${img3}`} style={{width:"100%"}} />
                  </div>
                }
                { GraphNum === "4" &&
                  <div >
                    {/* <img src={img} alt="icons" /> */}
                    <img src={`data:image/jpg;base64,${img4}`} style={{width:"100%"}} />
                  </div>
                }
                { GraphNum === "5" &&
                  <div >
                    {/* <img src={img} alt="icons" /> */}
                    <img src={`data:image/jpg;base64,${img5}`} style={{width:"100%"}} />
                  </div>
                }
                { GraphNum === "6" &&
                  <div >
                    {/* <img src={img} alt="icons" /> */}
                    <img src={`data:image/jpg;base64,${img6}`} style={{width:"100%"}} />
                  </div>
                }
                { GraphNum === "7" &&
                  <div >
                    {/* <img src={img} alt="icons" /> */}
                    <img src={`data:image/jpg;base64,${img7}`} style={{width:"100%"}} />
                  </div>
                }
                
              </div>
            </div>
            <div className="col-6">   
              <div className="row ">  
                <div className="col-12 col-sm-12 col-lg-12  ">
                {/* <h4 style={{color:"white"}}>Quality formula </h4> */}
                <h4 style={{color:"white"}}>Quality : α * e<sup style={{color:"white"}}>-β*n</sup>+(1-α)* e<sup style={{color:"white"}}>-γ*m</sup> </h4>
                <h6 style={{paddingTop:"10px",color:"white"}}>n : number of anchors</h6>
                <h6 style={{color:"white"}}>m : the highest moment = {moment}</h6>  
                    <InputGroup className="mb-3" style={{paddingTop:"10px",width:"200px"}}>
                        <InputGroup.Text id="basic-addon2">α :</InputGroup.Text>
                        <Form.Control  placeholder={default_alpha}  aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeA} />
                    </InputGroup>
                </div>
                <div className="col-12 col-sm-12 col-lg-12">  
                    <InputGroup className="mb-3" style={{width:"200px"}}>
                        <InputGroup.Text id="basic-addon3">β :</InputGroup.Text>
                        <Form.Control placeholder={default_beta}  aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeB} />
                    </InputGroup>
                </div>
                <div className="col-12 col-sm-12 col-lg-12">  
                    <InputGroup className="mb-3" style={{width:"200px"}}>
                        <InputGroup.Text id="basic-addon3">γ :</InputGroup.Text>
                        <Form.Control placeholder={default_gamma}  aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeC} />
                    </InputGroup>
                </div>             
                
                <h3 style={{color:'white',paddingTop:"30px"}}>Quality : <b style={{color:'white' }}>{quality} %</b></h3>
              </div>
            </div>
            
          </div>
        }
        { moment == 0 && 
          <LoadingDots/>
        }
      </div>
    );
  }
    
  export default Table2d;