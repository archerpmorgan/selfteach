import React from "react";
import "../../App.css";
import { Container, Paper } from "@material-ui/core";

function NewProblemSet() {

    return (
        <div>
            <h1>
            </h1>
            <Container style={{ paddingTop: "6rem" }}>
                <Paper>
                    <h1>New Problem Set</h1>
                    <p>
                        I can fill out a form to generate a new problem set according to my specific requirements, including which books the problems will come from, how many, etc. The new problem set appears in my problem sets.
                    </p>
                </Paper>
            </Container>
        </div>
    );
}

export default NewProblemSet;
