# Sparkify Analytics 

<b>Sparkify</b> is an international media services provider  
It's primary business is to build an <b>audio streaming</b> platform that provides music, videos and podcasts from record labels and media companies  

## Challenge

Sparkify wants to better serve its users and thus needs to analyze the data collected on songs and user activity on their music streaming app. 
The analytical goal is to understand what songs users are listening to  

## Architecture 

Currently, the data resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. 
This architecture doesn't provide an easy way to query the data  

## Analytics goals 

Sparkify wants to create a <b>Postgres database</b> with tables designed to optimize queries on song play analysis  
The main idea is to create a <b>(OLAP-oriented) database schema</b> to support their analytical needs and <b>ETL pipeline</b> to populate it from their metadata and logs  

## Scripts

Run the following commands in the terminal:  
* `python create_tables.py` to create the sparkify database and the corresponding tables
* `python etl.py` to process the files (logs/songs) stored  

At the end the database can be requested for analysis purposes  