const mongoose = require('mongoose')
const { dbKey } = require("../localSecrets.js");
const app = require('express')();
const bodyParser = require('body-parser');
const cors = require('cors')
app.use(cors());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());


//setup routes
var bookRoutes = require("./routes/books");
app.use(`/books`, bookRoutes);



//connect using mongoose
mongoose.connect(dbKey.uri).then(
    () => { 
        console.log("Database connection funciona");
        startup(); 
    },
    err => { console.log(err) }
  );


function startup() {
    const port = 3001;
    app.listen(port, () => console.log(`Hello world app listening on port ${port}!`))
}
