import React, { useState,useEffect }  from "react";
let anchorsMap ;
let anchorsArray;

const Tables = (acnhors_data) => {
    const height2 = localStorage.getItem("height");
    const width2 = localStorage.getItem("width");
    // useEffect(() => {
        
    //   const requestOptions = {
    //       method: "POST",
    //       headers: { "Content-Type": "application/json" },
    //       body: JSON.stringify({  
    //       }),
    //     };
    //   fetch("/api/start", requestOptions)
    //     .then((response) => response.json())
    //     .then((data) => {
    //       //console.log(data)
    //       anchorsMap = new Map(Object.entries(JSON.parse(data)))
    //       anchorsArray= Array.from(anchorsMap);
    //       //console.log(anchorsArray)
    //       console.log("2");
    //     });
    //   },[])

    const rowSequre = (width,height) => {
      // if (localStorage.getItem("data2") !== null && localStorage.getItem("data2") !== undefined){
      //   anchorsMap =new Map(Object.entries(JSON.parse(localStorage.getItem("data2"))))
      //   anchorsArray= Array.from(anchorsMap);
      // }else{

      // }
      //anchorsMap = new Map(Object.entries(JSON.parse(data)))
      //anchorsArray= Array.from(anchorsMap);
      anchorsArray=acnhors_data.acnhors_data
      const exist = anchorsArray.filter(item => {
        item[1].x+1 == 3 && item[1].y+0 == 27
      });
      if(exist.length > 0){
        console.log("pk") 
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

    const fillTheSquare = (x,y) =>{
      
      if (anchorsArray === null || anchorsArray === undefined){
        return <td>x</td>
      }
      
      const exist = anchorsArray.filter(item => 
        ( item[1].x == x &&  item[1].y == y)
      );
      
      const exist4 = anchorsArray.filter(item => {
        3 == x && 27 == y
      });
      if(x==3 ){
       console.log("ok") 
      }
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
        return <td style={{backgroundColor:"green" ,color:"red"}}>xx</td>
      }else if(exist1.length > 0){
        return <td style={{backgroundColor:"yellow" ,color:"yellow"}}>xx</td>
      }else if(exist2.length > 0){
        return <td style={{backgroundColor:"orange" ,color:"orange"}}>xx</td>
      }else if(exist3.length > 0){
        return <td style={{backgroundColor:"orangered" ,color:"orangered"}}>xx</td>
      }
      return <td>xx</td>
    }
    const fillTheSquare2 = (x,y) =>{
      if (anchorsArray === null || anchorsArray === undefined){
        return <td>x</td>
      }
      console.log(anchorsArray);
      const exist = anchorsArray.filter(item => 
        item.x === x && item.y === y
        );
      const exist1 = anchorsArray.filter(item => 
        ( item.x-1 == x &&  item.y == y)||( item.x+1 == x &&  item.y == y)||
        ( item.x == x &&  item.y-1 == y)||( item.x == x &&  item.y+1 == y)||
        ( item.x-1 == x &&  item.y+1 == y)||( item.x+1 == x &&  item.y+1 == y)||
        ( item.x-1 == x &&  item.y-1 == y)||( item.x+1 == x &&  item.y-1 == y)
        );
      const exist2 = anchorsArray.filter(item => 
        ( item.x-2 == x &&  item.y+2 == y)||( item.x-1 == x &&  item.y+2 == y)||
        ( item.x-0 == x &&  item.y+2 == y)||( item.x+1 == x &&  item.y+2 == y)||
        ( item.x+2 == x &&  item.y+2 == y)||( item.x+2 == x &&  item.y+1 == y)||
        ( item.x+2 == x &&  item.y+0 == y)||( item.x+2 == x &&  item.y-1 == y)||
        ( item.x+2 == x &&  item.y-2 == y)||( item.x+1 == x &&  item.y-2 == y)||
        ( item.x+0 == x &&  item.y-2 == y)||( item.x-1 == x &&  item.y-2 == y)||
        ( item.x-2 == x &&  item.y-2 == y)||( item.x-2 == x &&  item.y-1 == y)||
        ( item.x-2 == x &&  item.y+0 == y)||( item.x-2 == x &&  item.y+1 == y)
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
          {rowSequre()}   
        </table>
      </div>
    );
  }
    
  export default Tables;