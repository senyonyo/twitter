var json = require('./enjou.json');

function searchTweet(){
  bot.get('search/tweets', { q: '' },
    function(err, data, response) {
      var time = new Date().getTime();
      var fs = require('fs');
      //console.log(JSON.stringify(data));
      //console.log(data);
      var json_data = JSON.stringify(data);
      fs.writeFile('outputs1/'+time+'.json',json_data,function(err){
        console.log(err);
      })
    }
  );
}
