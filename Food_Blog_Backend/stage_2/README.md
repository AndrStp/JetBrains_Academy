<h1>Stage 2/5: Time for recipes</h1>

<h2>Description</h2>

<p>It is time to create the main recipe table. You decided to store the recipe name and description in the main table. You wanted to indicate which meal suits the dish best, but your great-grandmother told you that it doesn't have to be just one meal. So you have to think about the solution. You also need to build a tool that will allow you to fill your database with data.</p>

<p>Below is a diagram of the database tables. </p>

<p style="text-align: center;"><img alt="" src="https://ucarecdn.com/22aa1e6d-5eb0-438b-bbb7-9bdff6a32001/"></p>

<h2>Objectives</h2>

<ol>
	<li>Create a table named <code class="java">recipes</code> with three columns: <code class="java">recipe_id</code> of an integer type with the primary key attribute, <code class="java">recipe_name</code> of a text type with the not-null attribute, and <code class="java">recipe_description</code> of a text type.</li>
	<li>Prepare a simple system that allows you to populate this table. Ask for the recipe name and the cooking directions, and insert the data into the table.</li>
	<li>When a zero-length string is entered for the recipe name the script should terminate. Remember to commit your changes and close the database.</li>
	<li>Remember! You can print anything you want. Tests will check only the database file that your script will create and populate.</li>
	<li>You do not need to validate the entered data. The tests will pass the correct values.</li>
</ol>

<p><b>Hint</b></p>
<p>The primary key cell of an integer type will be incremented automatically. You only need to insert values to other columns.</p>

<h2>Example</h2>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<pre><code class="java">&gt; python food_blog.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: &gt; Cold milk
Recipe description: &gt; Freeze milk
Recipe name: &gt; Hot milk
Recipe description: &gt; Boil milk
Recipe name: &gt;</code></pre>
