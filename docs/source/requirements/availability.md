<br>

# Availability

<br>

The [systems engineering body of knowledge defines availability](https://sebokwiki.org/wiki/System_Reliability,_Availability,_and_Maintainability#Availability) as the

> "… probability that a repairable system or system element is operational at a given point-in-time under a given set of environmental conditions"

**Herein, define the system's availability expectations**.  Availability is a function of reliability and maintainability, i.e.,

$$
availability = \frac{MTBF}{MTBF + MTTR}
$$

whereby 

* The _mean time between failure_ is a reliability metric.
* The _mean time to repair_ is a maintainability metric.


```{image} ../../../../../assets/availability-metrics.png
:alt: Availability Metrics
:width: 80%

```

<br>
<br>

<figure>
<figcaption><a href="https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/understanding-availability.html" target="_blank">Availability metrics illustration by Amazon.</a>  Note: MTBF (Mean Time Between Failure) is a reliability metric, MTTR (Mean Time To Repair) is a maintainability metric, MTBF/(MTBF + MTTR) is a definition of availability, MTTD (Mean Time To Detection)
</figcaption>
</figure>

<br>

<details><summary><b>References</b></summary>
<ol>
<li><a href="https://sebokwiki.org/wiki/Availability_(glossary)" target="_blank">Availability</a></li>
<li><a href="https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/understanding
-availability.html" target="_blank">Understanding Availability</a></li></ol>
</details>



<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
