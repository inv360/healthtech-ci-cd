from app.eligibility import is_eligible
from app.risk import risk_level

def test_eligibility():
    assert is_eligible(20, True) is True
    assert is_eligible(16, True) is False

def test_risk():
    assert risk_level(150, 180) == "HIGH"
    assert risk_level(120, 150) == "NORMAL"
