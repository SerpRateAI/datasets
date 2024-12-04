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
| Hourly Precipitation | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_precip file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and Generate_Hourly_Precip.py in dataset_management folder in this repo
| Hourly Temperature 2m | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_temperature_2m file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and the Generate_Hourly_Temp2m.py file in the folder dataset_management in this repo |
| Hourly Surface Pressure | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_surface_pressure file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and the Generate_Hourly_Surface_Pressure.py file in the folder dataset_management in this repo |
| Hourly Soil Temperature (Level 1) | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_soil_temp_1 file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and the Generate_Hourly_Soil_Temp_1.py file in the folder dataset_management in this repo |
| Hourly Soil Temperature (Level 2) | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_soil_temp_2 file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and the Generate_Hourly_Soil_Temp_2.py file in the folder dataset_management in this repo |
| Hourly Soil Temperature (Level 3) | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_soil_temp_3 file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and the Generate_Hourly_Soil_Temp_3.py file in the folder dataset_management in this repo |
| Hourly Soil Temperature (Level 4) | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_soil_temp_4 file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and the Generate_Hourly_Soil_Temp_4.py file in the folder dataset_management in this repo |
| Hourly Volumetric Soil Water (Layer 1) | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_volu_soil_water_1 file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and the Generate_Hourly_Volu_Soil_Water_Layer1.py file in the folder dataset_management in this repo |
| Hourly Volumetric Soil Water (Layer 2) | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_volu_soil_water_2 file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and the Generate_Hourly_Volu_Soil_Water_Layer2.py file in the folder dataset_management in this repo |
| Hourly Volumetric Soil Water (Layer 3) | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_volu_soil_water_3 file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and the Generate_Hourly_Volu_Soil_Water_Layer3.py file in the folder dataset_management in this repo |
| Hourly Volumetric Soil Water (Layer 4) | Jan 01 2017 - Dec 31 2020 | hourly | 35064 | The hourly_volu_soil_water_4 file in https://code.earthengine.google.com/?accept_repo=users/cassandralem/tigertail-data and the Generate_Hourly_Volu_Soil_Water_Layer4.py file in the folder dataset_management in this repo |
| BA1D Pressure and Temperature | 1/18/19 11:15 - 2/29/20 17:21 | every 15 minutes | 39027 | logged from BA1D directly |
| Oman tidal data set | 2018-04-08 00:00:00 - 2020-09-04 00:45:00+00:00 | every 15 minutes | 844884 | from sohn and matter 2023 |
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

1. *datetime* - date for precipitation
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
25. Alteration_dummies_50%-90%	Alteration_dummies_>90% - columns indicating the amount of alteration according to field geologists
26. Veins	Serpentine vein	Oxidation	Carbonate veins	Network	Dyke	Black serpentinization	White veins	Open cracks	Dunite	Gabbro	Microgabbro	Green veins	Open crack	Irregular	Waxy green	Alteration	Subvertical	Fine grained	Subhorizontal	Lineation	Magnetite	Thickness	Harzburgite	Altered gabbro	Offset	Altered	Crack	Pxenites	Microbio sample	Bulk serp	Bulk	Coalescence	Waxy	Wavy	Slickensides	Alteration halo	Plagioclase	Fracture	Sheared	Pyroxenite	Striations	Branching	Blue patches	Magmatic intrusions	Hydrothermal	Rodingite	Magmatic veins	Offsets	Shearing	Dark green	Dunitic zone	SiO2	TiO2	Al2O3	Fe2O3t	MnO	MgO	CaO	Na2O	K2O	P2O5	100*Fe(III)/FeT	Vrecal	Crrecal	Co	Nirecal	Curecal	Znrecal	Srrecal - columns indicating this keyword was selected by chatgpt for this section
27. Redness	Greenness	Blueness	Y (luminance) - columns related to the image itself


## Hourly Precipitation

This data set was constructed from ERA5-land hourly precipitation data and the hydrobasins catchment shape files.

It has the following columns:

1. *datetime* - timestamp in the format YYYY-MM-DD HH:mm:ss.
2. *total_precip* - total precipitation amount during that hour, in meters (m)


## Hourly Temperature 2m

This data set was constructed from ERA5-land hourly temperature data and the hydrobasins catchment shape files.

It has the following columns:

1. *datetime* - timestamp in the format YYYY-MM-DD HH:mm:ss.
2. *temperature_2m* - temperature 2m above the surface during that hour, in degrees Kelvin (K).


## Hourly Surface Pressure

This data set was constructed from ERA5-land hourly surface pressure data and the hydrobasins catchment shape files.

It has the following columns:

1. *datetime* - timestamp in the format YYYY-MM-DD HH:mm:ss.
2. *surface_pressure* - pressure of the atmosphere on the surface of the land/sea/in-land water during that hour, in Pascals (Pa).


## Hourly Soil Temperature (Levels 1, 2, 3, 4)

These data sets were constructed from ERA5-land hourly soil temperature data and the hydrobasins catchment shape files.

Each one has the following columns:

1. *datetime* - timestamp in the format YYYY-MM-DD HH:mm:ss.
2. *soil_temperature_level_#* - temperature of the soil in level # of the ECMWF Integrated Forecasting System during that hour, in degrees Kelvin (K)


## Hourly Volumetric Soil Water (Layers 1, 2, 3, 4)

These data sets were constructed from ERA5-land hourly volumetric soil water data and the hydrobasins catchment shape files.

Each one has the following columns:

1. *datetime* - timestamp in the format YYYY-MM-DD HH:mm:ss.
2. *volumetric_soil_water_layer_#* - volume fraction of water in the soil in layer # of the ECMWF Integrated Forecasting System during that hour 

## BA1D Pressure and Temperature

This data set was logged from BA1D directly.

It has the following columns:

1. *datetime* - timestamp UTC 
2. *elapsed_sec* - the time in elapsed seconds from the start time
3. *pressure_bar* - the pressure in bars in the borehole fluid pressure
4. *temperature_c* - the temperature in celsius in the borehole fluid 

## Oman Tides

This data was calculated from water level changes in BA1D and come from Sohn and Matter, 2023.

1. *datetime* - timestamp UTC
2. *tide_nstr* - areal strain (unitless)