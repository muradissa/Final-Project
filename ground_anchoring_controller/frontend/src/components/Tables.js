import React, { useState,useEffect }  from "react";
let anchorsMap ;
let anchorsArray;

const Tables = (acnhors_data) => {
    const height2 = localStorage.getItem("height");
    const width2 = localStorage.getItem("width");
    

    const rowSequre = (width,height) => {
      
      anchorsArray=acnhors_data.acnhors_data
      
      let content2 = [];
      for(let y = height2 ; 0 < y; y--){
        let content = [];
        for (let x = 1; x <= width2; x++) {
          content.push(fillTheSquare(x,y));
        }
        content2.push(<tr>{content}</tr>);    
      }
      return content2;
    }

    const fillTheSquare = (x,y) =>{
      if (anchorsArray === null || anchorsArray === undefined){
        return <td>x</td>
      }
      const exist = anchorsArray.filter(item => 
        ( item[1].x == x &&  item[1].y == y)
      );    
      
      const exist1 = anchorsArray.filter(item => 
        ( item[1].x-1 == x &&  item[1].y == y)||( item[1].x+1 == x &&  item[1].y == y)||
        ( item[1].x == x &&  item[1].y-1 == y)||( item[1].x == x &&  item[1].y+1 == y)||
        ( item[1].x-1 == x &&  item[1].y+1 == y)||( item[1].x+1 == x &&  item[1].y+1 == y)||
        ( item[1].x-1 == x &&  item[1].y-1 == y)||( item[1].x+1 == x &&  item[1].y-1 == y)
        );
      const exist2 = anchorsArray.filter(item => 
        ( item[1].x-2 == x &&  item[1].y+2 == y)||( item[1].x-1 == x &&  item[1].y+2 == y)||
        ( item[1].x-0 == x &&  item[1].y+2 == y)||( item[1].x+1 == x &&  item[1].y+2 == y)||
        ( item[1].x+2 == x &&  item[1].y+2 == y)||( item[1].x+2 == x &&  item[1].y+1 == y)||
        ( item[1].x+2 == x &&  item[1].y+0 == y)||( item[1].x+2 == x &&  item[1].y-1 == y)||
        ( item[1].x+2 == x &&  item[1].y-2 == y)||( item[1].x+1 == x &&  item[1].y-2 == y)||
        ( item[1].x+0 == x &&  item[1].y-2 == y)||( item[1].x-1 == x &&  item[1].y-2 == y)||
        ( item[1].x-2 == x &&  item[1].y-2 == y)||( item[1].x-2 == x &&  item[1].y-1 == y)||
        ( item[1].x-2 == x &&  item[1].y+0 == y)||( item[1].x-2 == x &&  item[1].y+1 == y)
        );
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
        return <td style={{backgroundColor:"yellow" ,color:"yellow"}}>xxx</td>
      }else if(exist2.length > 0){
        return <td style={{backgroundColor:"orange" ,color:"orange"}}>xxx</td>
      }else if(exist3.length > 0){
        return <td style={{backgroundColor:"orangered" ,color:"orangered"}}>xxx</td>
      }
      return <td style={{backgroundColor:"sienna" ,color:"sienna"}}>xxx</td>
    }
    

    return (
      <div className="App">
        <table style={{ marginLeft:'auto', marginRight:'auto',}}>   
          {rowSequre()}   
        </table>
      </div>
    );
  }
    
  export default Tables;