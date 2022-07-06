const express = require('express');
const app =  express();
const port = 3001;

app.listen(port, () => {
    console.log(`Server Open: ${port} port`);
});

const router = require('./router.js');
app.use('/', router);