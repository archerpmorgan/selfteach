import { Schema, model } from "mongoose";
import Section from "./Section";

/*
{
Data schema for v1

    "title": "Calculus Single and Multivariable",
    "subject": "Mathematics",
    "author": "Hughes-Hallet",
    "edition": "6",
    "imageURL": "https://selfteachmedia.blob.core.windows.net/bookcovers/calculus.jpeg",
    "sections": [
        {
            "name": "1.2",
            "haveStudied": true,
            "studiedDate": "",
            "description": "Exponential Functions",
            "problems": [
                {
                    "name": "1",
                    "completed": true,
                    "completionDate": ""
*/

const bookSchema = new Schema({
    name: String,
    subject: String,
    author: String,
    edition: String,
    sections: [Section]
});

export default model("Book", bookSchema);