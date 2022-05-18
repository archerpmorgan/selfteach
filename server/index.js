
const mongoose = require("mongoose");
const MongoClient = require('mongodb').MongoClient
const Book = require('./Models/Book').default
const url = 'mongodb://127.0.0.1:27017'
const dbName = 'books'
let db

MongoClient.connect(url, { useNewUrlParser: true }, (err, client) => {
  if (err) return console.log(err)
  db = client.db(dbName)
  console.log(`Connected MongoDB: ${url}`)
  console.log(`Database: ${dbName}`)
})

const book = new Book({
    name: "dub book"
});

// boilerplate Express server startup
const express = require('express');

const app = express();

const port = 3001;

app.get('/', (req, res) => {
    res.send('Hello World, from express');
});

app.listen(port, () => console.log(`Hello world app listening on port ${port}!`))
