var express = require('express');
var router = express.Router();
let db = require('../add-ons/mongodb')


/* GET home page. */
router.get('/dashboard', function(req, res, next) {
  db.findMany("notifications",{}, resp=>{
    db.findOne("users",{name:"Joachim Asare"}, resl=>{
      // console.log(resl.sensor_readings)
      res.render('admin',{ notifications : resp.data, records : resl.sensor_readings });
    })    
  })
});



module.exports = router;
