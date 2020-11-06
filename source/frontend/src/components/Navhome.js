import React, { useState } from 'react';
import Navbar from 'react-bootstrap/Navbar';
import { FaGamepad, FaTimes, FaBars } from 'react-icons/fa';
import './Navhome.css'

function Navhome() {
    return (
        <>
            <Navbar className="purple" variant="dark" sticky="top">
                <Navbar.Brand href="#home">
                    <FaGamepad size={30}/>
                    &nbsp; GamingTrack
                </Navbar.Brand>
                <Nav className="mr-auto">
                    <Nav.Link href="#home">Home</Nav.Link>
                </Nav>
            </Navbar>
        </>
    )
}

export default Navhome
