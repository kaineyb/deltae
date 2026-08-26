from importlib.metadata import version as _version

__version__ = _version("deltae")

import math
from dataclasses import dataclass
from typing import Literal, TypedDict


class Lab(TypedDict):
    L: float
    a: float
    b: float


@dataclass(frozen=True)
class DeltaE2000Components:
    a1Prime: float
    a2Prime: float
    c1Prime: float
    c2Prime: float
    h1Prime: float
    h2Prime: float
    hBarPrime: float
    g: float
    t: float
    sL: float
    sC: float
    sH: float
    rT: float
    DE2000: float


def delta_e_1976(Lab1: Lab, Lab2: Lab) -> float:
    """
    Takes Lab values as a dictionary and outputs a DeltaE1976 calculation

    Example Dictionarys:
    Lab1 = {'L': 50.00, 'a': 2.6772, 'b': -79.7751}
    Lab2 = {'L': 50.00, 'a': 0.00, 'b': -82.7485}
    """

    delL = Lab1["L"] - Lab2["L"]
    dela = Lab1["a"] - Lab2["a"]
    delb = Lab1["b"] - Lab2["b"]
    result = math.sqrt(delL * delL + dela * dela + delb * delb)
    return result


def delta_e_94(
    Lab1: Lab,
    Lab2: Lab,
    application: Literal["graphic_arts", "textiles"] = "graphic_arts",
) -> float:
    """
    Takes Lab values as a dictionary and outputs a DeltaE94 (CIE94) calculation

    Example Dictionarys:
    Lab1 = {'L': 50.00, 'a': 2.6772, 'b': -79.7751}
    Lab2 = {'L': 50.00, 'a': 0.00, 'b': -82.7485}

    Lab1 is treated as the reference color and Lab2 as the sample. Unlike
    delta_e_1976 and delta_e_2000, CIE94 is not symmetric: sC and sH are
    weighted by the reference's chroma (c1) rather than an average of both
    colors, so delta_e_94(Lab1, Lab2) != delta_e_94(Lab2, Lab1) in general.

    application kwarg can be 'graphic_arts' (default) or 'textiles', which
    changes kL, K1 and K2 per the CIE94 spec.

    Formula per Lindbloom (http://www.brucelindbloom.com/Eqn_DeltaE_CIE94.html)
    """

    if application == "graphic_arts":
        kL = 1.0
        K1 = 0.045
        K2 = 0.015
    elif application == "textiles":
        kL = 2.0
        K1 = 0.048
        K2 = 0.014
    else:
        raise ValueError(
            f"application must be 'graphic_arts' or 'textiles', got {application!r}"
        )

    kC = 1.0
    kH = 1.0

    dL = Lab1["L"] - Lab2["L"]
    da = Lab1["a"] - Lab2["a"]
    db = Lab1["b"] - Lab2["b"]

    c1 = math.sqrt(Lab1["a"] * Lab1["a"] + Lab1["b"] * Lab1["b"])
    c2 = math.sqrt(Lab2["a"] * Lab2["a"] + Lab2["b"] * Lab2["b"])
    dC = c1 - c2

    # dH^2 is always >= 0 mathematically; clamp to guard against floating
    # point precision making it a tiny negative value.
    dH = math.sqrt(max(0.0, da * da + db * db - dC * dC))

    sL = 1.0
    sC = 1.0 + K1 * c1
    sH = 1.0 + K2 * c1

    result = math.sqrt(
        (dL / (kL * sL)) * (dL / (kL * sL))
        + (dC / (kC * sC)) * (dC / (kC * sC))
        + (dH / (kH * sH)) * (dH / (kH * sH))
    )

    return result


def _h_prime_rochester(b: float, aPrime: float) -> float:
    if b == 0 and aPrime == 0:
        return 0
    hPrime = math.atan2(b, aPrime) * 180 / math.pi
    if hPrime < 0:
        hPrime += 360
    return hPrime


def _h_bar_prime_rochester(
    h1Prime: float, h2Prime: float, c1Prime: float, c2Prime: float
) -> float:
    if abs(h1Prime - h2Prime) <= 180 and c1Prime * c2Prime != 0:
        return (h1Prime + h2Prime) / 2

    if (
        abs(h1Prime - h2Prime) > 180
        and (h1Prime + h2Prime) < 360
        and c1Prime * c2Prime != 0
    ):
        return (h1Prime + h2Prime + 360) / 2

    # NOTE: preserved as-is from the original implementation - this checks
    # c1Prime * c1Prime rather than c1Prime * c2Prime like the branches
    # above. Not changed here since fixing it would change DE2000 output;
    # flagged for a follow-up if it turns out to be a typo.
    if (
        abs(h1Prime - h2Prime) > 180
        and (h1Prime + h2Prime) >= 360
        and c1Prime * c1Prime != 0
    ):
        return (h1Prime + h2Prime - 360) / 2

    if (c1Prime * c2Prime) == 0:
        return h1Prime + h2Prime


