def get_total_resistance_left(r1, r2, r3, r4):
    """Calculates total resistance of parallel(series(r1, r2), series(r3, r4))."""
    r12 = calc_resistance_of_series_circuit(r1, r2)
    r34 = calc_resistance_of_series_circuit(r3, r4)
    return calc_resistance_of_parallel_circuit(r12, r34)


def get_total_resistance_right(r1, r2, r3, r4):
    """Calculates total resistance of series(parallel(r1, r3), parallel(r2, r4))."""
    r13 = calc_resistance_of_parallel_circuit(r1, r3)
    r24 = calc_resistance_of_parallel_circuit(r2, r4)
    return calc_resistance_of_series_circuit(r13, r24)


def calc_resistance_of_series_circuit(single_resistance, *further_resistance):
    check_for_negative_resistance(single_resistance)
    total = single_resistance
    for r in further_resistance:
        check_for_negative_resistance(r)
        total += r
    return total


def calc_resistance_of_parallel_circuit(single_resistance, *further_resistance):
    check_for_negative_resistance(single_resistance)
    if single_resistance == 0:
        return 0
    conductance = 1 / single_resistance
    for r in further_resistance:
        check_for_negative_resistance(r)
        if r == 0:
            return 0
        conductance += 1 / r

    return 1 / conductance


def check_for_negative_resistance(resistance):
    if resistance < 0:
        raise ValueError("No negative resistances are allowed!")
