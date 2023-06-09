"""MINARI_airflow_utils_pip 모듈.

Please put in a description of the module.

Example:
    ``MINARI_airflow_utils_pip`` 사용법은 아래와 같습니다.

        $ pip install ./

추가적인 설명은 여기에!

"""

from airflow.operators.bash import BashOperator

def gen_bash_task(name: str, cmd: str, test_dag, trigger="all_success"):
    """airflow bash task 생성
        - trigger-rules : https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#trigger-rules
    """
    bash_task = BashOperator(
        task_id=name,
        bash_command=cmd,
        trigger_rule=trigger,
        dag=test_dag
    )
    return bash_task
