import "../../App.css";
import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { Container, Paper, TextareaAutosize } from "@material-ui/core";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import Tooltip from "@material-ui/core/Tooltip";
import axios from "axios";

function MyLibrary() {

    return (
        <div>
            <h1>
            </h1>
            <Container style={{ paddingTop: "6rem" }}>
                <Paper>
                    <h1>My Library</h1>
                    <p>Here I will be able to view all of my books, I will be able to select books from the public library to add to my collection, and I will be able add a new book to the public library</p>
                    <NewBook />
                </Paper>
            </Container>
        </div>
    );
}


const useToolbarStyles = makeStyles((theme) => ({
    root: {
        paddingLeft: theme.spacing(2),
        paddingRight: theme.spacing(1),
    },
    title: {
        flex: "1 1 100%",
    },
}));

const NewBookToolbar = (props) => {
    const classes = useToolbarStyles();
    const { hasText, handleUpload, image } = props;

    return (
        <Toolbar className={classes.root}>
            {(hasText && image) ? (
                <Tooltip title="Upload">
                    <IconButton
                        className="far fa-save"
                        style={{ color: "blue" }}
                        onClick={handleUpload}
                    />
                </Tooltip>
            ) : (
                <Tooltip title="Input a well-formatted filled-out template into the textarea!">
                    <IconButton
                        className="far fa-times-circle"
                        style={{ color: "red" }}
                        onClick={() => {
                            alert("Input a well-formatted filled-out template into the textarea!");
                        }}
                    />
                </Tooltip>
            )}
        </Toolbar>
    );
};

const useStyles = makeStyles((theme) => ({
    formControl: {
        margin: theme.spacing(1),
        minWidth: 350,
    },
    root: {
        width: "100%",
    },
    paper: {
        width: "100%",
        marginBottom: theme.spacing(2),
    },
    table: {
        minWidth: 750,
    },
    visuallyHidden: {
        border: 0,
        clip: "rect(0 0 0 0)",
        height: 1,
        margin: -1,
        overflow: "hidden",
        padding: 0,
        position: "absolute",
        top: 20,
        width: 1,
    },
    textinput: {
        width: "100%",
    },
}));

function NewBook() {
    const classes = useStyles();
    const [inputText, setInputText] = useState("");
    const [image, setImage] = useState(null);

    const fileSelectedHandler = event => {
        console.log(event.target.files[0]);
        if (event.target.files && event.target.files[0]) {
            setImage(URL.createObjectURL(event.target.files[0]));
        }
    }

    const handleUpload = async () => {
        var inputObject = JSON.parse(inputText);
        const result = axios.post("http://localhost:3001/books/new", inputObject,
            {
                headers: {
                    'content-type': 'application/json'
                }
            }).catch(function (error) {
                if (error.response) {
                    // Request made and server responded
                    console.log(error.response.data);
                    console.log(error.response.status);
                    console.log(error.response.headers);
                } else if (error.request) {
                    // The request was made but no response was received
                    console.log(error.request);
                } else {
                    // Something happened in setting up the request that triggered an Error
                    console.log('Error', error.message);
                };
            });
        console.log(result)
        // window.location.reload();
    };

    const handletextareachange = (event) => {
        setInputText(event.target.value);
    }

    return (
        <Container>
            <h1>Suggest a New Book for the Public Library</h1>
            <h2>Upload a well-formatted template and a cover image and your submission will be reviewed by a service administrator</h2>
            <div className="App mt-4">
                <div className={classes.root}>
                    <Paper className={classes.paper}>
                        <NewBookToolbar
                            hasText={inputText.length > 0}
                            handleUpload={handleUpload}
                            image={image}
                        />
                        <TextareaAutosize
                            className={classes.textinput}
                            rowsMin={5}
                            aria-label="maximum height"
                            onChange={handletextareachange}
                        />
                        <input type="file" onChange={fileSelectedHandler} />
                        {image ?
                            <img src={image} alt="preview image" /> :
                            <></>
                        }
                    </Paper>
                </div>
            </div>
        </Container>
    );
}


export default MyLibrary;
