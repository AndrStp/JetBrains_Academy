<h1>Stage 1/5: Create dictionaries</h1>

<h2>Description</h2>

<p>Your great-grandmother asked you to copy "to these computers" all the recipes that she had been collecting in her notebook for several decades. You think that this task can be a good opportunity to practice your skills and build a tool that would collect the data in a database. It will allow you to create a database of recipes that you will be able to use in the blog with the great-grandma's recipes. You started by writing down the names of the ingredients and measures that Grandma used. It also may be good to assign different dishes to different times of the day. It's time to create a database and dictionaries!</p>

<p>Below is a diagram of the database tables. <strong>PK</strong> means the <strong>Primary Key</strong>.</p>

<p style="text-align: center;"><img alt="" src="https://ucarecdn.com/02f9c2e9-014c-4e1e-b6cd-893d401f9414/"></p>

<h2>Theory</h2>

<p>SQLite3 is a relational database management system. You can use it for free; it is licensed as Public Domain. The system implements most of the SQL standards. For this project, we will use the basic SQLite3 functions.</p>

<p>First, import the sqlite3 library:</p>

<pre><code class="java">import sqlite3
</code></pre>

<p>To connect your script to an SQLite database, use the <code class="java">connect()</code> method from the <code class="java">sqlite3</code> library and create a database cursor with the <code class="java">cursor()</code> method:</p>

<pre><code class="java">conn = sqlite3.connect(data_base_name)
cursor_name = conn.cursor()
</code></pre>

<p>To execute an SQL query, use the <code class="java">execute()</code> cursor method. This method will return an object that contains the result of the query. For example:</p>

<pre><code class="java">result = cursor_name.execute(SQL_query_as_string)
</code></pre>

<p>Another two important methods are <code class="java">close()</code> and <code class="java">commit()</code>. Remember that you need to confirm the SQL queries with the <code class="java">commit</code> command. Otherwise, the data will be lost. At the end of your code, disconnect your database. Both methods are related to the database connection:</p>

<pre><code class="java">conn.commit()
conn.close()
</code></pre>

<p>If you need more information, the <a target="_blank" href="https://www.sqlitetutorial.net/" rel="noopener noreferrer nofollow">SQLite Tutorial</a> will help you!</p>

<h2>Objectives</h2>

<ol>
	<li>Create a database. Pass the name of the database to the script as an argument.</li>
	<li>Create a table named <code class="java">meals</code> with two columns: <code class="java">meal_id</code> of an integer type with the primary key attribute, and <code class="java">meal_name</code> of a text type and with the unique and not null attribute. </li>
	<li>Create a table named <code class="java">ingredients</code> with two columns: <code class="java">ingredient_id</code> of an integer type with the primary key attribute and <code class="java">ingredient_name</code> of a text type with the unique and not null attribute. Multi-word ingredients are out of scope, you don't need to implement their support in your script.</li>
	<li>Create a table named <code class="java">measures</code> with two columns: <code class="java">measure_id</code> of an integer type with the primary key attribute, and <code class="java">measure_name</code> of a text type with the unique attribute. </li>
	<li>Populate the tables. Those tables are the dictionaries for the Food Blog system, you need to fill them once for the rest of the stages.
	<pre><code class="java">data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}</code></pre>
	</li>
	<li>Tests do not check the output. You can print anything you want. Tests will check only the database file that your script will create.</li>
	<li>Do not add other items to the dictionaries. This may affect the test results in this and the next stages.</li>
</ol>

<p><b>Hint</b></p>
<p>If you would like to see how your database looks like, you can use the <strong>DB Browser for SQLite </strong>tool. It can be downloaded from <a target="_blank" href="https://sqlitebrowser.org/" rel="noopener noreferrer nofollow">sqlitebrowser.org</a> for free.</p>

<h2>Example </h2>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<pre><code class="java">&gt; python food_blog.py food_blog.db</code></pre>

