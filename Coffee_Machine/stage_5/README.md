<h1>Stage 5/6: Keep track of the supplies</h1>

<h2 style="text-align: center;">Description</h2>

<p>Just one action is not so interesting, is it? Let's improve the program so it can do multiple actions, one after another. It should repeatedly ask a user what they want to do. If the user types <code class="java">"buy"</code>, <code class="java">"fill"</code> or <code class="java">"take"</code>, then the program should do exactly the same thing it did in the previous step. However, if the user wants to switch off the coffee machine, they should type <code class="java">"exit"</code>. The program should terminate on this command. Also, when the user types <code class="java">"remaining"</code>, the program should output all the resources that the coffee machine has.</p>

<h2 style="text-align: center;">Objectives</h2>

<p>Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. Introduce two new options: <code class="java">"remaining"</code> and <code class="java">"exit"</code>.</p>

<p>Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, the program should output a message that says it can't make a cup of coffee.</p>

<p>And the last improvement to the program at this step — if the user types <code class="java">"buy"</code> to buy a cup of coffee and then changes his mind, they should be able to type <code class="java">"back"</code> to return into the main cycle.</p>

<h2 style="text-align: center;">Example</h2>

<p>Your coffee machine should have the same initial resources as in the example (<em>400 ml</em> of water, <em>540 ml</em> of milk, <em>120 g</em> of coffee beans, <em>9</em> disposable cups, <em>$550</em> in cash).</p>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that it's not part of the input.</p>

<pre><code class="language-no-highlight">
Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
&gt; buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
&gt; 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
&gt; buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
&gt; 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit):
&gt; fill

Write how many ml of water do you want to add:
&gt; 1000
Write how many ml of milk do you want to add:
&gt; 0
Write how many grams of coffee beans do you want to add:
&gt; 0
Write how many disposable cups of coffee do you want to add:
&gt; 0

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
1050 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
&gt; buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
&gt; 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit):
&gt; take

I gave you $564

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
0 of money

Write action (buy, fill, take, remaining, exit):
&gt; exit</code></pre>
