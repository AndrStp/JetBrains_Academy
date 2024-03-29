<h1>Stage 6/6: Give me an answer</h1>

<h2>Description</h2>

<p>This puzzle may seem too hard, but our program will find the way, so let's delegate the solution to our program!</p>

<p>Note that some boards may not have a solution. A rectangular with a minimum dimension of 5 is guaranteed to have at least one open tour.</p>

<h2>Objectives</h2>

<p>In this stage, you should modify your program to do the following:</p>

<ol>
	<li>Set up the board.</li>
	<li>Ask the player whether they want to try the puzzle or see the solution with a line <code class="java">Do you want to try the puzzle? (y/n):</code>. If the user enters <code class="java">y</code>, proceed to step 3. If the user enters <code class="java">n</code>, proceed to step 4. In the case of any other input, ask the same question. </li>
	<li>If the player wants to try the puzzle, check whether the board has a solution. If not, print <code class="java">No solution exists!</code> and end the game. Otherwise, let the player give the puzzle a try like in the previous stage.</li>
	<li>If they want to see the solution, check whether the board has one. Print <code class="java">No solution exists!</code> in case there is none. If a solution exists, label the starting point as 1, then label each move with the next number until you have visited all the squares.</li>
	<li>If the board is big and the number of moves exceeds 9, use spaces for the extra digits and align the text to the right.</li>
</ol>

<p>The most intuitive method for the solution finder is to use recursion and backtracking. The recursive function should check the best possible move based on Warnsdorff's rule. The function should call itself from the new position, and continue to call itself until there are no more possible moves. If you've visited all the squares, then it is the solution you're looking for. If not, it means you've reached a dead end and need to go back to the previous square and check the next best possible move. Obviously, bigger boards take much longer to solve.</p>

<h2>Examples</h2>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1</strong></p>

<pre><code class="language-no-highlight">Enter your board dimensions: &gt; 4 4
Enter the knight's starting position: &gt; 2 2
Do you want to try the puzzle? (y/n): &gt; n
No solution exists!
</code></pre>

<p><strong>Example 2</strong></p>

<pre><code class="language-no-highlight">Enter your board dimensions: &gt; 4 4
Enter your knight's starting position: &gt; 2 2
Do you want to try the puzzle? (y/n): &gt; y
No solution exists!
</code></pre>

<p><strong>Example 3</strong></p>

<pre><code class="language-no-highlight">Enter your board dimensions: &gt; 5 4
Enter knight's starting position: &gt; 1 4
Do you want to try the puzzle? (y/n): &gt; y
 ------------------
4|  X __ __ __ __ |
3| __ __  5 __ __ |
2| __  3 __ __ __ |
1| __ __ __ __ __ |
 ------------------
    1  2  3  4  5
....

Enter your next move: &gt; 2 4
 ------------------
4|  *  X  *  *  * |
3|  *  *  *  *  * |
2|  *  *  *  *  * |
1|  *  *  *  *  * |
 ------------------
    1  2  3  4  5

What a great tour! Congratulations!


</code></pre>

<p><strong>Example 4</strong></p>

<pre><code class="language-no-highlight">Enter your board dimensions: &gt; 4 3
Enter the knight's starting position: &gt; 1 3
Do you want to try the puzzle? (y/n): &gt; n

Here's the solution!
 ---------------
3|  1  4  7 10 |
2| 12  9  2  5 |
1|  3  6 11  8 |
 ---------------
    1  2  3  4</code></pre>

<p><strong>Example 5</strong></p>

<pre><code class="language-no-highlight">Enter your board's dimensions: &gt; 6 6
Enter the knight's starting position: &gt; 1 6
Do you want to try the puzzle? (y/n): &gt; n

Here's the solution!
 ---------------------
6|  1 30 27 12 15 36 |
5| 28 11  2  5 26 13 |
4| 31  4 29 14 35 16 |
3| 10 21 18  3  6 25 |
2| 19 32 23  8 17 34 |
1| 22  9 20 33 24  7 |
 ---------------------
    1  2  3  4  5  6
</code></pre>
