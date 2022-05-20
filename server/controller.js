const mongoose = require('mongoose')
const { BookModel, SectionModel, ProblemModel, NewBookRequestModel, ChapterModel } = require("./models.js");

const createNewBook = async (req, res) => {
    const data = req.body;

    // need to do format validation on it
    //we expect it to come in as structured JSON
    let reqObj;
    let newBookDocument;
    try {
        reqObj = JSON.parse(reqObj);

        // then, check to see if that book already exists
        var queryResult = BookModel.findOne({title: reqObj.title}).exec();

        newBookDocument = new NewBookRequestModel(reqObj);

    } catch (error) {
    console.log(error.message);
    res.status(409).json({ message: error.message });
    }
}

module.exports = {
    createNewBook: createNewBook
}

