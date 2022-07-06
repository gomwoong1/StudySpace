//npm install npm, express, ejs

const express = require('express');
const app =  express();
const port = 3001;

const path = require('path');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.listen(port, () => {
    console.log(`Server Open: ${port} port`);
});

const router = require('./router.js');
app.use('/', router);