def _h_prime_bruce(b: float, aPrime: float) -> float:
    hPrime = (math.atan2(b, aPrime) * 180.0) / math.pi
    if hPrime < 0.0:
        hPrime += 360.0
    return hPrime


def _h_bar_prime_bruce(h1Prime: float, h2Prime: float) -> float:
    if abs(h1Prime - h2Prime) > 180.0:
        return 0.5 * (h1Prime + h2Prime + 360.0)
    return 0.5 * (h1Prime + h2Prime)


def _print_verbose(
    Lab1: Lab,
    Lab2: Lab,
    cBar: float,
    cBar7: float,
    components: DeltaE2000Components,
) -> None:
    decoration = "-" * 20

    print(decoration)
    print("LAB Value Input")
    print(decoration)
    print(f"LAB1: {Lab1['L']}, {Lab1['a']}, {Lab1['b']}")
    print(f"LAB2: {Lab2['L']}, {Lab2['a']}, {Lab2['b']}")
    print(decoration)
    print("Outputs")
    print(decoration)
    print(f"a1Prime: {round(components.a1Prime, 4)}")
    print(f"a2Prime: {round(components.a2Prime, 4)}")
    print(decoration)
    print(f"cBar: {round(cBar, 4)}")
    print(f"cBar7: {round(cBar7, 4)}")
    print(decoration)
    print(f"c1Prime: {round(components.c1Prime, 4)}")
    print(f"c2Prime: {round(components.c2Prime, 4)}")
    print(decoration)
    print(f"h1Prime: {round(components.h1Prime, 4)}")
    print(f"h2Prime: {round(components.h2Prime, 4)}")
    print(decoration)
    print(
        f"(abs)h1Prime - h2Prime: {round(abs(components.h1Prime - components.h2Prime), 4)}"
    )
    print(decoration)
    print(f"hBarPrime: {round(components.hBarPrime, 4)}")
    print(f"g: {round(components.g, 4)}")
    print(f"t: {round(components.t, 4)}")
    print(f"sL: {round(components.sL, 4)}")
    print(f"sC: {round(components.sC, 4)}")
    print(f"sH: {round(components.sH, 4)}")
    print(f"rT: {round(components.rT, 4)}")
    print(decoration)
    print(f"DE2000: {round(components.DE2000, 4)}")


def _round_test_output(components: DeltaE2000Components) -> DeltaE2000Components:
    return DeltaE2000Components(
        a1Prime=round(components.a1Prime, 4),
        a2Prime=round(components.a2Prime, 4),
        c1Prime=round(components.c1Prime, 4),
        c2Prime=round(components.c2Prime, 4),
        h1Prime=round(components.h1Prime, 4),
        h2Prime=round(components.h2Prime, 4),
        hBarPrime=round(components.hBarPrime, 4),
        g=round(components.g, 4),
        t=round(components.t, 4),
        sL=round(components.sL, 4),
        sC=round(components.sC, 4),
        sH=round(components.sH, 4),
        rT=round(components.rT, 4),
        DE2000=round(components.DE2000, 4),
    )


