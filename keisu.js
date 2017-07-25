var fs=require('fs');
var rs = fs.createReadStream('./outputs5000.lst');
var readline = require('readline');

var rl = readline.createInterface(rs, {});

rl.on('line', function(line) {
  var obj = JSON.parse(fs.readFileSync('outputs5000/'+line, 'utf8'));
  for(k in obj.statuses){
    if(obj.statuses[k]==obj.statuses.length){
			console.log(obj.statuses[k]);
  	}
	}	
});
