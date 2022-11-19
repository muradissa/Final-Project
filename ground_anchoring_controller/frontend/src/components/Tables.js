import React, { useState,useEffect }  from "react";
let anchorsMap ;
let anchorsArray;

const Tables = () => {
    const height2 = localStorage.getItem("height");
    const width2 = localStorage.getItem("width");
    const rowSequre = (width,height) =>{
      anchorsMap =new Map(Object.entries(JSON.parse(localStorage.getItem("data2"))))
      //anchorsMap =localStorage.getItem("data2");
      
      // console.log(anchorsMap.get("1").x);
      anchorsArray= Array.from(anchorsMap);
      // console.log(anchorsArray[0]);
      
      //console.log(localStorage.getItem("data"));
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

    const space ='-';
    const [anchors, setBlogs] = useState([
        { x: 2, y: 2, id: 1 },
        { x: 2, y: 4, id: 2 },
        { x: 2, y: 6, id: 3 },
        { x: 2, y: 8, id: 4 },
        
        { x: 4, y: 2, id: 5 },
        { x: 4, y: 4, id: 6 },
        { x: 4, y: 6, id: 7 },
        { x: 4, y: 8, id: 8 },

        { x: 6, y: 2, id: 9 },
        { x: 6, y: 4, id: 10 },
        { x: 6, y: 6, id: 11 },
        { x: 6, y: 8, id: 12 },

        { x: 8, y: 2, id: 13 },
        { x: 8, y: 4, id: 14 },
        { x: 8, y: 6, id: 15 },
        { x: 8, y: 8, id: 16 },

        { x: 10, y: 2, id: 17 },
        { x: 10, y: 4, id: 18 },
        { x: 10, y: 6, id: 19 },
        { x: 10, y: 8, id: 20 },
              
      ])

    return (
      <div className="App">
        <table style={{ marginLeft:'auto', marginRight:'auto',}}>
         
          {rowSequre(200,30)}
          
        </table>
      </div>
    );
  }
    
  export default Tables;