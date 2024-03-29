<h1>Stage 1/4: Getting Started</h1>

<h5>Description</h5>

<p>The original Tetris game has 7 unique pieces, each made up of 4 segments: the <code class="java">T</code> piece, the <code class="java">O</code> piece, the <code class="java">L</code> piece, the <code class="java">J</code> piece, the <code class="java">I</code> piece, the <code class="java">S</code> piece, and the <code class="java">Z</code> piece.</p>

<p>In this stage, you need to design the pieces and show how they can be rotated counterclockwise at 90 degrees inside a 4x4 grid.</p>

<pre><code class="language-no-highlight">00 01 02 03
04 05 06 07
08 09 10 11
12 13 14 15
</code></pre>

<p>The numbers <code class="java">00 01 02 03</code> represent the first items on the four columns of the grid. The numbers below represent the first items of the grid rows.</p>

<pre><code class="language-no-highlight">00
04
08
12</code></pre>

<p>So, a 4x4 grid should have four rows and columns — naturally, a 4x4 matrix. Every element in our matrix is filled with a hyphen, <code class="java">-</code>, and one space.</p>

<pre><code class="java">- - - -
- - - -
- - - -
- - - -
</code></pre>

<p>Each piece is designed with the help of four zeros <code class="java">(0)</code>. They are our building segments. In the end, we should have the following:</p>

<p>The <code class="java">I</code> piece:</p>

<pre><code class="language-no-highlight">- 0 - -
- 0 - -
- 0 - -
- 0 - -</code></pre>

<p>The <code class="java">S</code> piece:</p>

<pre><code class="language-no-highlight">- - - -
- 0 0 -
0 0 - -
- - - -
</code></pre>

<p>The <code class="java">Z</code> piece:</p>

<pre><code class="language-no-highlight">- - - -
0 0 - -
- 0 0 -
- - - -
</code></pre>

<p>The <code class="java">L</code> piece:</p>

<pre><code class="language-no-highlight">- 0 - -
- 0 - -
- 0 0 -
- - - -
</code></pre>

<p>The <code class="java">J</code> piece:</p>

<pre><code class="language-no-highlight">- - 0 -
- - 0 -
- 0 0 -
- - - -
</code></pre>

<p>The <code class="java">O</code> piece:</p>

<pre><code class="language-no-highlight">- - - -
- 0 0 -
- 0 0 -
- - - -
</code></pre>

<p>The <code class="java">T</code> piece:</p>

<pre><code class="language-no-highlight">- 0 - -
0 0 0 -
- - - -
- - - -
</code></pre>

<h5>Objectives</h5>

<p>In this stage, your program should:</p>

<ol>
	<li>Create a 4x4 grid. </li>
	<li>Design seven unique pieces: <code class="java">I, S, Z, L, J, O, T</code></li>
	<li>Design the rotated states of the unique pieces. </li>
	<li>The pieces and their rotated states should be placed inside one list. The unique piece should take the first position in the list. the next positions should be filled with the pieces rotated by 90 degrees counterclockwise.</li>
	<li>Rotate the pieces inside the grid. The piece is rotated automatically and should appear in a new grid </li>
	<li>Print and rotate the unique pieces in the order they were created</li>
</ol>

<p>The examples below show how the <code class="java">I</code> and<code class="java"> S </code>pieces and their rotated states described in steps 3 and 4 looks like:</p>

<pre><code class="language-no-highlight">I = [[1, 5, 9, 13], [4, 5, 6, 7]]
S = [[6, 5, 9, 8], [5, 9, 10, 14]]</code></pre>

<p><div class="alert alert-primary">Print a unique piece first. Then print new grids with all its rotated states. The <span style="color: #000000;">O</span> piece does not change on rotation, so it has only one state. A piece will be rotated four times as shown in the examples below.</div></p>

<h5>Examples</h5>

<p>The example below shows how your program should work.</p>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1:</strong></p>

<pre><code class="language-no-highlight">Input command: &gt; T

- - - -
- - - -
- - - -
- - - -

- 0 - -
0 0 0 -
- - - -
- - - -

- 0 - -
0 0 - -
- 0 - -
- - - -

- - - -
0 0 0 -
- 0 - -
- - - -

- 0 - -
- 0 0 -
- 0 - -
- - - -

- 0 - -
0 0 0 -
- - - -
- - - -
</code></pre>

<p><strong>Example 2</strong></p>

<pre><code class="language-no-highlight">Input command: &gt; J

- - - -
- - - -
- - - -
- - - -

- - 0 -
- - 0 -
- 0 0 -
- - - -

- - - -
0 0 0 -
- - 0 -
- - - -

- 0 0 -
- 0 - -
- 0 - -
- - - -

0 - - -
0 0 0 -
- - - -
- - - -

- - 0 -
- - 0 -
- 0 0 -
- - - -
</code></pre>
