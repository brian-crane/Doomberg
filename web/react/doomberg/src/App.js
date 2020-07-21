import React, {useState} from 'react';
import ToDoList from './ToDoList';

function App() {
    const[stocks, addStocks] =  useState(['AAPL','TSLA'])
    return (
        <>
            <ToDoList stocks={stocks}/>
            <input type="text"/>
            <button>Get Stock Details</button>
            <button>Remove Stock from Portfolio</button>
            <button>Add Stock to Portfolio</button>
        </>
    )
}

export default App;