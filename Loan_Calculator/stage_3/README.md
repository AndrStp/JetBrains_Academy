<h1>Stage 3/4: Annuity payment</h1>

<h2 style="text-align: center;">Description</h2>

<p>Let's compute all the parameters of the loan. There are at least two kinds of loan: those with annuity payment and those with differentiated payment. In this stage, you are going to calculate only the annuity payment which is fixed during the whole loan term.</p>

<p>Here is the formula:</p>

<p style="text-align: center;"><span class="math-tex">\(A_{ordinary\_annuity} = P * \dfrac{i * (1+i)^n}{(1+i)^n-1}\)</span></p>

<p>Where:</p>

<p><span class="math-tex">\(A\)</span> = annuity payment;</p>

<p><span class="math-tex">\(P\)</span> = loan principal;</p>

<p><span class="math-tex">\(i\)</span> = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01;</p>

<p><span class="math-tex">\(n\)</span> = number of payments. This is usually the number of months in which repayments will be made.</p>

<p>You are interested in four values: the number of monthly payments required to repay the loan, the monthly payment amount, the loan principal, and the loan interest. Each of these values can be calculated if others are known:</p>

<p><strong>Loan principal:</strong></p>

<p><span class="math-tex">\(P = \dfrac{A}{\left( \dfrac{i * (1+i)^n}{(1+i)^n-1} \right)}\)</span></p>

<p><strong>The number of payments:</strong></p>

<p><strong><span class="math-tex">\(n = \log_{1+i} \left( \dfrac{A}{A - i*P} \right)\)</span></strong></p>

<h2 style="text-align: center;">Objectives</h2>

<p>In this stage, you should add new behavior to the calculator:</p>

<ol>
	<li>First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.</li>
	<li>Then, you need to ask them to input the remaining values.</li>
	<li>Finally, compute and output the value that they wanted.</li>
</ol>

<p><div class="alert alert-warning">Note that the user inputs the interest rate as a percentage, for example, 11.7, so you should divide this value by 100 to use it in the formula above.</div></p>

<p>Please be careful converting "<strong>X months</strong>" to "<strong>Y years and Z months</strong>". Avoid writing "0 years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).</p>

<p>Note that in this stage, you have to ask the user to input parameters in a specific order which is provided below. Simply skip the value the user wants to calculate:</p>

<ul>
	<li>The first is the loan principal. </li>
	<li>The second is the monthly payment. </li>
	<li>The next is the number of monthly payments.</li>
	<li>The last is the loan interest.</li>
</ul>

<h2 style="text-align: center;">Examples</h2>

<p>The greater-than symbol followed by a space (<code class="java">&gt; </code>) represents the user input. Note that this is not part of the input.</p>

<p><strong>Example 1</strong></p>

<pre><code class="language-no-highlight">What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
&gt; n
Enter the loan principal:
&gt; 1000000
Enter the monthly payment:
&gt; 15000
Enter the loan interest:
&gt; 10
It will take 8 years and 2 months to repay this loan!</code></pre>

<p>Let’s take a closer look at <strong>Example 1</strong>.</p>

<p>You know the loan principal, the loan interest and want to calculate the number of monthly payments. What do you do?</p>

<p>1) You need to know the nominal interest rate. It is calculated like this:</p>

<p><span class="math-tex">\(i = \dfrac{10\%}{12 * 100\%} = 0.008333...\)</span></p>

<p>2) Now you can calculate the number of months:</p>

<p><span class="math-tex">\(n = \log_{1 + 0.008333...} \left( \dfrac{15000}{15000-0.008333... * 1000000} \right) = 97.71...\)</span></p>

<p>3) You need an integer number, so let’s round it up. Notice that the user will pay the same amount every month for 97 months, and in the 98th month the user will pay<em> 0.71...</em> of the monthly payment. So, there are 98 months to pay.</p>

<p><span class="math-tex">\(n = 98\)</span></p>

<p>4) Finally, you need to convert “98 months” to “8 years and 2 months” so that it is more readable and understandable for the user.</p>

<p><strong>Example 2</strong></p>

<pre><code class="language-no-highlight">
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
&gt; a
Enter the loan principal:
&gt; 1000000
Enter the number of periods:
&gt; 60
Enter the loan interest:
&gt; 10
Your monthly payment = 21248!</code></pre>

<p><strong>Example 3</strong></p>

<pre><code class="language-no-highlight">
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
&gt; p
Enter the annuity payment:
&gt; 8721.8
Enter the number of periods:
&gt; 120
Enter the loan interest:
&gt; 5.6
Your loan principal = 800000!</code></pre>
