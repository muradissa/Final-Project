import React, { useState,useEffect }  from "react";
let anchorsMap ;
let anchorsArray;

const Tables = () => {
    const height2 = localStorage.getItem("height");
    const width2 = localStorage.getItem("width");
    const rowSequre = (width,height) =>{
      if (localStorage.getItem("data2") !== null && localStorage.getItem("data2") !== undefined){
        anchorsMap =new Map(Object.entries(JSON.parse(localStorage.getItem("data2"))))
        anchorsArray= Array.from(anchorsMap);
      }else{

      }
      
      let content2 = [];
      for(let y = height2 ; 0 < y; y--){
        let content = [];
        for (let x = 1; x <= width2; x++) {
          //content.push(<td>x</td>);
          content.push(fillTheSquare(x,y));
        }
        content2.push(<tr>{content}</tr>);    
      }
      return content2;
    }

    const fillTheSquare =(x,y) =>{
      if (anchorsArray === null || anchorsArray === undefined){
        return <td>x</td>
      }
      const exist = anchorsArray.filter(item => 
        item[1].x === x && item[1].y === y
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
      if(exist.length > 0){
        return <td style={{backgroundColor:"green" ,color:"blue"}}>x</td>
      }else if(exist1.length > 0){
        return <td style={{backgroundColor:"yellow" ,color:"yellow"}}>x</td>
      }else if(exist2.length > 0){
        return <td style={{backgroundColor:"orange" ,color:"orange"}}>x</td>
      }
      return <td>x</td>
    }
 

    return (
      <div className="App">
        <table style={{ marginLeft:'auto', marginRight:'auto',}}>   
          {rowSequre(200,30)}   
        </table>
      </div>
    );
  }
    
  export default Tables;