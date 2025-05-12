# Reddit Data Engineering Project

Data engineering project that implements an ETL process ingesting Reddit data, transforming it and saving it into a cvs file. This projects also load data to S3 Amazon service, do some extra transformations with AWS Glue and connecting it to Amazon Athena. As final step data is loaded into AWS Redshift data warehouse

The steps realized during this project includes:
- Extract data from Reddit API
- Set up and orchestate ETL processes with Apache Airflow and Celery
- Store the data in Amazon S3 using Airflow
- Implement AWS Glue for data cataloging and ETL jobs
- Query and transform data with Amazon Athena
- Set up Redshift cluster and load data into Amazon Redshift for analytics

## Architecture
![Project Architecture](project_architecture\reddit_project_architecture.png)

# Executing the project

Clone this github repository and execute this steps

Into the config folder change the file config.cfg with the credentials to consume reddit API:

```bash

[api_keys]
reddit_secret_key = <Your reddit secret key>
reddit_client_id = <Your reddit client id>

```

then execute docker compose build and up on your project's root folder:

```bash

docker-compose up -d --build

```

[Further documentation as well as steps for getting Reddit API key and steps for replicating aws infrastructure will be added soon...]