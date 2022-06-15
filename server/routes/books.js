const { BookModel, SectionModel, ProblemModel, NewBookRequestModel, PublicLibraryBookModel } = require("../models.js")

var router = require('express').Router();

router.post('/new', async (req, res) => {
    //we expect it to come in as structured JSON
    let reqObj;
    let newBookDocument;
    try {

        let reqObj = req.body;

        //save the request
        newBookDocument = new NewBookRequestModel(reqObj);
        newBookDocument.save();

        //check to see if that book already exists
        var newPublicLibraryBook = new PublicLibraryBookModel(reqObj);
        var publicLibraryBookQueryResult = await PublicLibraryBookModel.findOne({title: reqObj.title}).exec();

        if (publicLibraryBookQueryResult == null) {
            // we haven't seen a book with this title before, we are good to add it
            newPublicLibraryBook.save();
        }
    } catch (error) {
    console.log(error.message);
    res.status(409).json({ message: error.message });
    }
    res.status(201).json(newBookDocument);
});

router.post('/cover', async (req, res) => {
    var body;
    try {
        body = req.body;
    } catch (error) {
    console.log(error.message);
    res.status(409).json({ message: error.message });
    }
    res.status(201).json(newBookDocument);
});


module.exports = router;