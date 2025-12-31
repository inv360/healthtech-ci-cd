def risk_level(bp, sugar):
    if bp > 140 or sugar > 200:
        return "HIGH"
    return "NORMAL"
