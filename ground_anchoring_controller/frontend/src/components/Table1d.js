import React, { useState,useEffect }  from "react";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Switch from '@mui/material/Switch';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';

let anchorsMap ;
let anchorsArray;
let highMoment=0, default_alpha=0.01, default_beta = 1.0 , default_gamma=0.000001;

const Table1d = (acnhors_data) => {
    const height2 = localStorage.getItem("height");
    const [quality,setQuality] = useState(0);
    const [moment,setMoment] = useState(0);
    let n = localStorage.getItem("numbersOfAnchors");
    const label = { inputProps: { 'aria-label': 'Switch demo' } };
    const [switchButton,setSwitchButton] = useState(true);
    const [img, setImg] = useState();
    const [img2, setImg2] = useState();
    const [GraphNum, setGraphNum] = useState("1");


    const fetchImage = async () => {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
        }),
      };
      const res = await fetch("/api/plot-moment",requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setImg(data);
      });
      const res2 = await fetch("/api/plot-moment-numerical",requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setImg2(data);
      });
    };

    useEffect(() => {  
      const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
          }),
        };
      fetch("/api/high-moment", requestOptions)
      .then((response) => response.json())
      .then((data) => {
          highMoment = Math.abs(data);
          setMoment(highMoment)
          calcQulaity();
          fetchImage();
      });
    },[])
  
    const rowSequre = (width,height) => {
      
      anchorsArray=acnhors_data.acnhors_data
      let content2 = [];
      for(let y = height2 ; 0 < y; y--){
        let content = [];
        for (let x = 0; x < 3; x++) {
          content.push(fillTheSquare(x,y));
        }
        content2.push(<tr>{content}</tr>);    
      }
      let content = [];
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xxx</td>);
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xxx</td>);
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xxx</td>);
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xxx</td>);
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xxx</td>);
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xxx</td>);
      content2.push(<tr>{content}</tr>); 
      return content2;
    }

    const fillTheSquare = (x,y) =>{
      
      if (anchorsArray === null || anchorsArray === undefined){
        return <td style={{backgroundColor:"sienna" ,color:"sienna"}}>xxx</td>
      }
      // console.log(anchorsArray)
      const exist = anchorsArray.filter(item => 
        ( item[1].x == x &&  Math.round(item[1].y) == y)
      );    

      const exist1 = anchorsArray.filter(item => 
        ( item[1].x+1 == x &&  Math.round(item[1].y) == y));
      const exist2 = anchorsArray.filter(item => 
        ( item[1].x+2 == x &&  Math.round(item[1].y) == y));
      const exist3 = anchorsArray.filter(item => 
        ( item[1].x-3 == x &&  item[1].y+3 == y)||( item[1].x-2 == x &&  item[1].y+3 == y)||
        ( item[1].x-1 == x &&  item[1].y+3 == y)||( item[1].x+0 == x &&  item[1].y+3 == y)||
        ( item[1].x+1 == x &&  item[1].y+3 == y)||( item[1].x+2 == x &&  item[1].y+3 == y)||
        ( item[1].x+3 == x &&  item[1].y+3 == y)||( item[1].x+3 == x &&  item[1].y+2 == y)||
        ( item[1].x+3 == x &&  item[1].y+1 == y)||( item[1].x+3 == x &&  item[1].y+0 == y)||
        ( item[1].x+3 == x &&  item[1].y-1 == y)||( item[1].x+3 == x &&  item[1].y-2 == y)||
        ( item[1].x+3 == x &&  item[1].y-3 == y)||( item[1].x+2 == x &&  item[1].y-3 == y)||  
        ( item[1].x+1 == x &&  item[1].y-3 == y)||( item[1].x+0 == x &&  item[1].y-3 == y)||
        ( item[1].x-1 == x &&  item[1].y-3 == y)||( item[1].x-2 == x &&  item[1].y-3 == y)||
        ( item[1].x-3 == x &&  item[1].y-3 == y)||( item[1].x-3 == x &&  item[1].y-2 == y)||
        ( item[1].x-3 == x &&  item[1].y-1 == y)||( item[1].x-3 == x &&  item[1].y+0 == y)||
        ( item[1].x-3 == x &&  item[1].y+1 == y)||( item[1].x-3 == x &&  item[1].y+2 == y)

        );  
      
      if(exist.length > 0){
        return <td style={{backgroundColor:"green" ,color:"green"}}>xxx</td>
      }else if(exist1.length > 0){
        let found ,foundy;
        found = anchorsArray.find(element =>  Math.round(element[1].y) == y);   
        foundy = found[1].y.toFixed(1);
        return <td style={{backgroundColor:"sienna" , color:"white",textAlign:"center"}}>{foundy}</td>
      }else if(exist2.length > 0){
        return <td style={{backgroundColor:"sienna" ,color:"white"}}>m</td>
      }else if(exist3.length < 0){
        return <td style={{backgroundColor:"orangered" ,color:"orangered"}}>xxx</td>
      }
      return <td style={{backgroundColor:"sienna" ,color:"sienna"}}>xxx</td>
    }
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
        <div className="row">
          <div className="col-6" >
            {/* <div className="row"  style={{ marginLeft:'35%',alignItems:"center"}}>
              <div >
                <Stack direction="row" spacing={1} alignItems="center" size="lg" style={{ padding:"5px",paddingLeft:"00px"}} >
                  <Typography style={{color:"white"}}>Plot</Typography>
                  <Switch {...label} defaultChecked size="medium"  onChange={handleSwitchChange}/>
                  <Typography style={{color:"white"}}>Wall</Typography>
                </Stack> 
              </div>
            </div> */}
            <div className="row"  style={{alignItems:"center"}}>
                <div className="radio-btn-container" style={{marginBottom:"0"}}>
                  <div className="radio-btn" onClick={() => { setGraphNum("1");}} style={{
                      background: GraphNum === "1" ? '#0080FF' : '#0891b2'}}>
                      <input type="radio" value={GraphNum} name="optimizationType" checked={GraphNum === "1"}/>
                      Wall
                  </div>
                  <div className="radio-btn" onClick={() => {setGraphNum("2"); }} style={{
                      background: GraphNum === "2" ? '#0080FF' : '#0891b2'}}>
                      <input type="radio" value={GraphNum} name="optimizationType" checked={GraphNum === "2"} />
                      Analytic
                  </div>
                  <div className="radio-btn" onClick={() => { setGraphNum("3");}} style={{
                      background: GraphNum === "3" ? '#0080FF' : '#0891b2'}}>
                      <input type="radio" value={GraphNum} name="optimizationType" checked={GraphNum === "3"}/>
                      Numerical
                  </div>
                </div>
              </div>
            <div className="row">
              { GraphNum === '1' &&
                <div className="col-7" >
                  <table style={{ marginLeft:'auto', marginRight:'auto',}}>
                    {rowSequre()}   
                  </table>
                </div>
              }
              { GraphNum === '1' &&
                <div className="col-4" style={{ alignItems:"center",paddingTop:"50px"}}>
                    <div style={{ padding:"6px",border: '2px solid #ccc',borderRadius:'15px' }}>
                      <div style={{padding:"2px",backgroundColor:"green" ,color:"white",textAlign:"center",borderRadius:'10px'}}>Anchor</div>
                      <div style={{padding:"2px",backgroundColor:"sienna" ,color:"white",textAlign:"center",borderRadius:'10px'}}>Wall</div>
                      <div style={{padding:"2px",backgroundColor:"black" ,color:"white",textAlign:"center",borderRadius:'10px'}}>Ground</div>  
                    </div>          
                </div>
              }
              
              { GraphNum === '2' &&
                <div >
                  {/* <img src={img} alt="icons" /> */}
                  <img src={`data:image/jpg;base64,${img}`} style={{width:"100%"}} />
                </div>
              }
              { GraphNum === '3' &&
                <div >
                  {/* <img src={img} alt="icons" /> */}
                  <img src={`data:image2/jpg;base64,${img2}`} style={{width:"100%"}} />
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
        
      </div>
    );
  }
    
  export default Table1d;