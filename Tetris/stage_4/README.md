<h1>Stage 4/4: I Disappear</h1>

<h5>Description</h5>

<p>We are not done yet. We know how to rotate a piece, move it from left or right, and store it on the floor. Also, we restricted all these movements to the four walls of the game board.</p>

<p>Let's take our game to the next level. In addition to other features we have implemented, at this stage, the piece should become static when it touches another piece. Another thing we should do is to make horizontal blocks disappear when a row is filled. The game should end when the game board is filled.</p>

<pre><code class="language-no-highlight">- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -</code></pre>

<p>As you can see, the T piece is on the floor, static. We requested the <code class="java">O</code> piece. If the <code class="java">O</code> piece continues on its current path, it is going to touch the <code class="java">T</code> piece and become static as shown below:</p>

<pre><code class="language-no-highlight">- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - 0 0 - - - - -
- - - 0 0 - - - - -
- - - 0 - - - - - -
- - 0 0 0 - - - - -</code></pre>

<p> </p>

<p>The figure below shows the <code class="java">O</code> piece and two rotated <code class="java">I</code> pieces. The <code class="java">O</code> and the first rotated piece are on the floor. When the second <code class="java">I</code> piece hits the base, the entire row should disappear from the board:</p>

<pre><code class="language-no-highlight">- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - 0 0 0 0
0 0 0 0 0 0 - - - -</code></pre>

<p> </p>

<p>The figure below shows the game board once it has been done:</p>

<pre><code class="java">- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -</code></pre>

<p>The game should end once there is no more free space for our pieces.</p>

<p><div class="alert alert-primary">The column is considered filled when the height of the column equals the height of the pieces on the board. The row is considered filled when the row width equals the width of the row with pieces. We will also test if a moving piece can go through the static blocks. It means we will run the <code class="java">down</code> command one more time when a piece is on top of a static block.</div></p>

<h5>Objectives</h5>

<p>In this stage your program should:</p>

<ol>
	<li>Make a piece static when it touches another piece on the game board.</li>
	<li>Make rows disappear.</li>
	<li>Reduce the height of the block.</li>
	<li>End the game when the vertical column is filled.</li>
</ol>

<h5>Examples</h5>

<p>The example below shows how your program should work.</p>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1:</strong></p>

<pre><code class="language-no-highlight">input command &gt; board dimension: 10 10
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; piece
&gt;T
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - 0 - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; rotate
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -

input command &gt; piece
&gt;S
- - - - 0 0 - - - -
- - - 0 0 - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -

input command &gt; rotate
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - - 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - - 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - - 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - - 0 - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - - 0 - - - -
- - - - 0 - - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - 0 0 0 - - - -

input command &gt; piece
&gt;I
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - 0 0 0 - - - -

input command &gt; piece
&gt;O
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - 0 0 0 - - - -

input command &gt; down
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - 0 0 0 - - - -

Game Over!
</code></pre>

<p><strong>Example 2:</strong></p>

<pre><code class="language-no-highlight">input command &gt; board dimension: 10 10
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; piece
&gt;O
- - - - 0 0 - - - -
- - - - 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; left
- - - - - - - - - -
- - - 0 0 - - - - -
- - - 0 0 - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; left
- - - - - - - - - -
- - - - - - - - - -
- - 0 0 - - - - - -
- - 0 0 - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; left
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- 0 0 - - - - - - -
- 0 0 - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; left
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -
- - - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -

input command &gt; piece
&gt;I
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -

input command &gt; rotate
- - - - - - - - - -
- - - 0 0 0 0 - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -

input command &gt; left
- - - - - - - - - -
- - - - - - - - - -
- - 0 0 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - 0 0 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - 0 0 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - 0 0 0 0 - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - 0 0 0 0 - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - 0 0 0 0 - - - -
0 0 - - - - - - - -
0 0 - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 0 0 0 0 - - - -
0 0 - - - - - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 - - - -

input command &gt; piece
&gt;I
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - 0 - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 - - - -

input command &gt; rotate
- - - - - - - - - -
- - - 0 0 0 0 - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 - - - -

input command &gt; right
- - - - - - - - - -
- - - - - - - - - -
- - - - 0 0 0 0 - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 - - - -

input command &gt; right
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - 0 0 0 0 -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 - - - -

input command &gt; right
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - 0 0 0 0
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - 0 0 0 0
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - 0 0 0 0
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - 0 0 0 0
0 0 - - - - - - - -
0 0 0 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - 0 0 0 0
0 0 0 0 0 0 - - - -

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 0 0 0 0

input command &gt; down
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -
0 0 0 0 0 0 0 0 0 0

input command &gt; break
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
0 0 - - - - - - - -

input command &gt; exit
</code></pre>
