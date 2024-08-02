from hsr_simulation.hunt.topaz import simulate_turns_for_topaz, Topaz, Numby


def test_simulate_turns_with_default_parameters():
    # Given
    topaz = Topaz()
    numby = Numby(topaz)
    max_cycles = 5
    simulate_round = 1

    # When
    result = simulate_turns_for_topaz(topaz, numby, max_cycles, simulate_round)

    # Then
    assert isinstance(result, dict)
    assert 'DMG' in result
    assert 'DMG_Type' in result
    assert 'Simulate Round No.' in result
    assert len(result['DMG']) > 0
    assert len(result['DMG_Type']) > 0
    assert len(result['Simulate Round No.']) > 0


def test_simulate_turns_with_zero_max_cycles():
    # Given
    topaz = Topaz()
    numby = Numby(topaz)
    max_cycles = 0
    simulate_round = 1

    # When
    result = simulate_turns_for_topaz(topaz, numby, max_cycles, simulate_round)

    # Then
    assert isinstance(result, dict)
    assert 'DMG' in result
    assert 'DMG_Type' in result
    assert 'Simulate Round No.' in result
    assert len(result['DMG']) == 0
    assert len(result['DMG_Type']) == 0
    assert len(result['Simulate Round No.']) == 0