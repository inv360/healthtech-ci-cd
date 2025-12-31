from eligibility import is_eligible
from risk import risk_level

def main():
    eligible = is_eligible(25, True)
    risk = risk_level(130, 180)

    print("Eligible:", eligible)
    print("Risk Level:", risk)

if __name__ == "__main__":
    main()
