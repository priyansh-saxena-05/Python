from unittest.mock import patch
from pytest_service import Yes


@patch('pytest_service.MyFile')
@patch('pytest_service.MyClass')
def test_values(mock_myclass, mock_myfile):
    mock_instance_file = mock_myfile.return_value
    mock_instance_file.calculate.return_value = {"myfile": 100}
    mock_instance_class = mock_myclass.return_value
    mock_instance_class.calculate.return_value = {"myclass": 200}
    yes = Yes()
    result = yes.values(10, 20)
    assert result == {"resp": {"myfile": 100, "myclass": 200}}
