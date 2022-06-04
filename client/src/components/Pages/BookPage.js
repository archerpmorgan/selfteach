import React from "react";
import "../../App.css";
import { Container, Paper } from "@material-ui/core";

function BookPage() {

    return (
        <div>
            <h1>
            </h1>
            <Container style={{ paddingTop: "6rem" }}>
                <Paper>
                    <h1>[Book Title]</h1>
                    <p>A page with all the data about a single book, including section and problem data in an editable table. I am able to mark sections as studied and problems as completed. Any high level summary question I might want to ask about each book is answerable.

                        I can navigate back.
                    </p>
                </Paper>
            </Container>
        </div>
    );
}

export default BookPage;
