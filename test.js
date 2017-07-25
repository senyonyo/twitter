var fs = require('fs');
var rs = fs.createReadStream('./outputs.lst');
var readline = require('readline');

var rl = readline.createInterface(rs, {});

rl.on('line', function(line) {
  var obj = JSON.parse(fs.readFileSync('outputs/'+line, 'utf8'));
  for(k in obj.statuses){
    if(obj.statuses[k].id==884528664905359360)console.log(obj.statuses[k]);
  }
});
