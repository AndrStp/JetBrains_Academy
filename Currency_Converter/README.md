<h1>Stage 6/6: Last but not least</h1>

<h2>Description</h2>

<p>At this stage, you need to specify what currency you want to exchange. Imagine that you came to the bank with some money in your pocket. You want to choose the best currency to exchange your money for. First, read the currency to exchange, then read the currency you might exchange your money for and the amount of money you want to exchange. Notice that the input number can have a fractional part!</p>

<p><div class="alert alert-primary">There is a different amount of currencies in different tests. Checking if input is empty might be really useful.</div></p>

<p>Parse the data from <a target="_blank" href="http://www.floatrates.com/json-feeds.html" rel="noopener noreferrer nofollow">FloatRates</a>. You can store it in any collection you want. It's called caching – a simple way to speed up the program. If we need to exchange the same currencies that we have already changed, we won't need to connect to the Internet, we only need to refer to the data in our cache. </p>

<p><div class="alert alert-primary">The very first currency is the one you want to exchange.</div></p>

<p>Check the cache — the required currency might be already in there, print the result afterward. Output the amount of money that the bank employee should give you. </p>

<h2>Objectives</h2>

<p>You're in the bank. Think about how much and what kind of currency you have.</p>

<ol>
	<li>Take the currency code, the amount of money the user has, and the currency code that the user wants to receive as the user input.</li>
	<li>Retrieve the data from <a target="_blank" href="http://www.floatrates.com/json-feeds.html" rel="noopener noreferrer nofollow">FloatRates</a> as in the previous exercises.</li>
	<li>Save the exchange rates for USD and EUR.</li>
	<li>Read the currency to exchange for and the amount of money.</li>
	<li>Take a look at the cache. Maybe you already have what you need?</li>
	<li>If you have the currency in your cache, calculate the amount.</li>
	<li>If not, get it from the site, and calculate the amount.</li>
	<li>Save all the information to your cache.</li>
	<li>Print the results.</li>
	<li>Repeat steps 4-9 until there is no currency left to process.</li>
</ol>

<h2>Examples</h2>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><div class="alert alert-primary">Be aware that the dictionary elements are unordered.</div></p>

<p>Example 1:</p>

<pre><code class="language-no-highlight">
&gt; ILS
&gt; USD
&gt; 45
Checking the cache...
Oh! It is in the cache!
You received 13.84 USD.
&gt; RSD
&gt; 57
Checking the cache...
Sorry, but it is not in the cache!
You received 1684.41 RSD.
&gt; EUR
&gt; 33
Checking the cache...
Oh! It is in the cache!
You received 8.38 EUR.</code></pre>

<p>Example 2:</p>

<pre><code class="language-no-highlight">
&gt; USD
&gt; EUR
&gt; 20
Checking the cache...
Oh! It is in the cache!
You received 16.52 EUR.
&gt; NOK
&gt; 45
Checking the cache...
Sorry, but it is not in the cache!
You received 382.1 NOK.
&gt; SEK
&gt; 75
Checking the cache...
Sorry, but it is not in the cache!
You received 624.66 SEK.
&gt; NOK
&gt; 55
Checking the cache...
Oh! It is in the cache!
You received 467.02 NOK.
&gt; ISK
&gt; 91
Checking the cache...
Sorry, but it is not in the cache!
You received 11708.38 ISK.</code></pre>
