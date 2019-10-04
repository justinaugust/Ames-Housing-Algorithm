# Ames Housing Price Prediction Model Recommendation

_Justin August_


## Problem statement

>Problem Statement - Is it clear what the student plans to do? - What type of model will be developed? - How will success be evaluated? - Is the scope of the project appropriate? - Is it clear who cares about this or why this is important to investigate? - Does the student consider the audience and the primary and secondary stakeholders?


- Create a model to accurately predict housing prices in Ames, Iowa

## Description of Data
    
- [Ames Housing Data](./data/train.csv) ([source](https://www.kaggle.com/c/dsi-us-9-project-2-regression-challenge/data))

	>This data includes housing features and sale prices for houses in Ames, Iowa

A full data dictionary can be found [here](https://www.kaggle.com/c/dsi-us-9-project-2-regression-challenge/data)

## Data Cleaning & EDA
>Data Cleaning and EDA - Are missing values imputed appropriately? - Are distributions examined and described? - Are outliers identified and addressed? - Are appropriate summary statistics provided? - Are steps taken during data cleaning and EDA framed appropriately? - Does the student address whether or not they are likely to be able to answer their problem statement with the provided data given what they've discovered during EDA?



Give Flowchart of cleaning and processing

- Categorical

- Numerical


## Prepropcessing & Modeling
Started with correlations to saleprice greater than .3
<img src="resources/corrmap.png" alt="Correlation of features to sale price greater than .3" />

>Preprocessing and Modeling - Are categorical variables one-hot encoded? - Does the student investigate or manufacture features with linear relationships to the target? - Have the data been scaled appropriately? - Does the student properly split and/or sample the data for validation/training purposes? - Does the student utilize feature selection to remove noisy or multi-collinear features? - Does the student test and evaluate a variety of models to identify a production algorithm (AT MINIMUM: linear regression, lasso, and ridge)? - Does the student defend their choice of production model relevant to the data at hand and the problem? - Does the student explain how the model works and evaluate its performance successes/downfalls?

<img src="resources/log_saleprice.png" />


## Key takeaways:
>Evaluation and Conceptual Understanding - Does the student accurately identify and explain the baseline score? - Does the student select and use metrics relevant to the problem objective? - Is more than one metric utilized in order to better assess performance? - Does the student interpret the results of their model for purposes of inference? - Is domain knowledge demonstrated when interpreting results? - Does the student provide appropriate interpretation with regards to descriptive and inferential statistics?


>Which features appear to add the most value to a home?

Undetermined

>Which features hurt the value of a home the most?

Undetermined

>What are things that homeowners could improve in their homes to increase the value?

Undetermined

>What neighborhoods seem like they might be a good investment?

Undetermined


## Generalization and Next Steps
>Conclusion and Recommendations - Does the student provide appropriate context to connect individual steps back to the overall project? - Is it clear how the final recommendations were reached? - Are the conclusions/recommendations clearly stated? - Does the conclusion answer the original problem statement? - Does the student address how findings of this research can be applied for the benefit of stakeholders? - Are future steps to move the project forward identified?

>Do you feel that this model will generalize to other cities? How could you revise your model to make it more universal OR what date would you need from another city to make a comparable model?

Housing models can be generalizable but in this case the 

## Next Steps & Additional Data Analysis


## Media Links
[Presentation Here](https://docs.google.com/presentation/d/1ksYouZabXuXNUsVuTZ9ZRGaMaEGdBNSHRsDJyKNVcgw/)