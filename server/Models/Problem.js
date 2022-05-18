import pkg from 'mongoose';
const { Schema, model } = pkg;

export const problemSchema = new Schema({
    name: String,
    completed: Boolean,
    completionDate: String
})
