import React from 'react'
import Stock from './Stock';


export default function ToDoList({ stocks }) {
    return (

            stocks.map(stock => {
                return <Stock stock={stock} />
            })
    )
}