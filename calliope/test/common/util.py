import os
import sys

import pytest

import calliope
from calliope import AttrDict


constraint_sets = AttrDict.from_yaml(os.path.join(os.path.dirname(__file__), 'constraint_sets.yaml'))

defaults = AttrDict.from_yaml(os.path.join(os.path.dirname(calliope.__file__), 'config', 'defaults.yaml'))


python36_or_higher = pytest.mark.skipif(
    sys.version_info < (3, 6),
    reason="Requires ordered dicts from Python >= 3.6"
)


def build_test_model(override_dict=None, scenario=None, model_file='model.yaml'):
    return calliope.Model(
        os.path.join(os.path.dirname(__file__), 'test_model', model_file),
        override_dict=override_dict,
        scenario=scenario
    )


def check_error_or_warning(error_warning, test_string_or_strings):
    if hasattr(error_warning, 'list'):
        output = ','.join(str(error_warning.list[i]) for i in range(len(error_warning.list)))
    else:
        output = str(error_warning.value)

    if isinstance(test_string_or_strings, list):
        result = all(test_string in output for test_string in test_string_or_strings)
    else:
        result = test_string_or_strings in output

    return result
