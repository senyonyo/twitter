var twitter = require('twitter');

var bot  = new twitter({
	consumer_key        : process.env.API_KEY, 	
  consumer_secret     : process.env.API_SECRET,
	access_token_key    : process.env.ACCESS_TOKEN,
	access_token_secret : process.env.ACCESS_TOKEN_SECRET 
});

bot.post('statuses/update',
	{status: '半ライス大盛(このツイートはテストです)'},
	function(error, tweet, response) {
		if (error) {
			console.error(error);
		}
  })

function searchTweet(){
  bot.get('search/tweets', { q: 'lang:ja min_retweets:50' }, 
    function(err, data, response) {
      var time = new Date().getgetTime();
      var fs = require('fs');
      console.log(JSON.stringify(data));
      fs.writeFile(time+'.json',JSON.stringfy(data),function(err){
        console.log(err);
      })
    }
  );
}


setInterval(searchTweet, 2*60*1000);
