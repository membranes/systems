<br>

# Performance Metrics

:::{admonition} In Progress
:class: margin
<br>
:::

<br>

## Model Performance Metrics

These are the standard technical metrics.  **Referring back to the retinal images classification example**, we may define the performance metrics criteria as follows: [^metrics]

<br>

<dl><b>EXAMPLE</b><br><div style="margin-bottom: 15px; margin-top: 10px;">Based on the <b>(a)</b> error matrix measures, i.
e., True Positive, False Negative, False Positive, True Negative, and <b>(b)</b> a threshold defined as the intersection of precision & sensitivity, the expected criteria are: </div>
    <dt>Overarching Criteria</dt>
    <dd>Precision > 0.9, Sensitivity (True Positive Rate) > 0.9, Specificity (True Negative Rate) > 0.9, Youden's J Statistic > 0.9, and False Positive Rate < 0.1. </dd>
    <dt>Disaggregated Criteria</dt>
    <dd>For each class, and by the same overarching threshold value, ensure that each criterion metric value is within its defined range; as outlined above.</dd>
</dl>

<br>
<br>

## Model Card

This is for auditing purposes.  A model's model card should summarise the artefacts of the released, in-use,
in-production, model.  A model card example:

<ul class="disc">
    <li class="disc"><a href="https://arxiv.org/abs/1810.03993" target="_blank">Model Cards for Model Reporting</a></li>
    <li class="disc"><a href="https://modelcards.withgoogle.com/about">Model Cards for Model Reporting: Prototypes</a></li>
</ul>

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>


[^metrics]: **N**: # of negative cases, **P**: # of positive cases. | **TN**: True Negative, **FP**: False Positive, **FN**: False Negative, **TP**: True Positive | **TNR = TN/N**: True Negative Rate (specificity) | **FPR = FP/N**: False Positive Rate (fall out) | **FNR = FN/P**: False Negative Rate (miss rate) | **TPR = TP/P**: True Positive Rate (hit rate, sensitivity, recall)


<br>
<br>
