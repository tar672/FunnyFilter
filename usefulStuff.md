Useful Stuff
============
TODO
----
* Connect to Pusher using key: `b325dfd8a54f892c35a0`
* Subscribe to channel: `all-tweets`
* Bind events to a callback function the events are called: `tweet`

* Write the callback function mentioned above to parse and display the tweet on the page (probably using jQuery)

* Bind the event of a user clicking on a tweet to a callback function
* Write the callback function to send the tweet as a post request to: `http://funny-filter.appspot.com/tweet`

* Make it pretty :)

Links
-----
For pusher API
* http://pusher.com/docs/javascript_quick_start

For parsing tweets
* `tweetObject = JSON.parse(data)` gives an object representing the tweet
* This object has a text attribute accessed using `tweetText = tweetObject.text`

For prepending to a page using jQuery
* http://api.jquery.com/prepend/

For binding a callback function to the click event in jQuery
* http://api.jquery.com/click/

For making a post request using jQuery
* http://api.jquery.com/jQuery.post/

Explanation of callbacks
* http://recurial.com/programming/understanding-callback-functions-in-javascript/
