import React from "react";
import "../../App.css";
import { Container, Paper } from "@material-ui/core";

function About() {

    return (
        <div>
            <h1>
            </h1>
            <Container style={{ paddingTop: "6rem" }}>
                <Paper>
                <h1>Selfteach About</h1>
                <p>Selfteach is a web app for helping me learn and practice with technical textbooks.</p>
                </Paper>
            </Container>
        </div>
    );
}

export default About;
