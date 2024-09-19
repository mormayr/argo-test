from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

# These args will get passed on to the dummy operator
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'dummy_dag',
    default_args=default_args,
    description='A simple dummy DAG',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

# Define the dummy task
dummy_task = DummyOperator(
    task_id='dummy_task',
    dag=dag,
)

# Set the task in the DAG
dummy_task
