import React, { useState } from 'react'
import Button from 'react-bootstrap/esm/Button'
import Col from 'react-bootstrap/esm/Col'
import Container from 'react-bootstrap/esm/Container'
import Row from 'react-bootstrap/esm/Row'
import Form from 'react-bootstrap/Form'
import InputGroup from 'react-bootstrap/InputGroup'
import { FaGamepad } from 'react-icons/fa'
import { Link } from 'react-router-dom'
import Navhome from '../Navhome'
import './Register.css'

function Register() {
    const [validated, setValidated] = useState(false);

    const handleSubmit = (event) => {
      const form = event.currentTarget;
      if (form.checkValidity() === false) {
        event.preventDefault();
        event.stopPropagation();
      }
  
      setValidated(true);
    };
    
    return (
        <>
            <Navhome />
            <Container fluid="true">
               <Row className="justify-content-md-center">
                    <div className="register-box">
                        <div className="title">
                            <h2 className="title">Crie sua Conta</h2>
                        </div>
                        <Form>
                            <Form.Group>
                                <Form.Label>Nome Completo</Form.Label>
                                <Form.Control type="text" placeholder="Insira seu nome" />
                            </Form.Group>
                            <Form.Group>
                                <Form.Label>E-mail</Form.Label>
                                <Form.Control type="email" placeholder="Insira seu e-mail" />
                            </Form.Group>
                            <Form.Group>
                                <Form.Label>Login</Form.Label>
                                <Form.Control type="text" placeholder="Escolha um nome de usuário" />
                            </Form.Group>
                            <Form.Group>
                                <Form.Label>Senha</Form.Label>
                                <Form.Control type="password" placeholder="Insira sua senha" />
                            </Form.Group>
                            <Form.Group>
                                <Form.Label>Confirme a sua senha</Form.Label>
                                <Form.Control type="password" placeholder="Repita a sua senha" />
                            </Form.Group>
                            <Form.Group>
                                <Form.Check type="checkbox" label="Concordo com os termos e condições de uso." />
                            </Form.Group>
                            <Button className="bttn btn--submit blue">
                                Cadastrar
                            </Button>
                        </Form>
                    </div>
               </Row>
            </Container>
        </>
    )
}

export default Register
