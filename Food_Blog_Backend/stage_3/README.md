<h1>Stage 3/5: Many-to-many relations</h1>

<h2>Description</h2>

<p>On this stage, you need to create many-to-many relations between two tables. One dish can be served at different mealtimes, and one meal can consist of different dishes. </p>

<p>Below is a database diagram showing tables with a many-to-many relationship.</p>

<p style="text-align: center;"><img alt="" src="https://ucarecdn.com/dfd33277-85c3-459e-8c7f-6bb4a87f1fa9/"></p>

<p>However, this model is not recommended. Instead, we suggest you implementing a cross-reference table that contains primary key attributes from the two tables in relation. </p>

<p>Take a look at the diagram below. It contains an intermediate table; one-to-many relationships are also indicated. <strong>FK</strong> stands for <strong>Foreign Key</strong>.</p>

<p style="text-align: center;"><img alt="" src="https://ucarecdn.com/50d5570e-7dd6-4a13-a45b-191adb70262a/"></p>

<p>You need to expand your backend system.</p>

<h2>Theory</h2>

<p>In SQLite, you can use two methods to retrieve entries from the returned object: <code class="java">fetchall()</code> and <code class="java">fetchone()</code>. The first method returns all matching entries as a list of tuples, while the second method returns the next data row or <code class="java">None</code> if there are no more rows:</p>

<pre><code class="java">result = cursor_name.execute(SQL_query_as_string)
all_rows = result.fetchall()  # all_rows stores a list of tuples

result = cursor_name.execute(SQL_query_as_string)
next_row = result.fetchone()  # returns a single tuple
</code></pre>

<p>A useful attribute of the cursor object is <code class="java">lastrowid</code>. When the <strong>INTEGER PRIMARY KEY </strong>column is auto-incremented, this attribute stores the value of this key. It allows you to know the <code class="java">PRIMARY KEY</code> attribute of the entry. Don't forget to commit your changes!</p>

<pre><code class="java">result = cursor_name.execute(SQL_INSERT_query_as_string).lastrowid</code></pre>

<p>To use foreign keys in your SQLite database, you need to turn them on first by executing the command:</p>

<pre><code class="java">PRAGMA foreign_keys = ON;</code></pre>

<p>When creating a table, you need to associate the foreign key with the given column:</p>

<pre><code class="java">CREATE TABLE IF NOT EXISTS table1(table1_id INTEGER PRIMARY KEY, table2_id INTEGER NOT NULL,
FOREIGN KEY(table2_id) REFERENCES table2(table2_id));
</code></pre>

<p>Once you indicated the <code class="java">FOREIGN KEY</code> parameter in your code, the entries associated with this parameter cannot be deleted as long as this parameter persists. In the example above, we won't be able to remove the entries from the <code class="java">table2</code> until we remove the linking entry from the <code class="java">table1</code>.</p>

<p> You can refer to <a target="_blank" href="https://www.sqlitetutorial.net/sqlite-foreign-key/" rel="noopener noreferrer nofollow">the Foreign Key</a> section of the SQLite tutorial for more details.</p>

<h2>Objectives</h2>

<ol>
	<li>Create a table named <code class="java">serve</code> with three columns: <code class="java">serve_id</code> of an <code class="java">INTEGER</code> type with the <code class="java">PRIMARY KEY</code> attribute, and <code class="java">recipe_id</code> and <code class="java">meal_id</code>, both of <code class="java">INTEGER</code> type with the <code class="java">NOT NULL</code> attribute.</li>
	<li>Assign the <code class="java">recipe_id</code> and <code class="java">meal_id</code> as Foreign Keys to the following tables: <code class="java">recipes</code> (the <code class="java">recipe_id</code> column) and <code class="java">meals</code> (the <code class="java">meal_id</code> column).</li>
	<li>Once a user has entered a dish name and a recipe description print all available meals with their primary key numbers. </li>
	<li>Ask a user when this dish can be served. Users should input numbers separated by a space.</li>
	<li>Input values to the <code class="java">serve</code> table. If the user has selected three meals when the dish can be served, there should be three new entries in the <code class="java">serve</code> table.</li>
	<li>You do not need to validate the entered data. The tests will enter the correct values.</li>
	<li>Tests do not check the output. You can print anything you want. Tests will check only the database file that your script will create.</li>
</ol>

<h2>Examples</h2>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<pre><code class="java">&gt; python food_blog.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: &gt; Hot milk
Recipe description: &gt; Boil milk
1) breakfast  2) brunch  3) lunch  4) supper 
When the dish can be served: &gt; 1 3 4
Recipe name:</code></pre>
