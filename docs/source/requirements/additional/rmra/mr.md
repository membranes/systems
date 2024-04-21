<br>

# Maintainability & Resilience

<br>

## Definitions

### Maintainability

In the systems engineering body of knowledge the [basic definition of maintainability](https://sebokwiki.org/wiki/System_Reliability,_Availability,_and_Maintainability#Maintainability) is the

> “ … probability that a given maintenance action for an item under given usage conditions can be performed within a stated time interval when the maintenance is performed under stated conditions using stated procedures and resources.”

Note that **maintainability comprises** serviceability & repairability, i.e.,

> "… the ease of conducting scheduled inspections and servicing"

**and**

> "… the ease of restoring service after a failure"

<br>

### Resilience

The resilience of a system can be defined as "… the ability to maintain [capability](https://sebokwiki.org/wiki/Capability_(glossary)) in the face of a [disruption](https://sebokwiki.org/wiki/Disruption_(glossary))" [[The Systems Engineering Body of Knowledge.](https://sebokwiki.org/wiki/System_Resilience#Definition)]

The body of knowledge outlines the objectives of a system's resilience plan. Study the Achieving Resilience details, therein the fundamental objectives are:

* Avoid: eliminate or reduce exposure to [stress](https://sebokwiki.org/wiki/Stress_(glossary))
* Withstand: resist capability degradation when stressed
* Recover: replenish lost capability after degradation

<br>
<br>

## Outlining Specifications for Machine Learning Systems

**In the context of machine learning**, the foci herein are

* **The model drift and data drift strategy**.  The blog [Model Drift: Best Practices to Improve Machine Learning Model Performance](https://encord.com/blog/model-drift-best-practices/) includes an excellent discussion about how to monitor machine learning systems.  Drift details must be outlined vis-à-vis model drift and data drift.  Model drift monitoring is via the evaluation metrics detailed in the <a href="../../../model/evaluation/performance/criteria.html">model performance metrics</a> section.  Whereas data drift is generally via statistical tests or custom models, depending on the data types in question.

* **Continuous performance improvement strategy**.  For continuous model improvement purposes, the system architecture should include a re-training component.  If it does not, the monitoring system should have an automatic end-of-life alert, triggered by one or more evaluation metrics falling-out of their constraints.

* **Maintenance services/agreements**.  For general maintainability concepts, study the [reliability, maintainability, and availability page](https://sebokwiki.org/wiki/System_Reliability,_Availability,_and_Maintainability) of the systems engineering body of knowledge for the expectations herein; **and the maintenance and resilience metrics thereof**.  

Define maintenance and resilience metrics vis-a-vis

* The System/Product
* Model Drift & Data Drift

The references link to metrics definitions examples.

<br>

<details><summary><b>References</b></summary>
<ol>
    <li><a href="https://www.maintworld.com/Applications/5-Important-Maintenance-Metrics-and-How-To-Use-Them" target="_blank">Maintenance Metrics</a></li>
    <li><a href="https://sebokwiki.org/wiki/System_Resilience#Metrics" target="_blank">Resilience Metrics</a></li>
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
