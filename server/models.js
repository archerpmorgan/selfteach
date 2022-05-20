const mongoose = require('mongoose')
const Schema = mongoose.Schema;

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
    title: { type: String, unique: true },
    subject: String,
    author: String,
    edition: String,
    sections: [sectionSchema]
});

const chapterSchema = new Schema({
    name: String,
    number: String,
    problemCount: Number
})

/**
 * ingestion template
name:Introduction To Mechanics
subject:Physics
author:Kleppner
edition:2
imageURL: https://selfteachmedia.blob.core.windows.net/bookcovers/introductionToMechanics.png
chapters (name->description->number of problems) (Note chapter review goes up through CAS):
1->Vectors and Kinematics->27
2->Newton's Laws->17
3->Forces of Equation and motion->26
4->Momentum->27
5->Energy->19
6->Topics in Dynamics->17
7->Angular Momentum and Fixed Axis Rotation->41
8->Rigid Body Motion->12
9->Non-Inertial Systems and Fictitious Forces->12
10->Central Force Motion->15
11->The Harmonic Oscillator ->14
12->The Special Theory of Relativity->19
13->Relativistic Dynamics->12
14->Spacetime Physics->8
end of chapters
 */

const newBookRequestSchema = new Schema({
    title: String,
    subject: String,
    author: String,
    edition: String,
    chapters: [chapterSchema]
})

const BookModel = mongoose.model("Book", bookSchema);
const SectionModel = mongoose.model("Section", sectionSchema);
const ProblemModel = mongoose.model("Problem", problemSchema);
const NewBookRequestModel = mongoose.model("NewBookRequest", newBookRequestSchema);
const ChapterModel = mongoose.model("Chapter", chapterSchema);

module.exports = {
    BookModel: BookModel,
    SectionModel: SectionModel,
    ProblemModel: ProblemModel,
    NewBookRequestModel: NewBookRequestModel,
    ChapterModel: ChapterModel
}