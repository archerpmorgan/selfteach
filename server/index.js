
const mongoose = require('mongoose')
const Schema = mongoose.Schema;
const MongoClient = require("mongodb").MongoClient;






const url = 'mongodb://127.0.0.1:27017/test'

mongoose.connect(url, { useNewUrlParser: true })

const db = mongoose.connection
db.once('open', _ => {
  console.log('Database connected:', url)
})

db.on('error', err => {
  console.error('connection error:', err)
})


const problemSchema = new Schema({
    name: String,
    completed: Boolean,
    completionDate: String
})

const sectionSchema = new Schema({
    name: String,
    haveStudied: Boolean,
    studiedDate: String,
    description: String,
    problems: [problemSchema],
});

const bookSchema = new Schema({
    name: String,
    subject: String,
    author: String,
    edition: String,
    sections: [sectionSchema]
});

const BookModel = mongoose.model("Book", bookSchema);

const newBook = new BookModel({
    name:"dubious name"
})

newBook.save(function (error, document) {
    if (error) console.error(error)
    console.log(document)
})

// boilerplate Express server startup
const express = require('express');

const app = express();

const port = 3001;

app.get('/', (req, res) => {
    res.send('Hello World, from express');
});

app.listen(port, () => console.log(`Hello world app listening on port ${port}!`))
