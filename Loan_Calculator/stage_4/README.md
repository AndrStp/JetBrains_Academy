<h1>Stage 4/4: Differentiate payment</h1>

<h2 style="text-align: center;">Description</h2>

<p>Finally, let's add to our calculator the capacity to compute differentiated payments. We’ll do this for the type of repayment where the loan principal is reduced by a constant amount each month. The rest of the monthly payment goes toward interest repayment and it is gradually reduced over the term of the loan. This means that the payment is different each month. Let’s look at the formula:</p>

<p style="text-align: center;"><span class="math-tex">\(D_m = \dfrac{P}{n} + i * \left( P - \dfrac{P*(m-1)}{n} \right) \)</span></p>

<p>Where:</p>

<p><span class="math-tex">\(D_m\)</span> = mth differentiated payment;</p>

<p><span class="math-tex">\(P\)</span> = the loan principal;</p>

<p><span class="math-tex">\(i\)</span> = nominal interest rate. This is usually 1/12 of the annual interest rate, and it’s usually a float value, not a percentage. For example, if our annual interest rate = 12%, then i = 0.01.</p>

<p><span class="math-tex">\(n\)</span> = number of payments. This is usually the number of months in which repayments will be made.</p>

<p><span class="math-tex">\(m\)</span> = current repayment month.</p>

<p>The user has to input a lot of parameters, so it might be convenient to use command-line arguments.</p>

<p>You can run your loan calculator via command line like this:</p>

<pre><code class="language-no-highlight">
python creditcalc.py</code></pre>

<p>Using command-line arguments you can run your program this way:</p>

<pre><code class="language-no-highlight">
python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10</code></pre>

<p>This way, your program can get different values without prompting the user to input them. It can be useful when you are developing your program and trying to find a mistake, and you want to run the program with the same parameters again and again. It's also convenient if you made a mistake in a single parameter: you don't have to input all the other values again.</p>

<h2 style="text-align: center;">Objectives</h2>

<p>In this stage, you are going to implement the following features:</p>

<ul>
	<li>Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.</li>
	<li>Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.</li>
	<li>Handling of invalid parameters. It's a good idea to show an error message if the user enters invalid parameters (they are discussed in detail below).</li>
</ul>

<p>The final version of your program is supposed to work from the command line and parse the following parameters:</p>

<ul>
	<li><code class="java">--type</code> indicates the type of payment: <code class="java">"annuity"</code> or <code class="java">"diff"</code> (differentiated). If <code class="java">--type</code> is specified neither as <code class="java">"annuity"</code> nor as <code class="java">"diff"</code> or not specified at all, show the error message.

	<pre><code class="language-no-highlight">
	&gt; python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters
	</code></pre>
	</li>
	<li><code class="java">--payment</code> is the monthly payment amount. For <code class="java">--type=diff</code>, the payment is different each month, so we can't calculate months or principal, therefore a combination with <code class="java">--payment</code> is invalid, too:
	<pre><code class="language-no-highlight">
	&gt; python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters
	</code></pre>
	</li>
	<li><code class="java">--principal</code> is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.</li>
	<li><code class="java">--periods</code> denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.</li>
	<li><code class="java">--interest</code> is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. These parameters are incorrect because <code class="java">--interest</code> is missing:
	<pre><code class="language-no-highlight">
	&gt; python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters
	</code></pre>
	</li>
</ul>

<p>You may have noticed that for differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided:</p>

<pre><code class="language-no-highlight">
&gt; python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters</code></pre>

<p>You should also display an error message when negative values are entered:</p>

<pre><code class="language-no-highlight">
&gt; python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters</code></pre>

<p>The only thing left is to compute the overpayment: the amount of interest paid over the whole term of the loan. Voila: you have a real loan calculator!</p>

<h2 style="text-align: center;">Examples</h2>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that this is not part of the input.</p>

<p><strong>Example 1: </strong><em>calculating differentiated payments</em></p>

<pre><code class="language-no-highlight">&gt; 
python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837</code></pre>

<p>In this example, the user wants to take a loan with differentiated payments. You know the principal, the count of periods, and interest, which are 1,000,000, 10 months, and 10%, respectively.</p>

<p>The calculator should calculate payments for all 10 months. Let’s look at the formula above. In this case:</p>

<p><span class="math-tex">\(P = 1000000\)</span><br>
<span class="math-tex">\(n = 10\)</span><br>
<span class="math-tex">\(i = \dfrac{ interest }{ 12 * 100\% } = \dfrac { 10\% }{12 * 100\% } = 0.008333...\)</span></p>

<p>Now let’s calculate the payment for the first month:</p>

<p><span class="math-tex">\(D_1 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(1-1) }{ 10 } \right) = 108333.333...\)</span></p>

<p>The second month (<span class="math-tex">\(m = 2\)</span>):</p>

<p><span class="math-tex">\(D_2 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(2-1) }{ 10 } \right) = 107500\)</span></p>

<p>The third month (<span class="math-tex">\(m = 3\)</span>):</p>

<p><span class="math-tex">\(D_3 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(3-1) }{ 10 } \right) = 106666.666...\)</span></p>

<p>And so on. You can see other monthly payments above.</p>

<p><div class="alert alert-warning">Your loan calculator should output monthly payments for every month as in the first stage. Also, round up all floating-point values.</div></p>

<p>Finally, your loan calculator should add up all the payments and subtract the loan principal so that you get the overpayment.</p>

<p><strong>Example 2: </strong><em>calculate the annuity payment for a 60-month (5-year) loan with a principal amount of 1,000,000 at 10% interest</em></p>

<pre><code class="language-no-highlight">
&gt; python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880</code></pre>

<p><strong>Example 3: </strong><em>fewer than four arguments are given</em></p>

<pre><code class="language-no-highlight">
&gt; python creditcalc.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.</code></pre>

<p><strong>Example 4: </strong><em>calculate differentiated payments given a principal of 500,000 over 8 months at an interest rate of 7.8%</em></p>

<pre><code class="language-no-highlight">
&gt; python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
Month 1: payment is 65750
Month 2: payment is 65344
Month 3: payment is 64938
Month 4: payment is 64532
Month 5: payment is 64125
Month 6: payment is 63719
Month 7: payment is 63313
Month 8: payment is 62907

Overpayment = 14628</code></pre>

<p><strong>Example 5: </strong><em>calculate the principal for a user paying 8,722 per month for 120 months (10 years) at 5.6% interest</em></p>

<pre><code class="language-no-highlight">
&gt; python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800018!
Overpayment = 246622</code></pre>

<p><strong>Example 6: </strong><em>calculate how long it will take to repay a loan with 500,000 principal, monthly payment of 23,000, and 7.8% interest</em></p>

<pre><code class="language-no-highlight">
&gt; python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000</code></pre>
