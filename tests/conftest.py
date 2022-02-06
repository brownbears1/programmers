import pytest
from airflow.models import DagBag


@pytest.fixture
def dag_bag() -> DagBag:
    return DagBag(include_examples=False)
