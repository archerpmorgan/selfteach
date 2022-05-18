const mongoose = require("mongoose");

const problemSchema = new mongoose.Schema({
    name: String,
    completed: Boolean,
    completionDate: String
})

module.exports = mongoose.model("Problem", problemSchema);