# SNF Case Study  - Team 5


DS-5360: Case Studies in Data Science

Team 5

Below is a brief overview of the repo structure and a description of the various files


```
├── README.md
├── data
│   ├── base_data							# Folder with original CSV data
│   ├── merged_data.csv						# Merged episode + SNF data
│   ├── data_with_datetime_objects.csv  # County + Episode + SNF data by week
│   ├── timeseries_base.csv				# Merged data transformed to timeseries (weekly)
│   └── timeseries_with_tasks.csv			# Timeseries data with task workload added
├── map_data									# Various files to create maps from
│   ├── county_count_monthly.csv
│   ├── county_snf_count_monthly.csv
│   ├── snfs_per_county.csv
│   └── snfs_per_county_25plus.csv
├── notebooks
│   ├── 00_merge-data.ipynb				# Create base_data.csv
│   ├── 01_explore.ipynb					# EDA of base data
│   ├── 10_create-timeseries.ipynb		# Create timeseries_base.csv
│   ├── 20a_eda-timeseries.ipynb			# EDA of timeseries data. Creates data_with_datetime_objects.csv
│   ├── 20b_eda-timeseries.ipynb			# EDA of timeseries data.
│   ├── 30_cc-analysis.ipynb				# Analysis of timeseries data + tasks for CC recommendation
│   ├── mapping.Rmd							# Create county-level maps
│   └── mapping.nb.html
└── requirements.txt
```