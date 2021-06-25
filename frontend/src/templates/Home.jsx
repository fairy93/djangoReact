import React,{useEffect} from 'react'
import axios from 'axios'


const Home = ({children}) => { 
    useEffect(()=>{
        axios({
            method: "get",
            url: "http://127.0.0.1:8000/hello",
            responseType: "json"
        }).then(function (response) {
            alert(response.data.greeting)
        });
    },[])
    
    
    return (<>
    <table className="tab_lay">
        <tr><td><h1>Ȩ</h1></td></tr>
        <tr><td><button >���� ���� �׽�Ʈ</button></td></tr>
    </table>
    {children}

</>)}


export default Home
