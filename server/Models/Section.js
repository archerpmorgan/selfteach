const mongoose = require("mongoose");
const Problem = requre("./Problem");

const sectionSchema = new mongoose.Schema({
    name: String,
    haveStudied: Boolean,
    studiedDate: String,
    description: String,
    problems: [Problem],
});
module.exports = mongoose.model("Section", sectionSchema);