# import the libraries

from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


#defining DAG arguments

default_args = {
    'owner': 'Nikhil Cherian',
    'start_date': days_ago(0),
    'email': ['ramesh@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

dag = DAG(
    'etl_server_access_log_processing',
    default_args=default_args,
    description='ETL Log Processing',
    schedule_interval=timedelta(days=1),
)


# define the tasks


extract = BashOperator(
    task_id='download',
    bash_command='wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt"',
    dag=dag,
)


# define the second task
transform_and_load = BashOperator(
    task_id='extract',
    bash_command='cut -d"#" -f1,4 web-server-access-log.txt > /home/project/airflow/dags/extracted-data.txt',
    dag=dag,
)


# define the third task
transform_and_load = BashOperator(
    task_id='transform',
        bash_command='tr "[a-z]" "[A-Z]" < /home/project/airflow/dags/extracted-data.txt > /home/project/airflow/dags/capitalized.txt',
    dag=dag,
)

# define the third task
transform_and_load = BashOperator(
    task_id='load',
    bash_command='zip log.zip capitalized.txt',
    dag=dag,
)


# task pipeline
download >> extract >> transform >> load