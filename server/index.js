const mongoose = require('mongoose')
const { dbKey } = require("../localSecrets.js");
const { BookModel } = require("./models.js");
const { router } = require('./routes.js');
const { cors } = require('cors');

// connect using mongodb client
// var mongoClient = require("mongodb").MongoClient;
// mongoClient.connect(dbKey.uri, function (err, client) {
//     if (err) {
//         console.log(err)
//     } else {
//         db = client.db('test');
//         startup();
//     }
// });

//connect using mongoose
mongoose.connect(dbKey.uri).then(
    () => { 
        console.log("Database connection funciona");
        startup(); 
    },
    err => { console.log(err) }
  );


function startup() {

    const express = require('express');
    const app = express();
    app.use('/', router);

    const port = 3001;

    app.get('/', (req, res) => {
        res.send('Hello World, from express');
    });

    app.listen(port, () => console.log(`Hello world app listening on port ${port}!`))

    // const newBook = new BookModel({
    //     title: "dubious name"
    // })    

    // newBook.save(function (error, document) {
    //     if (error) console.error(error)
    //     console.log(document)
    // })
}
