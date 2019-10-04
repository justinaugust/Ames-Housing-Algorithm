# Ames Housing Price Prediction Model Recommendation

_Justin August_


## Problem statement

Zillow is moving into a new market and needs a new algorithm to effectively price houses based on their data. Currently the company has metadata for over 2,000 homes with 80 columns of data for each home.

The goal is to develop an algorithm to be used in a production application to estimate the price of a home based on metadata about the property & determine the potential for generalizability.

## Description of Data
    
- [Ames Housing Data](./data/train.csv) ([source](https://www.kaggle.com/c/dsi-us-9-project-2-regression-challenge/data))

	>This data includes housing features and sale prices for houses in Ames, Iowa

A full data dictionary can be found [here](https://www.kaggle.com/c/dsi-us-9-project-2-regression-challenge/data)

Target Variable: `logsaleprice`
>The `saleprice` feature was not normally distributed so the natural log() was applied to it to create an evenly distributed target.

<img src="resources/log_saleprice.png" />

| | OLS Model|Ridge & Random Forest Feature Selection|
|-----|-----|-----|
|Untouched Features|21|4|
|Transformed Features|5|11|
|Interaction Features|2|92|



Predictive Features:
>`lot_frontage`, `lot_area`, `alley`, `year_built`, `ms_zoning lot_shape`, `ms_zoning bldg_type`, `ms_zoning bsmtfin_sf_2`, `lot_frontage^2`, `lot_frontage lot_shape`, `lot_frontage land_slope`, `lot_frontage bldg_type`, `lot_frontage overall_cond`, `lot_frontage year_built`, `lot_frontage foundation`, `lot_frontage bsmt_cond`, `lot_frontage bsmtfin_sf_2`, `lot_area^2`, `lot_area lot_shape`, `lot_area utilities`, `lot_area condition_1`, `lot_area bldg_type`, `lot_area overall_cond`, `lot_area year_remod/add`, `lot_area foundation`, `lot_area bsmt_cond`, `lot_area bsmtfin_sf_1`, `lot_area bsmtfin_type_2`, `lot_area bsmtfin_sf_2`, `lot_area bsmt_unf_sf`, `street bsmtfin_sf_2`, `street bsmt_unf_sf`, `alley^2`, `alley lot_shape`, `alley land_slope`, `alley bldg_type`,  `alley overall_cond`, `alley year_remod/add`, `alley foundation`, `alley bsmt_cond`, `alley bsmtfin_type_2`, `alley bsmtfin_sf_2`, `lot_shape^2`, `lot_shape condition_1`, `lot_shape bldg_type`, `lot_shape overall_cond`, `lot_shape year_built`, `lot_shape year_remod/add`, `lot_shape mas_vnr_area`, `lot_shape exter_qual`, `lot_shape bsmtfin_sf_1`, `lot_shape bsmtfin_sf_2`, `lot_shape bsmt_unf_sf`, `utilities^2`,  `utilities condition_1`, `utilities bldg_type`, `utilities year_remod/add`, `utilities foundation`, `utilities bsmtfin_sf_2`, `land_slope overall_cond`, `land_slope year_built`, `land_slope year_remod/add`, `land_slope mas_vnr_area`, `land_slope exter_qual`, `land_slope foundation`, `land_slope bsmt_cond`, `land_slope bsmtfin_type_2`, `condition_1^2`, `condition_1 bldg_type`, `condition_1 overall_cond`, `condition_1 mas_vnr_area`, `condition_1 foundation`, `condition_1 bsmtfin_sf_2`, `condition_1 bsmt_unf_sf`,      `bldg_type^2`, `bldg_type year_built`, `bldg_type mas_vnr_area`, `bldg_type exter_qual`, `bldg_type foundation`, `bldg_type bsmtfin_sf_1`, `overall_cond year_remod/add`, `overall_cond mas_vnr_area`, `overall_cond foundation`, `overall_cond bsmtfin_sf_1`, `overall_cond bsmtfin_sf_2`, `year_built year_remod/add`, `year_built foundation`, `year_built bsmtfin_sf_2`, `year_built bsmt_unf_sf`, `year_remod/add^2`, `year_remod/add bsmt_cond`, `year_remod/add bsmtfin_sf_1`, `year_remod/add bsmtfin_sf_2`, `mas_vnr_area^2`, `mas_vnr_area bsmt_cond`,`mas_vnr_area bsmtfin_sf_1`, `mas_vnr_area bsmtfin_sf_2`, `exter_qual^2`, `exter_qual bsmtfin_sf_2`, `foundation^2`, `foundation bsmt_cond`, `foundation bsmtfin_sf_1`, `foundation bsmtfin_sf_2`, `bsmt_cond bsmtfin_sf_1`, `bsmt_cond bsmtfin_sf_2`, `bsmt_cond bsmt_unf_sf`, `bsmt_exposure bsmtfin_sf_2`, `bsmt_exposure bsmt_unf_sf`

## Data Cleaning & EDA
>Data Cleaning and EDA - Are missing values imputed appropriately? - Are distributions examined and described? - Are outliers identified and addressed? - Are appropriate summary statistics provided? - Are steps taken during data cleaning and EDA framed appropriately? - Does the student address whether or not they are likely to be able to answer their problem statement with the provided data given what they've discovered during EDA?



Give Flowchart of cleaning and processing

- Categorical

- Numerical


## Prepropcessing & Modeling
Started with correlations to saleprice greater than .3
<img src="resources/corrmap.png" alt="Correlation of features to sale price greater than .3" />

>Preprocessing and Modeling - Are categorical variables one-hot encoded? - Does the student investigate or manufacture features with linear relationships to the target? - Have the data been scaled appropriately? - Does the student properly split and/or sample the data for validation/training purposes? - Does the student utilize feature selection to remove noisy or multi-collinear features? - Does the student test and evaluate a variety of models to identify a production algorithm (AT MINIMUM: linear regression, lasso, and ridge)? - Does the student defend their choice of production model relevant to the data at hand and the problem? - Does the student explain how the model works and evaluate its performance successes/downfalls?




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