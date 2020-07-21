import React from 'react';
import Form from 'react';

const HelloWorld = () => {
    async function getUsers() {
        let url = 'http://localhost:5001/userInfo?userId=1';
        try {
            let res = await fetch(url);
            alert(await res.json());
        } catch (error) {
            console.log(error);
        }
    }

    return (
        <button onClick={getUsers}>Get Users</button>
    );
};

export default HelloWorld;