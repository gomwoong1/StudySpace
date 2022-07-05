const express = require('express');
const router = express.Router();

router.get('/',(req,res) => {
    const name = {name: req.query.name};
    console.log(name);
    console.log(name.name);

    return res.render('main', {name: name.name});
});

module.exports = router;