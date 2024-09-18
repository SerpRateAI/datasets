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
| Daily Precipitation | Jan 2019 - Feb 2020 | daily | 425 | https://code.earthengine.google.com/65cfcd01ee34290615a7c854a00b76f4 |
| Geology      | N/A | N/A | 690 | constructed from AI paper, Aiken et al. |

## Bubbles
This is the dataset from Aiken et al., 2022 for the bubbles detected in BA1B.

It was constructed by using a detected bubble as a template and then used a matched filter template matching algorithm to find the other bubbles.

It has the following columns:

1. *time* - a datetime column for the detection time of the bubble
2. *similarity* - the cross correlation similarity with the origin bubble event
3. *template_id* - the template ID for the detected events, there was only one bubble template so this column is always 0
4. *ones* - a column of 1s to make a cumulative count plot easy to make

## Daily Precipitation

This data set was constructed from ERA5-land daily precipitation data and the hydrobasins catchement shape files.

It has the following columns:

1. *system:time_start* - date for precipitation
2. *total_precipitation_sum* - the total accumulated precipitation for the day

## Geology

This data set is created from the AI framework paper, Aiken et al., In review.

For a full description please see the paper.

It has the following columns:

1. CORE - the core piece number
2. SECTION - the section of the core
3. Cell abundance (cells/g) - the amount of cells detected in the core
4. Mean dry electrical Resistivity (ohmm)
5. Bulk density (g/cm³) - this is a useful column for the amount of peridotite alteration present
6. AMS bulk susceptibility
7. LOI wt%
8. CO2 wt%
9. H20 wt%
10. CaCO3 calc
11. SECTION_UNIT
12. % of fractures - this is a calculated column based on the number of pixels labeled in the data
13. IMAGES
14. SEGMENTATION
15. TOP_DEPTH - the depth at the top of the core section when taken
16. ALTERATION
17. REMARKS1 REMARKS2 REMARKS4 REMARKS5 - the raw text remarks used for keyword generation
21. PnS2_sum	PnL_sum	PnP3V_sum	PnP3H_sum	PnP4_sum	PnP6V_sum	FnS2_sum	FnL_sum	FnP3V_sum	FnP3H_sum	FnP4_sum	FnP6V_sum - the calculated connectivity statistics based on different polytopes
22. UNIT_TYPE_Dunite	UNIT_TYPE_Fault rock	UNIT_TYPE_Gabbro	UNIT_TYPE_Harzburgite	UNIT_TYPE_Metagabbro	UNIT_TYPE_Other	UNIT_CLASS_OPHIO	UNIT_CLASS_UND
23. TEXTURES_Brecciated	TEXTURES_Sheared
24. GRAINSIZE_Cryptocrystalline	GRAINSIZE_Fine grained	GRAINSIZE_Medium grained	GRAINSIZE_Microcrystalline	GRAINSIZE2_Coarse grained	GRAINSIZE2_Cryptocrystalline	GRAINSIZE2_Fine grained	GRAINSIZE2_Medium grained	GRAINSIZE2_Pegmatitic
25. Alteration_dummies_50%-90%	Alteration_dummies_>90%
26. Veins	Serpentine vein	Oxidation	Carbonate veins	Network	Dyke	Black serpentinization	White veins	Open cracks	Dunite	Gabbro	Microgabbro	Green veins	Open crack	Irregular	Waxy green	Alteration	Subvertical	Fine grained	Subhorizontal	Lineation	Magnetite	Thickness	Harzburgite	Altered gabbro	Offset	Altered	Crack	Pxenites	Microbio sample	Bulk serp	Bulk	Coalescence	Waxy	Wavy	Slickensides	Alteration halo	Plagioclase	Fracture	Sheared	Pyroxenite	Striations	Branching	Blue patches	Magmatic intrusions	Hydrothermal	Rodingite	Magmatic veins	Offsets	Shearing	Dark green	Dunitic zone	SiO2	TiO2	Al2O3	Fe2O3t	MnO	MgO	CaO	Na2O	K2O	P2O5	100*Fe(III)/FeT	Vrecal	Crrecal	Co	Nirecal	Curecal	Znrecal	Srrecal	Redness	Greenness	Blueness	Y (luminance)
