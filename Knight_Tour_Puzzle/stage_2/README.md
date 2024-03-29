<h1>Stage 2/6: And now for something completely different</h1>

<h2>Description</h2>

<p>The traditional version of the puzzle uses a standard chessboard, but you can use a board of any size. You can try smaller boards like 5×5, rectangular boards like 4×8, or even non-rectangular boards with some squares missing! Here, we will only focus on rectangular boards. Note that the board is guaranteed to have a solution if the smallest dimension is at least 5. Smaller boards may not have a solution.</p>

<h2>Objectives</h2>

<p>In this stage, you should modify your program to do the following:</p>

<ol>
	<li>Ask the user for the board's dimensions using X for columns and Y for rows.</li>
	<li>If the board's dimensions contain non-integer numbers print <code class="java">Invalid dimensions!</code>.</li>
	<li>If the board's dimensions contain more than 2 numbers print <code class="java">Invalid dimensions!</code>.</li>
	<li>If the board's dimensions contain negative numbers print <code class="java">Invalid dimensions!</code>.</li>
	<li>If invalid dimensions were provided by the user, ask them for valid dimensions again after outputting <code class="java">Invalid dimensions!</code></li>
	<li>Once the starting position is determined, check whether it is valid as in the previous stage.</li>
	<li>If not, you should show the <code class="java">Invalid position!</code> error message and then prompt the user for another starting position.</li>
	<li>Draw the board.</li>
</ol>

<p>Use an underscore symbol <code class="java">_</code> to mark empty board squares; the number of underscore symbols for each empty square should be chosen according to the total number of cells: there should be as many underscores for each cell as there are digits in the total number of cells. For example, a 10 × 10 board has 100 spaces, so your placeholder should be <code class="java">___</code> for an empty cell. If your board dimension is 6 x 5, your placeholder will be <code class="java">__</code>. This will be used in later stages.</p>

<p>Make sure that the column numbers are exactly under the placeholders for the given column. Also, make sure your column, row numbers, and the knight position are aligned to the right: for example, the knight positions should be marked as <code class="java">_X</code> or <code class="java">__X</code> (instead of <code class="java">X_</code> or <code class="java">_X_</code>), depending on the number of underscores for each square. </p>

<p>The border's length also depends on the size of the field. Use the following formula to calculate the length of the required border: <code class="java">column_n * (cell_size + 1) + 3</code>, where <code class="java">column_n</code> is the number of columns, and <code class="java">cell_size</code> is the length of a placeholder for one cell.</p>

<h2>Examples</h2>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1</strong></p>

<pre><code class="language-no-highlight">Enter your board dimensions: &gt; 6 5
Enter the knight's starting position: &gt; 4 2
 ---------------------
5| __ __ __ __ __ __ |
4| __ __ __ __ __ __ |
3| __ __ __ __ __ __ |
2| __ __ __  X __ __ |
1| __ __ __ __ __ __ |
 ---------------------
    1  2  3  4  5  6</code></pre>

<p><strong>Example 2</strong></p>

<pre><code class="language-no-highlight">Enter your board dimensions: &gt; 4 4
Enter the knight's starting position: &gt; 8 8
Invalid position!
Enter the knight's starting position: &gt; -1 2
Invalid position!
Enter the knight's starting position: &gt; 2 2
 ---------------
4| __ __ __ __ |
3| __ __ __ __ |
2| __  X __ __ |
1| __ __ __ __ |
 ---------------
    1  2  3  4</code></pre>

<p><strong>Example 3</strong></p>

<pre><code class="language-no-highlight">Enter your board dimensions: &gt; 10 10
Enter the knight's starting position: &gt; 5 5
  -------------------------------------------
10| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 9| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 8| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 7| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 6| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 5| ___ ___ ___ ___   X ___ ___ ___ ___ ___ |
 4| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 3| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 2| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 1| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
  -------------------------------------------
      1   2   3   4   5   6   7   8   9  10</code></pre>
