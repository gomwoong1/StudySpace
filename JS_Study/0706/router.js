const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    return res.render('main');
});

router.get('/page_move', (req, res) => {
    res.redirect('page1.ejs');
});

module.exports = router;