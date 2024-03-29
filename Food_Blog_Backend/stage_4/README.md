<h1>Stage 4/5: Too many ingredients</h1>

<h2>Description</h2>

<p>It's time to add ingredient quantities, measures, and ingredient names to your recipes! You noticed that some ingredients have long names and measures rarely start with the same letter. You decided to build your backend so that you do not have to enter full names when completing the database. You will encounter a many-to-many relationship again, this time between three tables, so you decided to introduce an intermediate table that would link all three tables.</p>

<p>Below is a diagram of the database tables.</p>

<p style="text-align: center;"><img alt="" src="https://ucarecdn.com/ef46f77a-b1a3-4fa3-9f3d-22d2fd40d28b/"></p>

<h2>Objectives</h2>

<ol>
	<li>Create a table named <code class="java">quantity</code> with five columns: <code class="java">quantity_id</code> of an <code class="java">INTEGER</code> type with the <code class="java">PRIMARY KEY</code> attribute, and four other columns: <code class="java">measure_id</code><span style="color: #000000;">, </span><code class="java">ingredient_id</code>, <code class="java">quantity</code> and <code class="java">recipe_id</code> . They should be of an <code class="java">INTEGER</code> type with the <code class="java">NOT NULL</code> attribute.</li>
	<li>Assign the following columns <code class="java">measure_id</code>, <code class="java">ingredient_id</code> and <code class="java">recipe_id</code> as Foreign Keys to the following <em>tables </em>(<code class="java">columns</code>): <em>measures</em> <code class="java">(measure_id)</code>, <em>ingredients </em><code class="java">(ingredient_id)</code>, and <em>recipes </em><code class="java">(recipe_id</code>) </li>
	<li>After asking a user about certain mealtime, make a loop that will gather information about the ingredients. The ingredients should be entered in the following format: <code class="java">quantity measure ingredient</code>.</li>
	<li>Pressing <code class="java">&lt;Enter&gt;</code> should finish the information gathering.</li>
	<li>The measure parameter should start with a string provided by a user. If there is more than one measure that starts with the provided string, ask the user again. For example <code class="java">tbs</code> and <code class="java">tbsp</code> both start with the <code class="java">t</code>. So the <code class="java">1 t sugar</code> entry should not pass.</li>
	<li>Mind that the <code class="java">measures</code> table contains an entry where the <code class="java">measure_name</code> is empty string, it means, that the measure could be not provided. In this case, use this entry to relate tables. For example, <code class="java">1 strawberry</code> should have a <code class="java">measure_key</code> from the entry with an empty name.</li>
	<li>The ingredient parameter should contain strings provided by a user. If there is more than one ingredient that contains the provided string, ask the user again. For example <code class="java">strawberry</code> and <code class="java">blueberry</code> both contain <code class="java">berry</code> as part of the string. So the <code class="java">10 kg berry</code> entry should not pass.</li>
	<li>Tests do not check the output. You can print anything you want. Tests will check only the database file that your script will create.</li>
</ol>

<h2>Examples</h2>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1:</strong></p>

<pre><code class="java">&gt; python food_blog.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: Hot milk
Recipe description: Boil milk
1) breakfast  2) brunch  3) lunch  4) supper 
Enter proposed meals separated by a space: 1 3 4
Input quantity of ingredient &lt;press enter to stop&gt;: 10 ml milk
Input quantity of ingredient &lt;press enter to stop&gt;: 
Recipe name:</code></pre>

<p><strong>Example 2:</strong></p>

<pre><code class="java">&gt; python food_blog.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: Hot milk
Recipe description: Boil milk
1) breakfast  2) brunch  3) lunch  4) supper 
Enter proposed meals separated by a space: 1 3 4
Input quantity of ingredient &lt;press enter to stop&gt;: 250 ml m
Input quantity of ingredient &lt;press enter to stop&gt;: 1 t sugar
The measure is not conclusive!
Input quantity of ingredient &lt;press enter to stop&gt;: 1 tbs sugar
Input quantity of ingredient &lt;press enter to stop&gt;: 1 berry
The ingredient is not conclusive!
Input quantity of ingredient &lt;press enter to stop&gt;: 1 blueberry
Input quantity of ingredient &lt;press enter to stop&gt;: 
Recipe name:</code></pre>
