const mongoose = require('mongoose')
const { BookModel, SectionModel, ProblemModel, NewBookRequestModel, ChapterModel } = require("./models.js");

export const createNewBook = async (req, res) => {
    const data = req.body;

    // need to do format validation on it
    //we expect it to come in as structured JSON
    let reqObj;
    let newBookDocument;
    try {
        reqObj = JSON.parse(reqObj);
        newBookDocument = new NewBookRequestModel(reqObj);
    } catch(e) {
        console.log(error.message);
        res.status(409).json({ message: error.message });
    }

    // then, check to see if that book already exists
    



    // then if well-formatted and truly new, add to database

    try {
    const { container } = await database.containers.createIfNotExists({ id: "archer" });
    const result = await container.items.create(data);
    res.status(201).json({});
    } catch (error) {
    console.log(error.message);
    res.status(409).json({ message: error.message });
    }
}

