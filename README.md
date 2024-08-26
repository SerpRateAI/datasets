# datasets

This repo contains constructed data sets from the SerpRateAI project.

## Contributing a dataset

In order to contribute a dataset, you will need to:

1. Update the README file to include the an entry in the dataset table as well as a subsection with the Data set name describing the dataset itself (e.g., column descriptions)
2. A single data file for the data set, if there are multiple data files these should each be considered their own data set

These should be committed on their own branch and a pull request is made per data set to merge with main.

# Data

| **Data set** | **time period** | Sample rate | Number of Samples | **source** |
|--------------|-----------------|-------------|-------------------|------------|
| Bubbles      | May 2019 - Feb 2020 | events | 2434 | Bubble detection catalog from BA1B for Aiken et al., 2022 |

## Bubbles
This is the dataset from Aiken et al., 2022 for the bubbles detected in BA1B.

It was constructed by using a detected bubble as a template and then used a matched filter template matching algorithm to find the other bubbles.

It has the following columns:

1. *time* - a datetime column for the detection time of the bubble
2. *similarity* - the cross correlation similarity with the origin bubble event
3. *template_id* - the template ID for the detected events, there was only one bubble template so this column is always 0
4. *ones* - a column of 1s to make a cumulative count plot easy to make