def _delta_e_2000(
    Lab1: Lab,
    Lab2: Lab,
    verbose: bool = False,
    test: bool = False,
    formula: Literal["Rochester", "Bruce"] = "Rochester",
) -> float | DeltaE2000Components:
    """
    Full DE2000 implementation, not part of the public API - the public
    delta_e_2000 always calls this with verbose/test at their defaults and
    returns only the float.

    verbose=True prints every intermediate calculation, for manual
    debugging.

    test=True returns every intermediate value as a DeltaE2000Components
    NamedTuple (a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime,
    hBarPrime, g, t, sL, sC, sH, rT, DE2000), rounded to 4 decimal places
    to match the reference dataset - used by the test suite to check
    against the Rochester dataset pair-by-pair, not just the final DE2000.

    formula kwarg can be 'Rochester' or 'Bruce'.

    Rochester uses a different calculation for hPrime, h1Prime, h2Prime and hBarPrime than Bruce
    Read the white paper by Gaurav Sharma, Wencheng Wu and Endul N. Dala (https://hajim.rochester.edu/ece/sites/gsharma/ciede2000/ciede2000noteCRNA.pdf)
    """

    kL = 1.0
    kC = 1.0
    kH = 1.0
    lBarPrime = 0.5 * (Lab1["L"] + Lab2["L"])
    c1 = math.sqrt(Lab1["a"] * Lab1["a"] + Lab1["b"] * Lab1["b"])
    c2 = math.sqrt(Lab2["a"] * Lab2["a"] + Lab2["b"] * Lab2["b"])
    cBar = 0.5 * (c1 + c2)
    cBar7 = cBar**7
    g = 0.5 * (1.0 - math.sqrt(cBar7 / (cBar7 + 25**7)))  # 25**7 or 6103515625

    a1Prime = Lab1["a"] * (1.0 + g)
    a2Prime = Lab2["a"] * (1.0 + g)

    c1Prime = math.sqrt(a1Prime * a1Prime + Lab1["b"] * Lab1["b"])
    c2Prime = math.sqrt(a2Prime * a2Prime + Lab2["b"] * Lab2["b"])

    cBarPrime = 0.5 * (c1Prime + c2Prime)

    if formula == "Rochester":
        h1Prime = _h_prime_rochester(Lab1["b"], a1Prime)
        h2Prime = _h_prime_rochester(Lab2["b"], a2Prime)
        hBarPrime = _h_bar_prime_rochester(h1Prime, h2Prime, c1Prime, c2Prime)
    elif formula == "Bruce":
        h1Prime = _h_prime_bruce(Lab1["b"], a1Prime)
        h2Prime = _h_prime_bruce(Lab2["b"], a2Prime)
        hBarPrime = _h_bar_prime_bruce(h1Prime, h2Prime)
    else:
        raise ValueError(f"formula must be 'Rochester' or 'Bruce', got {formula!r}")

    t = (
        1.0
        - 0.17 * math.cos((math.pi * (hBarPrime - 30.0)) / 180.0)
        + 0.24 * math.cos((math.pi * (2.0 * hBarPrime)) / 180.0)
        + 0.32 * math.cos((math.pi * (3.0 * hBarPrime + 6.0)) / 180.0)
        - 0.2 * math.cos((math.pi * (4.0 * hBarPrime - 63.0)) / 180.0)
    )

    if abs(h2Prime - h1Prime) <= 180.0:
        dhPrime = h2Prime - h1Prime

    else:
        dhPrime = (
            h2Prime - h1Prime + 360.0
            if h2Prime <= h1Prime
            else h2Prime - h1Prime - 360.0
        )

    dLPrime = Lab2["L"] - Lab1["L"]
    dCPrime = c2Prime - c1Prime
    dHPrime = (
        2.0
        * math.sqrt(c1Prime * c2Prime)
        * math.sin((math.pi * (0.5 * dhPrime)) / 180.0)
    )

    sL = 1.0 + (0.015 * (lBarPrime - 50.0) * (lBarPrime - 50.0)) / math.sqrt(
        20.0 + (lBarPrime - 50.0) * (lBarPrime - 50.0)
    )

    sC = 1.0 + 0.045 * cBarPrime
    sH = 1.0 + 0.015 * cBarPrime * t

    dTheta = 30.0 * math.exp(
        -((hBarPrime - 275.0) / 25.0) * ((hBarPrime - 275.0) / 25.0)
    )

    cBarPrime7 = cBarPrime**7

    rC = math.sqrt(cBarPrime7 / (cBarPrime7 + 6103515625.0))
    rT = -2.0 * rC * math.sin((math.pi * (2.0 * dTheta)) / 180.0)

    DE2000 = math.sqrt(
        (dLPrime / (kL * sL)) * (dLPrime / (kL * sL))
        + (dCPrime / (kC * sC)) * (dCPrime / (kC * sC))
        + (dHPrime / (kH * sH)) * (dHPrime / (kH * sH))
        + (dCPrime / (kC * sC)) * (dHPrime / (kH * sH)) * rT
    )

    components = DeltaE2000Components(
        a1Prime=a1Prime,
        a2Prime=a2Prime,
        c1Prime=c1Prime,
        c2Prime=c2Prime,
        h1Prime=h1Prime,
        h2Prime=h2Prime,
        hBarPrime=hBarPrime,
        g=g,
        t=t,
        sL=sL,
        sC=sC,
        sH=sH,
        rT=rT,
        DE2000=DE2000,
    )

    if verbose:
        _print_verbose(Lab1, Lab2, cBar, cBar7, components)

    if test:
        return _round_test_output(components)

    return DE2000


def delta_e_2000(
    Lab1: Lab,
    Lab2: Lab,
    formula: Literal["Rochester", "Bruce"] = "Rochester",
) -> float:
    """
    Takes Lab values as a dictionary and outputs a DeltaE2000 calculation

    Example Dictionarys:
    Lab1 = {'L': 50.00, 'a': 2.6772, 'b': -79.7751}
    Lab2 = {'L': 50.00, 'a': 0.00, 'b': -82.7485}

    formula kwarg can be 'Rochester' or 'Bruce'.

    Rochester uses a different calculation for hPrime, h1Prime, h2Prime and hBarPrime than Bruce
    Read the white paper by Gaurav Sharma, Wencheng Wu and Endul N. Dala (https://hajim.rochester.edu/ece/sites/gsharma/ciede2000/ciede2000noteCRNA.pdf)
    """

    return _delta_e_2000(Lab1, Lab2, formula=formula)
