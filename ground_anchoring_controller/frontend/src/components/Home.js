
import React, { useState,useEffect }  from "react";
import { useNavigate } from "react-router-dom";
import { Button } from 'react-bootstrap';

function simulateNetworkRequest() {
    return new Promise((resolve) => setTimeout(resolve, 500));
}
  
const Home = () => {
    const [strategyType, setStrategyType] = useState("1");
    const [optimizationType, setOptimizationType] = useState("1");
    const [dimensionalType, setDimensionalType] = useState("1");
    const [isLoading, setLoading] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        if (isLoading) {
        simulateNetworkRequest().then(() => {
            setLoading(false);
            localStorage.setItem("strategyType", strategyType);
            localStorage.setItem("dimensionalType", dimensionalType);
            localStorage.setItem("optimizationType", optimizationType);
            fillTypes();
            typeParametersRequest();
            navigate('/parameters');
        });
        }
    }, [isLoading]);

    const handleClick = () => {    
        setLoading(true);
    };

    const fillTypes = () => {
        const optimization_method = localStorage.getItem("optimizationType");
        const anchor_placing = localStorage.getItem("strategyType");
        const dimensional_type = localStorage.getItem("dimensionalType");
        if(optimization_method == 1){
            localStorage.setItem("optimizationType2", "No optimization"); 
        }else if(optimization_method == 2){           
            localStorage.setItem("optimizationType2", "Gradient descent"); 
        }else if(optimization_method == 3){            
            localStorage.setItem("optimizationType2", "Q-learning"); 
        }else if(optimization_method == 4){           
            localStorage.setItem("optimizationType2", "Artifical annealing"); 
        }      
        if(anchor_placing == 1){
            localStorage.setItem("strategyType2", "Manually");
        }else if(anchor_placing == 2){           
            localStorage.setItem("strategyType2", "Equal distance");
        }else if(anchor_placing == 3){            
            localStorage.setItem("strategyType2", "Monte Carlo");
        }
        if(dimensional_type == 1){
            localStorage.setItem("dimensionalType2", "1");
        }else if(dimensional_type == 2){           
            localStorage.setItem("dimensionalType2", "2");
        }             
    }
    const typeParametersRequest =() =>{
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            strategyType: strategyType,         
            dimensionalType: dimensionalType,
            optimizationType: optimizationType,
            
          }),
        };
        fetch("/api/enter-parameter", requestOptions)
          .then((response) => response.json())
          .then((data) => console.log(data));
    }
  
    return (
        <div className="home">
            <div className="radio-btn-container" >
                <div className="radio-btn" onClick={() => { setOptimizationType("1");}} style={{
                    background: optimizationType === "1" ? '#0080FF' : '#0891b2'}}>
                    <input type="radio" value={optimizationType} name="optimizationType" checked={optimizationType === "1"}/>
                    No optimization
                </div>
                <div className="radio-btn" onClick={() => {setOptimizationType("2"); }} style={{
                    background: optimizationType === "2" ? '#0080FF' : '#0891b2'}}>
                    <input type="radio" value={optimizationType} name="optimizationType" checked={optimizationType === "2"} />
                    Gradient descent 
                </div>
                <div className="radio-btn" onClick={() => { setOptimizationType("3");}} style={{
                    background: optimizationType === "3" ? '#0080FF' : '#0891b2'}}>
                    <input type="radio" value={optimizationType} name="optimizationType" checked={optimizationType === "3"}/>
                    Q-learning
                </div>
                <div className="radio-btn" onClick={() => { setOptimizationType("4");}} style={{
                    background: optimizationType === "4" ? '#0080FF' : '#0891b2'}}>
                    <input type="radio" value={optimizationType} name="optimizationType" checked={optimizationType === "4"}/>
                    Artifical annealing
                </div>      
            </div>

        <div className="radio-btn-container" >
                <div className="radio-btn" onClick={() => {setStrategyType("1"); }} style={{
                    background: strategyType === "1" ? '#0080FF' : '#0891b2'}}>
                    <input type="radio" value={strategyType} name="strategyType" checked={strategyType === "1"} />
                    Manually
                </div>
                <div className="radio-btn" onClick={() => { setStrategyType("2");}} style={{
                    background: strategyType === "2" ? '#0080FF' : '#0891b2'}}>
                    <input type="radio" value={strategyType} name="strategyType" checked={strategyType === "2"}/>
                    Equal distance
                </div>
                <div className="radio-btn" onClick={() => { setStrategyType("3");}} style={{
                    background: strategyType === "3" ? '#0080FF' : '#0891b2'}}>
                    <input type="radio" value={strategyType} name="strategyType" checked={strategyType === "3"}/>
                    Monte Carlo
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
