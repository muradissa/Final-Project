
import React, { useState,useEffect }  from "react";
import { useNavigate } from "react-router-dom";
import { Button } from 'react-bootstrap';

function simulateNetworkRequest() {
    return new Promise((resolve) => setTimeout(resolve, 500));
}
  
const Home = () => {
    //const { error, isPending, data: blogs } = useFetch('http://localhost:8000/blogs')
    //const { error, isPending, data: blogs } = useFetch('http://localhost:8000/blogs')

    const [strategyType, setTripType] = useState("1");
    const [dimensionalType, setDimensionalType] = useState("1");
    
    const [isLoading, setLoading] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        if (isLoading) {
        simulateNetworkRequest().then(() => {
            setLoading(false);
            localStorage.setItem("strategyType", strategyType);
            localStorage.setItem("dimensionalType", dimensionalType);
            navigate('/parameters');
        });
        }
    }, [isLoading]);

    const handleClick = () => {    
        setLoading(true);
    };

  

  return (
    <div className="home">
       <div className="radio-btn-container" >
            <div className="radio-btn" onClick={() => {setTripType("1"); }} style={{
                background: strategyType === "1" ? '#0080FF' : '#0891b2'}}>
                <input type="radio" value={strategyType} name="strategyType" checked={strategyType === "1"} />
                Manual
            </div>
            <div className="radio-btn" onClick={() => { setTripType("2");}} style={{
                background: strategyType === "2" ? '#0080FF' : '#0891b2'}}>
                <input type="radio" value={strategyType} name="strategyType" checked={strategyType === "2"}/>
                Random
            </div>
            <div className="radio-btn" onClick={() => { setTripType("3");}} style={{
                background: strategyType === "3" ? '#0080FF' : '#0891b2'}}>
                <input type="radio" value={strategyType} name="strategyType" checked={strategyType === "3"}/>
                Machine learning
            </div>
        </div>
        <div className="radio-btn-container" >
            <div className="radio-btn" onClick={() => {setDimensionalType("1"); }} style={{
                background: dimensionalType === "1" ? '#0080FF' : '#0891b2'}}>
                <input type="radio" value={dimensionalType} name="dimensionalType" checked={dimensionalType === "1"} />
                1 Dimensional
            </div>
            <div className="radio-btn" onClick={() => { setDimensionalType("2");}} style={{
                background: dimensionalType === "2" ? '#0080FF' : '#1391b2'}}>
                <input type="radio" value={dimensionalType} name="dimensionalType" checked={dimensionalType === "2"}/>
                2 Dimensional
            </div>
        </div>

        <div className="btn-container">
            <Button className="btn-primary"  disabled={isLoading} onClick={!isLoading ? handleClick : null}>
               {isLoading ? 'Loading…' : 'Click to Start'}
            </Button>
        </div>
    </div>
  );
}
 
export default Home;
