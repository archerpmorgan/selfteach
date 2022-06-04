import React from "react";
import "../../App.css";
import { Container, Paper } from "@material-ui/core";

function NewPublicLibraryBook() {

    return (
        <div>
            <h1>
            </h1>
            <Container style={{ paddingTop: "6rem" }}>
                <Paper>
                    <h1>Public Library</h1>
                    <p>
                        I can submit a new book to be added to the public library
                    </p>
                </Paper>
            </Container>
        </div>
    );
}

export default NewPublicLibraryBook;
