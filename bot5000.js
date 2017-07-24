var twitter = require('twitter');

var bot  = new twitter({
	consumer_key        : process.env.API_KEY, 	
  consumer_secret     : process.env.API_SECRET,
	access_token_key    : process.env.ACCESS_TOKEN,
	access_token_secret : process.env.ACCESS_TOKEN_SECRET 
});

/*bot.post('statuses/update',
	{status: '半ライス大盛(このツイートはテストです)'},
	function(error, tweet, response) {
		if (error) {
			console.error(error);
		}
  })
*/

function searchTweet(){
  bot.get('search/tweets', { q: 'lang:ja min_retweets:5000' }, 
    function(err, data, response) {
      var time = new Date().getTime();
      var fs = require('fs');
      //console.log(JSON.stringify(data));
      //console.log(data);
      var json_data = JSON.stringify(data);
      fs.writeFile('outputs5000/'+time+'.json',json_data,function(err){
        console.log(err);
      })
    }
  );
}

searchTweet();
setInterval(searchTweet, 120*60*1000);
