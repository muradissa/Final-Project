import React, { useState,useEffect }  from "react";
const Tables = () => {
    const height2 = localStorage.getItem("height");
    const width2 = localStorage.getItem("width");
    const rowSequre = (width,height) =>{       
      
      let content2 = [];

      for(let y = 0 ; y < height2; y++){
        let content = [];
        for (let x = 0; x < width2; x++) {
          content.push(<td>x</td>);
        }
        content2.push(<tr>{content}</tr>);
      
      }
      return content2;
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