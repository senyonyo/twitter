var fs = require('fs');
fs.readdir('.', function(err, files){
    if (err) throw err;
    var fileList = [];
    files.filter(function(file){
        data = fs.statSync(file).isFile() && /.*\.json$/.test(file);
    }).forEach(function (file) {
        fileList.push(file);
    });
		fs.writeFile('filename.json', JSON.stringify(data, null, '    '));
});

/*var json = JSON.parse(fs.readFileSync('./outputs1/', 'utf8'));
console.log(json.marker[0].name);

if(){
  


}
*/
