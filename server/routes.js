const express = require('express');

const { createNewBook } = require('./controller.js');

const router = express.Router();

router.post('/books/new', createNewBook);


module.exports = router;