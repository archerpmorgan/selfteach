const mongoose = require('mongoose')
const Schema = mongoose.Schema;

const problemSchema = new Schema({
    name: String,
    completed: Boolean,
    completionDate: String
})

const sectionSchema = new Schema({
    name: String, //usually a number, like 1, 13, etc, but can be an appendix name like AA or something
    haveStudied: Boolean,
    studiedDate: String,
    description: String, //usually the chapter name in the book, e.g. Vectors and Kinematics
    problemCount: Number,
    problems: [problemSchema],
});

const bookSchema = new Schema({
    title: { type: String, unique: true },
    subject: String,
    author: String,
    edition: String,
    sections: [sectionSchema]
});

const publicLibraryBookSchema = new Schema({
    title: { type: String, unique: true },
    subject: String,
    author: String,
    edition: String,
    sections: [sectionSchema]
});

const newBookRequestSchema = new Schema({
    title: String,
    subject: String,
    author: String,
    edition: String,
    sections: [sectionSchema]
})

const BookModel = mongoose.model("Book", bookSchema);
const PublicLibraryBookModel = mongoose.model("PublicLibraryBook", publicLibraryBookSchema);
const SectionModel = mongoose.model("Section", sectionSchema);
const ProblemModel = mongoose.model("Problem", problemSchema);
const NewBookRequestModel = mongoose.model("NewBookRequest", newBookRequestSchema);

module.exports = {
    BookModel,
    PublicLibraryBookModel,
    SectionModel,
    ProblemModel,
    NewBookRequestModel,
};