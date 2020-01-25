"""
test_measure.py

Unit tests for measure module.
"""
import numpy as np
import pytest
import molecool

def test_calculate_distance():
    """Test that calculate_distance function returns expected value."""
    
    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])
    
    expected_distance = 1
    
    calculated_distance = molecool.calculate_distance(r1, r2)
    
    assert calculated_distance == expected_distance

def test_calculate_distance_typeerror():
    
    r1 = [0, 0, 0]
    r2 = [1, 0, 0]
    
    with pytest.raises(TypeError):
        calculate_distance = molecool.calculate_distance(r1, r2)

def test_calculate_angle():

    rA = np.array([0, 0, -1]) 
    rB = np.array([0, 0,  0]) 
    rC = np.array([1, 0,  0]) 
    
    expected_measure = 90.0
    
    calcuated_measure = molecool.calculate_angle(rA, rB, rC, degrees=True)
    
    assert calcuated_measure == expected_measure
