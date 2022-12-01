import React, { useState,useEffect }  from "react";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
let anchorsMap ;
let anchorsArray;

const Table1d = (acnhors_data) => {
    const height2 = localStorage.getItem("height");
  
    const rowSequre = (width,height) => {
      
      anchorsArray=acnhors_data.acnhors_data
      console.log(anchorsArray)
      let content2 = [];
      for(let y = height2 ; 0 < y; y--){
        let content = [];
        for (let x = 0; x < 3; x++) {
          content.push(fillTheSquare(x,y));
        }
        content2.push(<tr>{content}</tr>);    
      }
      let content = [];
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xx</td>);
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xx</td>);
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xx</td>);
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xx</td>);
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xx</td>);
      content.push(<td style={{backgroundColor:"black" ,color:"black"}}>xx</td>);
      content2.push(<tr>{content}</tr>); 
      return content2;
    }

    const fillTheSquare = (x,y) =>{
      if (anchorsArray === null || anchorsArray === undefined){
        return <td style={{backgroundColor:"sienna" ,color:"sienna"}}>xx</td>
      }
      const exist = anchorsArray.filter(item => 
        ( item[1].x == x &&  item[1].y == y)
      );    
      
      const exist1 = anchorsArray.filter(item => 
        ( item[1].x+1 == x &&  item[1].y == y));
      const exist2 = anchorsArray.filter(item => 
        ( item[1].x+2 == x &&  item[1].y == y));
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
        return <td style={{backgroundColor:"green" ,color:"green"}}>xx</td>
      }else if(exist1.length > 0){
        return <td style={{backgroundColor:"sienna" , color:"white",textAlign:"center"}}>{y}</td>
      }else if(exist2.length > 0){
        return <td style={{backgroundColor:"sienna" ,color:"white"}}>m</td>
      }else if(exist3.length < 0){
        return <td style={{backgroundColor:"orangered" ,color:"orangered"}}>xx</td>
      }
      return <td style={{backgroundColor:"sienna" ,color:"sienna"}}>xx</td>
    }

    function handleChangeA(event) {
      wallPara.height = parseFloat (event.target.value);
      localStorage.setItem("alpha", wallPara.height);  
  }
  function handleChangeB(event) {   
      wallPara.width = parseFloat (event.target.value);
      localStorage.setItem("Beta", wallPara.width);  
  }
  function handleChangeC(event) {
      wallPara.angle = parseFloat (event.target.value);
      localStorage.setItem("Gamma", wallPara.angle);  
  }
    
    return (
      <div className="App" >
        <div className="row">
          <div className="col-6">
            
            <div className="row ">  
              <div className="col-12 col-sm-12 col-lg-12  ">
              {/* <h4 style={{color:"white"}}>Quality formula </h4> */}
              <h4 style={{color:"white"}}>Quality formula= α * e<sup style={{color:"white"}}>-β*n</sup>+(1-α)* e<sup style={{color:"white"}}>-γ*m</sup> </h4>  
                  <InputGroup className="mb-3" style={{paddingTop:"30px"}}>
                      <InputGroup.Text id="basic-addon2">α :</InputGroup.Text>
                      <Form.Control  placeholder="0.5"  aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeA} />
                  </InputGroup>
              </div>
              <div className="col-12 col-sm-12 col-lg-12">  
                  <InputGroup className="mb-3" >
                      <InputGroup.Text id="basic-addon3">β :</InputGroup.Text>
                      <Form.Control placeholder="1"  aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeB} />
                  </InputGroup>
              </div>
              <div className="col-12 col-sm-12 col-lg-12">  
                  <InputGroup className="mb-3" >
                      <InputGroup.Text id="basic-addon3">γ :</InputGroup.Text>
                      <Form.Control placeholder="1"  aria-label="numbers" aria-describedby="basic-addon1" onChange={handleChangeC} />
                  </InputGroup>
              </div>
              
              <h6 style={{paddingTop:"30px",color:"white"}}>n : number of anchors</h6>
              <h6 style={{color:"white"}}>m : the weakest moment</h6>
            </div>
          </div>
          <div className="col-4" >
            <table style={{ marginLeft:'auto', marginRight:'auto',}}>   
              {rowSequre()}   
            </table>

            
          </div>
          <div className="col-2">
              <div style={{ padding:"6px",border: '2px solid #ccc',borderRadius:'15px'}}>
                <div style={{padding:"2px",backgroundColor:"green" ,color:"white",textAlign:"center",borderRadius:'10px'}}>Anchor</div>
                <div style={{padding:"2px",backgroundColor:"sienna" ,color:"white",textAlign:"center",borderRadius:'10px'}}>Wall</div>
                <div style={{padding:"2px",backgroundColor:"black" ,color:"white",textAlign:"center",borderRadius:'10px'}}>Ground</div>  
              </div>
               
          </div>
        </div>
      </div>
    );
  }
    
  export default Table1d;