<br>

# Composition

In general, the questions herein should be studied before data collection.  The datasheets paper [1] notes that most of the questions:

<blockquote>
  "… are intended to provide dataset consumers with the information they need to make informed decisions about using the dataset for their chosen tasks. … the questions are designed to elicit information about compliance with the EU's General Data Protection Regulation (GDPR) or comparable regulations in other jurisdictions."
</blockquote>


<details><summary><b>References</b></summary>
<ol class="numeric">
    <li class="numeric"><a href="https://arxiv.org/abs/1803.09010v8" target="_blank">Datasheets for Datasets</a>, arXiv:1803.09010v8, 2021, updated datasheet appendix</li>
</ol>
</details>

<br>
<br>

## What does each data set instance represent?

Describe what each instance, i.e., row, of the data set represents.  Although peculiar, if the data set is multi-representational, e.g., an instance in a merchant's data base table might represent one of: (a) an online reading event, (b) an online product purchasing event, or \(c\) an online download event.  Each representation must be described.

<br>
<br>

## The # of Instances

How many instances does the data set have?

<br>
<br>

## Pre-processed?

Are any aspects of the data set pre-processed?  If yes:

<ul  class="disc">
    <li class="disc">Document the pre-processing steps.</li>
    <li class="disc">State whether the underlying raw data is available, and provide a link to the data.</li>
    <li class="disc">If available, provide a link to the pre-processing programs.</li>
</ul>

<br>
<br>

## Is the data set a sample of a larger data set?

**If yes:**

* **If the data set is representative** of the larger data set: How was representativeness verified/validated?
* **If the data set is not representative** of the larger data set, e.g., is a geographically focused subset, explain why.


<br>
<br>


## Lineage

Summarise the data set's lineage, including linkage options. [1, 2]

<details><summary><b>References</b></summary> 
<ol><li><a href="https://www.qlik.com/us/data-management/data-lineage" target="_blank">QLIK: What is data lineage?</a></li>
<li><a href="https://www.ibm.com/topics/data-lineage" target="_blank">IBM: What is data lineage?</a></li></ol>
</details>


<br>
<br>


## Licences & Fees

If applicable, summarise the data's costs.


<br>
<br>


## Profiles of Instances

Herein, the focus is a summary of the instances of a data set, e.g., for a tabular data set:

**By Field**

* The field name
* Description: What does the element of an instance denote/represent?
* Data Type
* Dictionary of a categorical data type
* Unit of Measure
* Is this a raw data field or a feature?
* Is this a target field?
* Does the field identify a sub-population?
* Column Profile: Note column profiling "… provides statistical information regarding the distribution of data values and associated patterns that are assigned to each data attribute, …".  Including "… range analysis, sparseness, format and pattern evaluation, cardinality and uniqueness analysis, value absence, abstract type recognition, and attribute overloading analysis".[1]  If a field/column has missing elements, explain why.
* A graph of the field's data distribution.


**Across Fields**

* Cross-Column Profiles: Relationships between columns.

<br>

<details><summary><b>References</b></summary>
<ol><li>5.5.2 Profiling for Data Quality Assessment, in <a href="https://www.sciencedirect.com/book/9780123742254/master-data-management" target="_blank">Master Data Management</a>, Page 96, The MK/OMG Press, 
2008</li>
<li><a href="https://www.talend.com/resources/what-is-data-profiling/" target="_blank">Data Profiling</a></li>
</ol>
</details>


<br>
<br>


## Errors

Please detail any errors, sources of noise, or redundancies.


<br>
<br>


## Recommended Data Splits for Machine Learning

Are there recommended data splits?


<br>
<br>


## Confidentiality

Does the data set contain data that might be considered confidential?  For example,
* Is the data protected by legal privilege or by doctor–patient confidentiality?
* Does the data include the content of private/non-public communications of individuals.


<br>
<br>


## Identification of Individuals

Is it possible to identify individuals directly or indirectly?

<br>
<br>

## Data Sensitivity

Does the data set include sensitive data elements?  Describe.  Examples of sensitive data elements are 
elements that directly/indirectly reveal:
* Locations.
* Financial details.
* Health details.
* Biometric profiles.
* Genetic profiles.
* Government identification codes of individuals.
* Criminal history.
* Institutionally and/or commercially sensitive data.
* Race or ethnic origin.
* Sexual orientations.
* Religious beliefs.
* Political opinions.
* Trade union memberships.
* And more.

<br>
<br>

## Distressing Data Elements

Does ``… the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?'' [1, 2]

<details><summary><b>References</b></summary>
<ol>
<li><a href="https://dl.acm.org/doi/10.1145/3458723" target="_blank">Datasheets for Datasets</a>, Communications of the ACM, 2021, Volume 64, Issue 12, pages 86 – 92</li>
<li><a href="https://arxiv.org/abs/1803.09010v8" target="_blank">Datasheets for Datasets</a>, arXiv:1803.09010v8, 2021, updated datasheet appendix</li>
</ol>
</details>

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
