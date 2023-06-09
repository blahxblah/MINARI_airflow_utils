import sys
import MINARI_airflow_utils_pip


def test_ping():
    sys.argv = ['foo', '10']
    MINARI_airflow_utils_pip.ping()

