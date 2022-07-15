var express = require('express');
var router = express.Router();
let db = require('../add-ons/mongodb')
var multer = require('multer')
const storage = multer.diskStorage({
  destination: function(req,res,cb){
    cb(null,'uploads/')
  }
})
const upload = multer({storage:storage})
let fs = require('fs')


/* GET users listing. */
router.get('/dashboard', function(req, res, next) {
  res.render('user');
});

router.get('/database', function(req, res, next) {
  db.findOne("users",{name:"Joachim Asare"}, resl=>{
    // console.log(resl.sensor_readings)
    res.render('user_view',{ records : resl.sensor_readings });
  })  
});

router.put('/temperature', function(req,res,next){
  let status = req.body.status
  try {
    db.findOne("users",{name:"Joachim Asare"}, rps => {
      if(rps.recording_status.temperature !== status){
        db.saveOne("notifications",{message:`User has ${status} Temperature recording`, date:new Date()}, resp =>{
          notid = resp.insertedId
          db.updateOne("users",{name:"Admin"},null,{notifications:notid})
        })
        db.updateOne("users",{name:"Joachim Asare"},{recording_status:{temperature:status,audio:rps.recording_status.audio,image:rps.recording_status.image}},null)
        res.json({message:`Temperature recording status changed`})
      }
      else{
        res.json({message:"Status unchanged"})
      }
    })
    
  } catch (error) {
    res.json("Service currently unvailable")
  }
  
})
//  /users/status
router.get('/status', function(req, res, next){
  db.findOne("users",{name:"Joachim Asare"}, resp => {
    res.json({status: resp.recording_status})
  })
})

router.put('/audio', function(req,res,next){
  let status = req.body.status
  try {
    db.findOne("users",{name:"Joachim Asare"}, rps => {
      if(rps.recording_status.audio !== status){
        db.saveOne("notifications",{message:`User has ${status} audio recording`, date:new Date()}, resp =>{
          notid = resp.insertedId
          db.updateOne("users",{name:"Admin"},null,{notifications:notid})
        })
        db.updateOne("users",{name:"Joachim Asare"},{recording_status:{temperature:rps.recording_status.temperature,audio:status,image:rps.recording_status.image}},null)
        res.json({message:`Audio recording status changed`})
      }else{
        res.json({message:"Status unchanged"})
      }
    })
    
  } catch (error) {
    res.json("Service currently unvailable")
  }
  
})

//For images use .../user/recordings body 
// { }
router.post('/recordings',upload.single('file'), function(req,res){
      let record = {
        temperature : req.body.temperature,
        audio : req.body.audiofilename,
        image: req.body.imageFilename,
        imagefile:{
        data:fs.readFileSync(req.file.path),
        contentType : 'image/jpeg'
      },
      timestamps : new Date()
    }
 
 db.updateOne("users",{name:"Joachim Asare"},null,{sensor_readings:record})
 res.json({
    message : 'New image added to the db!',
 })
})


// for unauthorized image .../user/recording
router.post('/recording', function(req,res){
  let record = {
    temperature : req.body.temperature,
    audio : req.body.audiofilename,
    image: null,
    imagefile:{
    data:null,
    contentType : ''
  },
  timestamps : new Date()
}

db.updateOne("users",{name:"Joachim Asare"},null,{sensor_readings:record})
res.json({
message : 'New image added to the db!',
})
})

router.put('/upload/image', function(req,res,next){
  let status = req.body.status
  try {
    db.findOne("users",{name:"Joachim Asare"}, rps => {
      if(rps.recording_status.image !== status){
        db.saveOne("notifications",{message:`User has ${status} image recording`, date:new Date()}, resp =>{
          notid = resp.insertedId
          db.updateOne("users",{name:"Admin"},null,{notifications:notid})
        })
        db.updateOne("users",{name:"Joachim Asare"},{recording_status:{temperature:rps.recording_status.temperature,audio:rps.recording_status.audio,image:status}},null)

        res.json({message:`Image recording status changed`})
      }else{
        res.json({message:"Status unchanged"})
      }
    })
  } catch (error) {
    res.json("Service currently unvailable")
  }
  
})

module.exports = router;
