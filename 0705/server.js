const express = require('express');
const app = express();
const port = 3001;
const path = require('path');
const mysql = require('mysql2');

const dbinfo = require('./db.js');
const db = new dbinfo();
const conn = mysql.createPool(db.info);
conn.getConnection((err) => {
    if(!err){
        console.log("연결 성공");
    }else{
        console.log(err);
    }
})

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.listen(port, () => {
    console.log(`Server Open: ${port} port`)
});

const router = require('./routers/router.js');
app.use('/', router);

app.get('/get-db', (req, res) => {
    const body = req.body;
    return db.getName(conn, res.body);
})