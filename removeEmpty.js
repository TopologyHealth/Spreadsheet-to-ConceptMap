const fs = require('fs')

const dir = '/Users/josephmitchell/Documents/convertToConceptMap/notFormattedTestFiles'
const files = fs.readdirSync(dir)
for(const file of files){
   
 const jsonData= require('./notFormattedTestFiles/'+file); 


 const removeEmpty = (obj) => {
     Object.keys(obj).forEach(k =>
       (obj[k] && typeof obj[k] === 'object') && removeEmpty(obj[k]) ||
       (!obj[k] && obj[k] !== undefined) && delete obj[k]
     );
     return obj;
   };

 myObj2 = removeEmpty(jsonData);


 console.log(myObj2);


 var json = JSON.stringify(myObj2, null, 4);

 console.log(json);


 fs.writeFile(file.slice(0,-17)+'.json', json, 'utf8', (err) => {
     if (err)
       console.log(err);
     else {
       console.log("File written successfully\n");
     }
   });
}


