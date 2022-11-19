import React, {Component,useState,useEffect} from "react";
import {render} from "react-dom";
import Navbar from './Navbar';
import Home from './Home';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Parameters from './Parameters';
// import 'bootstrap/dist/css/bootstrap.min.css'; 
import AnchorsPlaces from './AnchorsPlaces';
import FinalResult from "./FinalResult";
// import useFetch from "./useFetch";

export default class App extends Component{
    constructor(props){
        super(props);
    }
    
    render(){
        return (     
            <Router >
                <div className="App">
                    <div className="nav-bar">
                        <Navbar />
                    </div>
                    
                    <div className="content">
                        <Routes>
                            <Route exact path="" element={<Home/>}> </Route>
                            <Route exact path="/" element={<Home/>}> </Route>
                            <Route path="/parameters" element={<Parameters/>}> </Route>
                            <Route path="/anchorsPlaces" element={<AnchorsPlaces/>}> </Route>
                            <Route path="/finalResult" element={<FinalResult/>}> </Route>
                        </Routes>
                    </div>
                    <div class="area" >
                        <ul class="circles">
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div >
                </div>
               
            </Router>         
        );
    }
}

const appDiv =document.getElementById("app");
render(<App/>,appDiv);
// { error && <div>{ error }</div> }
// { isPending && <div>Loading...</div> } 