import pkg from 'mongoose';
const { Schema, model } = pkg;
import sectionSchema from "./Section.js";

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

export const bookSchema = new Schema({
    name: String,
    subject: String,
    author: String,
    edition: String,
    sections: [sectionSchema]
});
