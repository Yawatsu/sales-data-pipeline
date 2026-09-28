# Sales Data Pipeline

An end-to-end data cleaning pipeline built with Python and Pandas.

## Overview

This project processes raw sales data through a reproducible data-cleaning pipeline.

The pipeline loads raw CSV data, performs data quality checks, standardizes fields, converts data types, removes duplicates, validates essential records, and generates cleaned output files.

## Project Objectives

- Inspect raw sales data
- Identify potential data-quality issues
- Standardize column names and text values
- Convert dates and numeric fields
- Remove duplicate records
- Validate essential fields
- Generate a cleaned dataset
- Generate a data-quality report

## Technologies

- Python 3
- Pandas
- Git
- GitHub
- CSV

## Pipeline

```text
Raw CSV
   |
   v
Data Loading
   |
   v
Data Inspection
   |
   v
Data Cleaning
   |
   +--> Remove duplicates
   |
   +--> Standardize columns
   |
   +--> Clean text fields
   |
   +--> Convert dates
   |
   +--> Convert numeric fields
   |
   +--> Validate essential data
   |
   v
Clean CSV
   |
   v
Data Quality Report