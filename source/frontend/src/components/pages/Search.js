import React from 'react'
import Button from 'react-bootstrap/esm/Button'
import { connectWithAPI } from '../API/IGDB.js' 

function Search() {
    return (
        <>
            <Button onClick={connectWithAPI}>Testar conexão com API</Button>
        </>
    )
}

export default Search
