import React from "react";
import "../../App.css";
import { Container, Paper } from "@material-ui/core";

function PublicLibrary() {

    return (
        <div>
            <h1>
            </h1>
            <Container style={{ paddingTop: "6rem" }}>
                <Paper>
                    <h1>Public Library</h1>
                    <p>I can select a book from the options and add it to my personal list.

                        I can see basic information about each book.
                    </p>
                </Paper>
            </Container>
        </div>
    );
}

export default PublicLibrary;
