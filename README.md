# sampledag_etl_airflow
Creating a ETL pipeline with Airflow using Transactional Data. Our task is to dowload transactional data from https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt, take 2 important rows, change them to uppercase and finally zip it.

DAG arguments were given at first with email address if some error happens. 

DAG is created with an id.

Tasks are creating inside Operators which can be Bash, Python etc. For simple tasks, bash is used. 

After the 4 tasks are created, pipeline is created by priortizing tasks using >>
