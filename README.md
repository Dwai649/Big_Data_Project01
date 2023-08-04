# Big_Data_Project01
This is a Project which incorporates use of tools like Hadoop,Hbase,Sqoop,MapReduce Framework,AWS EMR,AWS EC2,AWS RDS.

The data here belongs to the Yellow Taxi which is a Cab company in USA and we have their past historical data.

Here we have processed about 6 GB of data.

The workflow of this particular project was to ingest data using sqoop from AWS RDS PostgresSQL and store it in HDFS.Then those data was imported to hbase tables with proper schema design for future analysis.

We also wrote python scripts using MRJob the MapReduce library in python to make use of the MapReduce Framework of Hadoop for aggegratuon and process large amount of data in small batch so that we get an aggregated result based on buisness requirements.


