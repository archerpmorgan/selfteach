import React from "react";
import "../../App.css";
import { Container, Paper } from "@material-ui/core";

function ProblemSet() {

    return (
        <div>
            <h1>
            </h1>
            <Container style={{ paddingTop: "6rem" }}>
                <Paper>
                    <h1>Problem Set</h1>
                    <p>
                        I can see all the individual problems in a set in a table.

                        I can edit the table to mark individual problems as completed, or the whole table as completed.

                        I can remove individual problems from the table.

                        I can "submit" the problem set. This updates the data in the corresponding books to show the problems as completed, and moves the problem set into a completed list somewhere, or deletes it.
                    </p>
                </Paper>
            </Container>
        </div>
    );
}

export default ProblemSet;
