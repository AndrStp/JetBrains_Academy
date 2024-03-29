<h1>Stage 4/4: Party is over</h1>

<h2>Description</h2>

<p>It's the right time to update your dictionary with new split values to make our "Who is lucky?" feature better. First, we need to recalculate the split value for everyone. Make sure that our lucky one pays <code class="java">0</code>.</p>

<p>Recalculate the split value for <code class="java">n-1</code> people where <code class="java">n</code> is the total length of the dictionary and update the values in the dictionary with the new split value for everyone.</p>

<p>If a user decides not to use the "Who is lucky" feature, print the original dictionary.</p>

<h2>Objectives</h2>

<p>In this stage your program should perform the following steps together with the steps from the previous stages:</p>

<ol>
	<li>In case of an invalid number of people, <code class="java">"No one is joining for the party"</code> is expected as an output;</li>
	<li>Otherwise, if the user choice is  <code class="java">Yes</code>, re-split the bill according to the feature;</li>
	<li>Round up the split value to two decimal places;</li>
	<li>Update the dictionary with new split values and <code class="java">0</code> for the lucky person;</li>
	<li>Print the updated dictionary;</li>
	<li>If the user entered anything else instead of  <code class="java">Yes</code>, print the original dictionary.</li>
</ol>

<h2>Examples</h2>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<p><strong>Example 1: </strong><em>The feature is used</em></p>

<pre><code class="language-no-highlight">
Enter the number of friends joining (including you):
&gt; 5

Enter the name of every friend (including you), each on a new line:
&gt; Marc
&gt; Jem
&gt; Monica
&gt; Anna
&gt; Jason

Enter the total bill value:
&gt; 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
&gt; Yes

Jem is the lucky one!

{'Marc': 25, 'Jem': 0, 'Monica': 25, 'Anna': 25, 'Jason': 25}
</code></pre>

<p><strong>Example 2: </strong><em>The feature is skipped</em></p>

<pre><code class="language-no-highlight">
Enter the number of friends joining (including you):
&gt; 5

Enter the name of every friend (including you), each on a new line:
&gt; Marc
&gt; Jem
&gt; Monica
&gt; Anna
&gt; Jason

Enter the total bill value:
&gt; 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
&gt; No

No one is going to be lucky

{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}
</code></pre>

<p><strong>Example 3:</strong><em> Invalid input</em></p>

<pre><code class="language-no-highlight">
Enter the number of friends joining (including you):
&gt; 0

No one is joining for the party</code></pre>
