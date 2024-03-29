<h1>Stage 5/5: First interface</h1>

<h2>Description</h2>

<p>You decided to build a simple database query interface. The search results will be displayed on the screen, but in the future, you may want to create JSON files, load them in the frontend and show them in a browser... Stop! For now, the screen should suffice. </p>

<p>Today you want to eat a dish that will contain strawberries and milk, so you decide to build a query to the database which will return all dishes that contain both ingredients. Thanks to this, you will learn what else you need to buy for selected recipes. And since you're not interested in dinner dishes, you decide to add a second condition to find dishes that are appropriate for the time of day.</p>

<p>Next week you have an appointment with your great-grandmother, so you can ask about a few unreadable recipes, and maybe also show her what you have done.</p>

<h2>Objectives</h2>

<ol>
	<li>Pass two new parameters to the script: <code class="language-bash">ingredients</code> and <code class="language-bash">meals</code>. The parameters are not mandatory. If the new parameters are not passed, the script should work like in the previous stage.</li>
	<li>The <code class="language-bash">--ingredients</code> parameter should contain a list of ingredients separated by commas: <code class="language-bash">--ingredients="milk,sugar,tea"</code>. </li>
	<li>The <code class="language-bash">--meals</code> parameter should contain a list of meals separated by commas <code class="language-bash">--meals="dinner,supper"</code>. </li>
	<li>You should search the database for all the recipes which contain all of the passed ingredients (recipes may contain other ingredients as well) and can be served at a specific mealtime. If there are recipes that meet the conditions, print their names after a colon, separated by a comma. If you find two recipes with the same name print both names.</li>
	<li>If there are no such recipes, print: <code class="language-bash">There are no such recipes in the database</code>.</li>
	<li>This time we will check the output, so make sure that the last line you print contains the expected elements.</li>
	<li>You do not need to validate the arguments The tests will pass the correct values.</li>
</ol>

<p><b>Hint</b></p>
<p>If you can't build complex SQL queries, you can always work on the results of simpler queries using lists and sets.</p>

<p><b>Hint</b></p>
<p>The logic of the query should be (ingredient1 AND ingredient2 AND ...) AND (meal1 OR meal2 OR ...)</p>

<h2>Examples</h2>

<p>The greater-than symbol followed by a space (<code class="language-bash">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1</strong>(data input):</p>

<pre><code class="language-bash">&gt; python food_blog.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: &gt; Milkshake
Recipe description: &gt; Blend all ingredients and put in the fridge.
1) breakfast  2) brunch  3) lunch  4) supper
Enter proposed meals separated by a space: &gt; 1 3 4
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 500 ml milk
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 1 cup strawberry
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 1 tbsp sugar
Input quantity of ingredient &lt;press enter to stop&gt;: &gt;
Pass the empty recipe name to exit.
Recipe name: &gt; Hot cacao
Recipe description: &gt; Pour the ingredients into the hot milk. Mix it up.
1) breakfast  2) brunch  3) lunch  4) supper
Enter proposed meals separated by a space: &gt; 1 2
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 250 ml milk
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 2 tbsp cacao
Input quantity of ingredient &lt;press enter to stop&gt;: &gt;
Pass the empty recipe name to exit.
Recipe name: &gt; Hot cacao
Recipe description: &gt; Pour the ingredients into the hot milk. Mix it up.
1) breakfast  2) brunch  3) lunch  4) supper
Enter proposed meals separated by a space: &gt; 1 4
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 250 ml milk
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 2 tbsp cacao
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 1 tsp sugar
Input quantity of ingredient &lt;press enter to stop&gt;: &gt;
Pass the empty recipe name to exit.
Recipe name: &gt; Fruit salad
Recipe description: &gt; Cut strawberries and mix with other fruits. you can sprinkle everything with sugar.
1) breakfast  2) brunch  3) lunch  4) supper
Enter proposed meals separated by a space: &gt; 3 4
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 10 strawberry
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 50 g black
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 1 cup blue
Input quantity of ingredient &lt;press enter to stop&gt;: &gt; 1 tsp sugar
Input quantity of ingredient &lt;press enter to stop&gt;: &gt;
Pass the empty recipe name to exit.
Recipe name: &gt; </code></pre>

<p><strong>Example 2:</strong></p>

<pre><code class="language-bash">&gt; python food_blog.py food_blog.db --ingredients="sugar,milk" --meals="breakfast,brunch"
Recipes selected for you: Hot cacao, Milkshake</code></pre>

<p><strong>Example 3:</strong></p>

<pre><code class="language-bash">&gt; python food_blog.py food_blog.db --ingredients="sugar,milk,strawberry" --meals="brunch"
There are no such recipes in the database.</code></pre>
