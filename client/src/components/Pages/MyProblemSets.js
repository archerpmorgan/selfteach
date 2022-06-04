import React from "react";
import "../../App.css";
import { Container, Paper } from "@material-ui/core";

function MyProblemSets() {

    return (
        <div>
            <h1>
            </h1>
            <Container style={{ paddingTop: "6rem" }}>
                <Paper>
                    <h1>Problem Sets</h1>
                    <p>
                        I can see a list of my problem sets in progress and summary metadata/visualization. I can click on any one of them and see the problem set page.
                    </p>
                </Paper>
            </Container>
        </div>
    );
}

export default MyProblemSets;
