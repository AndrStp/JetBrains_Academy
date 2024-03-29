<h1>Stage 5/5: Visualize it!</h1>

<h2>Description</h2>

<p>Are you ready to catch sight of your data?</p>

<p>Graphics are arguably the most accessible way to represent the data and its structure. Sometimes, it can help to find the main data patterns and deviations. We will use data visualization methods to conclude our dataset.</p>

<p>In the last stage, you need to create data visualization to answer the following questions:</p>

<ol>
	<li>What is the most common age of a patient among all hospitals? Plot a histogram and choose one of the following age ranges: 0 - 15, 15 - 35, 35 - 55, 55 - 70, or 70 - 80</li>
	<li>What is the most common diagnosis among patients in all hospitals? Create a pie chart</li>
	<li>Build a violin plot of height distribution by hospitals. Try to answer the questions. What is the main reason for the gap in values? Why there are two peaks, which correspond to the relatively small and big values? No special form is required to answer this question<br>
	There is <a target="_blank" href="https://towardsdatascience.com/violin-plots-explained-fb1d115e023d" rel="noopener noreferrer nofollow">a comprehensive explanation</a> of violin plots by Eryk Lewinson.</li>
</ol>

<p><b>Hint</b></p>
<div id="hint-1161" style="display:none;">To answer the last question think about specializations of the hospitals in the dataset and the unit of measurement of height.</div></p>

<p>Please note that the answers are independent of each other.</p>

<p>At this stage, we recommend using <code class="java">pandas</code> <a target="_blank" href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html" rel="noopener noreferrer nofollow">visualization tools</a>. However, feel free to use <code class="java">seaborn</code>, <code class="java">matplotlib</code> or any other library.</p>

<p>The tests to check graph content are very limited and we are sure that you can easily answer the questions without plotting any charts. Despite this, please be curious to answer them using graphs. It is a very valuable skill for a data scientist to plot and interpret the data.</p>

<h2>Objectives</h2>

<p>Steps 1-8 are the same as in the previous stage. The fifth stage requires completing the following steps:</p>

<ol>
	<li>Read the CSV files with datasets</li>
	<li>Change the column names. The column names of the sports<em> </em>and prenatal<em> </em>tables must match the column names of the general<em> </em>table</li>
	<li>Merge the dataframes into one. Use the <code class="java">ignore_index=True</code> parameter and the following order: <code class="java">general</code>, <code class="java">prenatal</code>, <code class="java">sports</code>.</li>
	<li>Delete the <code class="java">Unnamed: 0</code> column</li>
	<li>Delete all the empty rows</li>
	<li>Correct all the gender column values to <code class="java">f</code> and <code class="java">m</code> respectively</li>
	<li>Replace the <code class="java">NaN</code> values in the gender column of the prenatal hospital with <code class="java">f</code></li>
	<li>Replace the <code class="java">NaN</code> values in the <code class="java">bmi</code>, <code class="java">diagnosis</code>, <code class="java">blood_test</code>, <code class="java">ecg</code>, <code class="java">ultrasound</code>, <code class="java">mri</code>, <code class="java">xray</code>, <code class="java">children</code>, <code class="java">months</code> columns with zeros</li>
	<li>Answer questions 1-3. Output the answers in the specified format. The answers to the first two questions should be formatted as in the examples. No special form is required to answer the third question</li>
</ol>

<p>If you have corrupted CSV files, please <a target="_blank" href="https://stepik.org/media/attachments/lesson/467509/files.zip" rel="noopener noreferrer nofollow">download them</a> and unzip in your working directory.</p>

<h2>Example</h2>

<p>The input is 3 CSV files, <code class="java">test/general.csv</code>, <code class="java">test/prenatal.csv</code>, and <code class="java">test/sports.csv</code>.</p>

<p>The output:<br>
(The following answers are given for reference only, the actual answers might be different)</p>

<pre><code class="language-no-highlight">The answer to the 1st question: 0 - 15
The answer to the 2nd question: flu
The answer to the 3rd question: It's because...</code></pre>


