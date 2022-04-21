const fs = require('fs')

const dir = './NotFormatted/'
const files = fs.readdirSync(dir)
for(const file of files){
   
 const jsonData= require('./NotFormatted/'+file); 


 const removeEmpty = (obj) => {
     Object.keys(obj).forEach(k =>
       (obj[k] && typeof obj[k] === 'object') && removeEmpty(obj[k]) ||
       (!obj[k] && obj[k] !== undefined) && delete obj[k]
     );
     return obj;
   };

 myObj2 = removeEmpty(jsonData);


 var json = JSON.stringify(myObj2, null, 4);


 fs.writeFile('./Formatted/' + file +'.json', json, 'utf8', (err) => {
     if (err)
       console.log(err);
     else {
       console.log("File written successfully\n");
     }
   });
}


