from datetime import date
from decimal import Decimal
from bonds.models.bond import BaseBond


def flat_term_pv(bond: BaseBond, market_rate: Decimal, valuation_date: date):
    """
    Calculate the present value of a bond with a flat term structure.

    Assumptions:
      1. Flat Term Structure
      2. Bond is valued on a coupon data (no accrued interest)
      3. No default risk

    Formula:
        PV = Σ CF_t / (1 + r)^t

    where:
        CF_t = cash flow in period t
        r    = market discount rate / yield
        t    = time period

    FIN601 reference:
        Bond price equals the present value of all future coupon
        payments and the principal repayment. :contentReference[oaicite:0]{index=0}

    Args:
        bond (BaseBond): The bond for which to calculate pv
        market_rate (float): The term structures market rate which is assumed to be flat so constant

    """
    pv = Decimal("0.0")
    coupon_payment = bond.face_value * bond.coupon_rate
    maturity_years = bond.maturity_date.year - valuation_date.year

    msg = f"Calculating pv for default-free {maturity_years}-year bond with yearly coupon payments"
    print(msg)
    for i in range(1, maturity_years + 1):
        if i == maturity_years:
            pv += (
                (bond.face_value + coupon_payment) 
                / 
                ((1 + market_rate) ** i)
            )
            continue
        pv += (
            coupon_payment / ((1+market_rate) ** i)
        )
    return pv
