# Introduction

<br>

```{mermaid}
%%{ init: { 'flowchart': { 'curve': 'monotoneX'} } }%%
flowchart LR    
    id0([start]) --> id1{<span title="Does the potential project have a budget?">budget</span>} 
    id1 -- yes --> id2{<span title="Is the budget, project timebox, and the collaboration commitment plausible?">budget,<br>time</span>}
    id1 -- no --> id3([terminate])
    id2 -- no --> id3
    id2 -- yes --> id5(<span title="The project scope/design details">project<br>details</span>)
    id5 --> id6{<span title="Is the potential project addressable via machine learning, technically feasible, and economically viable?">feasible?</span>}
    id6 -- no --> id3
    id6 -- yes --> id8(next <br> steps)
    
    classDef default fill:#333333,stroke:#333333,stroke-width:0px,color:#ffffff,font-size:11pt;
```

> An illustration of considerations vis-à-vis a potential business machine learning project.  The project details inform the feasibility assessment.

<br>
<br>

The aim of these pages is to ensure that each prospective client/collaborator carefully considers the time commitment, collaboration commitment, cost, range of expertise, project details, etc., that are required for a business machine learning project. 

<br>

A project's details are especially critical to conducting a well-informed technical feasibility & economic 
viability assessment before proceeding.  It is also important to beware that the data science aspect of the project is only a part of the project, ignoring this leads to [project failures](https://www.kdnuggets.com/survey-machine-learning-projects-still-routinely-fail-to-deploy) due to, e.g.,

<ul>
    <li class="disc">Under-planning.</li>
    <li class="disc">Ambiguous project scope/design details.</li>
    <li class="disc">Project pilots that are neither informed by <b>nor</b> tests the deployment goal.</li>
    <li class="disc">Underestimating, or ignoring, cost.</li>
    <li class="disc">Ignoring the critical importance of intensive collaboration between the business, data science, operations, etc.,
teams.</li>
</ul>

<br>
<br>

One of the first sections of these pages is **Deployment Goal**.  Colleagues may question why.  Here are a few references that 
capture our experience of why business data science projects fail, and the advantages of starting with ``the end in mind'' [^deployment]

<ul>
    <li class="disc"><a href="https://pubsonline.informs.org/do/10.1287/LYTX.2023.02.04/full/" target="_blank">Why Data Science Projects Fail</a>: Practical Principles for Data Science Success, by Douglas A. Gray.  This is the first article of the excellent <a href="https://pubsonline.informs.org/action/doSearch?target=digital-object-search&content=digitalObjects&Keywords=Principles%20for%20Successful%20Analytics%20Projects" target="_blank">series</a>.</li>
    <li class="disc"><a href="https://mitpress.mit.edu/9780262048903/the-a
i-playbook/" target="_blank">The AI Play Book: Mastering the Rare Art of Machine Learning Deployment</a>, by Eric Siegel.</li>
</ul>

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>

[^deployment]: An upcoming update will include more notes.
