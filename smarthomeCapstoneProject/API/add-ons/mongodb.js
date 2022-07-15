const MongoClient = require('mongodb').MongoClient
const uri = "mongodb+srv://dbUser:dbUserPassword@cluster0-3hvot.mongodb.net/test?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true });

// client.connect(err => {
//     if (err) return console.error(err)
//   console.log('Connected to Database')
//   // const collection = client.db("test").collection("devices");
//   // perform actions on the collection object
//   client.close();
// });

module.exports = {
    saveOne : function (collection, data, callBack){
        client.connect((err,db)=>{
            if (err) throw err
            var dbo = db.db(`SmartHome`)
            dbo.collection(collection).insertOne(data, (err,res) => {
                if (err) {
                    console.log(err)
                    return;
                }
                db.close;
                callBack(res)
            })
        })
    },

    updateOne : function (collection, query, data,arrData){
        client.connect((err, db) => {
            if (err) throw err
            var dbo = db.db(`SmartHome`)
            if (arrData != null && data !== null){
                dbo.collection(collection).updateOne(query,{
                    $set: data,
                    $push : arrData,
                    $currentDate : {lastModified:true}
                })
            }if (arrData === null){
                dbo.collection(collection).updateOne(query,{
                    $set: data,
                    $currentDate : {lastModified:true}
                })
            }
            if (data === null){
                dbo.collection(collection).updateOne(query,{
                    $push: arrData,
                    $currentDate : {lastModified:true}
                })
            }
        })
    },

    findMany : function (collection,query,callBack){
        client.connect((err, db) => {
            if (err) throw err
            var dbo = db.db(`SmartHome`)
            dbo.collection(collection).find(query).toArray((err, res) => {
                if (err) callBack({status:400,data:err.message})
                db.close
                callBack({status:200,data:res})
            })
        })
    },

    findOne : function (collection,query,callBack){
        
        client.connect((err, db) => {
            if (err) throw err
            var dbo = db.db(`SmartHome`);
            dbo.collection(collection).findOne(query,(err, res) => {
                if (err) throw err
                db.close
                callBack(res);
            })
        })
    },

    

    findCount : function (collection, query, options, callBack){
        client.connect((err, db) => {
            if (err) throw err
            var dbo = db.db(`SmartHome`);
            dbo.collection(collection).countDocuments(query,options)
            .then(count => {
                callBack(count);
            })
        })
    }
}