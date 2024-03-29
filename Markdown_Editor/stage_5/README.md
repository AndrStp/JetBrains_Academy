<h1>Stage 5/5: Save the results</h1>

<h2>Description</h2>

<p>By this moment, our program can recognize some of the formatters and special commands, it can also print the results and exit. We need to implement yet another very useful feature — the ability to save the text to a file.</p>

<h2>Objectives</h2>

<p>Modify your <code class="java">done</code> function that was implemented in the second stage. Apart from exiting the program, it should save the final result of a session to a file, let's call it <em>output.md</em>. Create this file in the program directory. If it already exists, overwrite this file. The file should include the result of the last session.</p>

<h2>Examples</h2>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1:</strong></p>

<pre>	<code class="language-no-highlight">
Choose a formatter: &gt; header
Level: &gt; 1
Text: &gt; Hello World!
# Hello World!

Choose a formatter: &gt; plain
Text: &gt; Lorem ipsum dolor sit amet, consectetur adipiscing elit
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit
Choose a formatter: &gt; line-break
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit

Choose a formatter: &gt; ordered-list
Number of rows: &gt; 3
Row #1: &gt; dolor
Row #2: &gt; sit
Row #3: &gt; amet
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit
1. dolor
2. sit
3. amet

Choose a formatter: &gt; !done</code>
</pre>
