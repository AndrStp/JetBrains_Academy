<h1>Stage 4/6: Looking ahead</h1>

<h2>Description</h2>

<p>It is time to find a winning strategy. At each point, the player may have different move options. We could check every route combination, but it would take a long-long time. With a computer program, we could use brute force to check every possible route until we find a solution. However, this is inefficient and could take a while even for a computer. So what is the best way to crack this puzzle? <strong>Warnsdorff's rule</strong> is here to help us.</p>

<p>Warnsdorff's rule is a strategy that helps choose the best move based on the knight's position and the board status. To apply it, we need to do the following:</p>

<ol>
	<li>Check if each of the eight knight's moves is possible;</li>
	<li>Check how many moves are possible from that landing position.</li>
</ol>

<p>Here is an example of the algorithm:</p>

<p><img alt="" height="320" src="https://ucarecdn.com/8133a46d-ca7b-46c1-b95b-3955e4b7758b/" width="320"></p>

<p>There are 8 possible moves from the starting position. The number shows how many moves there are from that position. Here is an example to illustrate the next possible moves. Note that the highest number is 7, since you cannot revisit the square you moved from, and the lowest number is 0 which indicates a dead-end.</p>

<p><img alt="" height="321" src="https://ucarecdn.com/15faff45-acd4-4482-be87-21c854a765c0/" width="321"></p>

<h2>Objectives</h2>

<p>In this stage, you should modify your program to do the following:</p>

<ol>
	<li>From the starting position, check all eight possible moving directions.</li>
	<li>If the move is possible, mark the square with a number that indicates how many distinct moves are possible from that square.</li>
	<li>If the move is not possible, no action is required.</li>
</ol>

<p>Please, don't forget about functional decomposition: splitting your code into reusable functions is very important for the next stages.</p>

<h2>Examples</h2>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1</strong></p>

<pre><code class="language-no-highlight">Enter your board dimensions: &gt; 6 5
Enter the knight's starting position: &gt; 4 2

Here are the possible moves:
 ---------------------
5| __ __ __ __ __ __ |
4| __ __  5 __  3 __ |
3| __  5 __ __ __  3 |
2| __ __ __  X __ __ |
1| __  2 __ __ __  1 |
 ---------------------
    1  2  3  4  5  6</code></pre>

<p><strong>Example 2</strong></p>

<pre><code class="language-no-highlight">Enter your board dimensions: &gt; 3 4
Enter the knight's starting position: &gt; 2 2

Here are the possible moves:
 ------------
4|  1 __  1 |
3| __ __ __ |
2| __  X __ |
1| __ __ __ |
 ------------
    1  2  3</code></pre>

<p><strong>Example 3</strong></p>

<pre><code class="language-no-highlight">Enter your board dimensions: &gt; 1 2
Enter the knight's starting position: &gt; 1 2

Here are the possible moves:
 -----
2| X |
1| _ |
 -----
   1</code></pre>
