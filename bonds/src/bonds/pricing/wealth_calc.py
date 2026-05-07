def calculate_wealth_with_subperiods(
    investment: float, n_periods: int, coupon_rate: float
):
    """
    Calculate compound interest earned on interest paid in sub periods

    Args:
      investment (float): The initial investment amount
      n_periods (int): The amount of interest payments in one period
      coupon_rate (float): The interest rate paid on the investment
    """
    return (investment + (coupon_rate / n_periods)) ** n_periods


def calculate_effective_rate(
    investment: float, n_periods: int, coupon_rate: float
):
    """
    Calculate the effective rate `r` that is needed to obtain the same
    end-of-period wealth in comparison to the sub periods
    """
    return (
        ((investment + (coupon_rate / n_periods)) ** n_periods)
        - investment
    )
