from __future__ import annotations

from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Annotated, Literal

from pydantic import BaseModel, Field


class IssuerType(str, Enum):
    GOVERNMENT = "government"
    CORPORATE = "corporate"
    BANK = "bank"


class CouponFrequency(str, Enum):
    ANNUAL = "annual"
    SEMI_ANNUAL = "semi_annual"
    QUARTERLY = "quarterly"
    MONTHLY = "monthly" 


class Seniority(str, Enum):
    SENIOR = "senior"
    SUBORDINATED = "subordinated"


class BaseBond(BaseModel):
    """
    Generic fixed income security.

    Represents a contractual stream of cash flows
    consisting of coupon payments and principal repayment.
    """

    isin: Annotated[
        str,
        Field(
            description="International Securities Identification Number."
        ),
    ]

    issuer_name: Annotated[
        str,
        Field(
            description="Entity issuing the bond."
        ),
    ]

    issuer_type: Annotated[
        IssuerType,
        Field(
            description=(
                "Issuer category affecting default risk "
                "and market perception."
            )
        ),
    ]

    issue_date: Annotated[
        date,
        Field(
            description="Date on which the bond was issued."
        ),
    ]

    maturity_date: Annotated[
        date,
        Field(
            description=(
                "Date on which principal repayment occurs. "
                "Time to maturity is a key determinant "
                "of interest rate risk."
            )
        ),
    ]

    face_value: Annotated[
        Decimal,
        Field(
            gt=0,
            description=(
                "Principal (par/notional value) repaid at maturity."
            ),
            examples=[100, 1000],
        ),
    ]

    coupon_rate: Annotated[
        Decimal,
        Field(
            ge=0,
            description=(
                "Contractual coupon rate of the bond. "
                "Determines periodic interest payments."
            ),
            examples=[0.05],
        ),
    ]

    coupon_frequency: Annotated[
        CouponFrequency,
        Field(
            description=(
                "Frequency of coupon payments "
                "(annual, semi-annual, etc.)."
            )
        ),
    ]

    seniority: Annotated[
        Seniority,
        Field(
            description=(
                "Claim priority in bankruptcy/workout procedures."
            )
        ),
    ]

    callable: Annotated[
        bool,
        Field(
            default=False,
            description=(
                "Indicates whether the issuer has "
                "the right to redeem the bond before maturity."
            ),
        ),
    ]

    secured: Annotated[
        bool,
        Field(
            default=False,
            description=(
                "Indicates whether collateral secures the bond."
            ),
        ),
    ]

    currency: Annotated[
        str,
        Field(
            min_length=3,
            max_length=3,
            description="ISO currency code of denomination.",
            examples=["EUR", "USD"],
        ),
    ]