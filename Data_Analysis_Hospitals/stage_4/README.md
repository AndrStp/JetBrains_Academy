<h1>Stage 4/5: The statistics</h1>

<h2><strong style="background-color: transparent; color: #000000; font-size: 11pt; font-variant: normal;"></strong>Description</h2>

<p>You have cleared your dataset of empty rows and values. Some values have also been corrected, and now we can start a comprehensive study of our data. In this stage, we will find the main statistical characteristics of our data, consider data distributions, and so on.</p>

<p>Answer the following questions and output the answers in the specified format.</p>

<ol>
	<li>Which hospital has the highest number of patients?</li>
	<li>What share of the patients in the general hospital suffers from stomach-related issues? Round the result to the third decimal place.</li>
	<li>What share of the patients in the sports hospital suffers from dislocation-related issues? Round the result to the third decimal place.</li>
	<li>What is the difference in the median ages of the patients in the general and sports hospitals?</li>
	<li>After data processing at the previous stages, the <code class="java">blood_test</code> column has three values: <code class="java">t</code>= a blood test was taken, <code class="java">f</code>= a blood test wasn't taken, and <code class="java">0</code>= there is no information. In which hospital the blood test was taken the most often (there is the biggest number of <code class="java">t</code> in the <code class="java">blood_test</code> column among all the hospitals)? How many blood tests were taken?</li>
</ol>

<p><b>Hint</b></p>
<div id="hint-1405" style="display:none;">One of the methods to solve the last problem is <code class="java">pandas.pivot_table()</code> . Set<code class="java">aggfunc='count'</code> and read <a target="_blank" href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html" rel="noopener noreferrer nofollow">documentation</a> to set other parameters.</div></p>

<h2>Objectives</h2>

<p>Steps 1-8 are the same as steps 2-9 in the third stage. It's not necessary here to set the maximum number of columns to display. The fourth stage requires completing the following steps:</p>

<ol>
	<li>Read the CSV files with datasets.</li>
	<li>Change the column names. The column names of the sports<em> </em>and prenatal<em> </em>tables must match the column names of the general<em> </em>table.</li>
	<li>Merge the data frames into one. Use the <code class="java">ignore_index = True</code> parameter and the following order: <code class="java">general</code>, <code class="java">prenatal</code>, <code class="java">sports</code>.</li>
	<li>Delete the <code class="java">Unnamed: 0</code> column.</li>
	<li>Delete all the empty rows.</li>
	<li>Correct all the gender column values to <code class="java">f</code> and <code class="java">m</code> respectively.</li>
	<li>Replace the <code class="java">NaN</code> values in the gender column of the prenatal hospital with <code class="java">f</code>.</li>
	<li>Replace the <code class="java">NaN</code> values in the <code class="java">bmi</code>, <code class="java">diagnosis</code>, <code class="java">blood_test</code>, <code class="java">ecg</code>, <code class="java">ultrasound</code>, <code class="java">mri</code>, <code class="java">xray</code>, <code class="java">children</code>, <code class="java">months</code> columns with zeros.</li>
	<li>Answer the 1-5 questions using the <code class="java">pandas</code> library methods. Output the answers on the separate lines in the format given in the Example section.</li>
</ol>

<p>If you have corrupted CSV files, please <a target="_blank" href="https://stepik.org/media/attachments/lesson/467509/files.zip" rel="noopener noreferrer nofollow">download them</a> and unzip in your working directory.</p>

<h2>Example</h2>

<p>The input is 3 CSV files, <code class="java">test/general.csv</code>, <code class="java">test/prenatal.csv</code>, and <code class="java">test/sports.csv</code>.</p>

<p>The output: the following answers are given for reference only, the actual answers might be different.</p>

<pre><code class="language-no-highlight">The answer to the 1st question is Brighton
The answer to the 2nd question is 0.645
The answer to the 3rd question is 0.873
The answer to the 4th question is 35
The answer to the 5th question is Oxford, 178 blood tests

</code></pre>
