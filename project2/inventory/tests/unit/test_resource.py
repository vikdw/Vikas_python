"""
Tests for Resource class
Command line: python -m pytest tests/unit/test_resource.py
"""

import pytest

from app.models import inventory


@pytest.fixture
def resource_values():
    return {
        'name': 'Parrot',
        'manufacturer': 'Pirates A-Hoy',
        'total': 100,
        'allocated': 50
    }


@pytest.fixture
def resource(resource_values):
    return inventory.Resource(**resource_values)