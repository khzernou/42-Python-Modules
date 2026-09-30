from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def power_echo(target: str, power: int) -> str:
    return str(power)


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """combine two spells: casts both and return tuple of both res"""
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """return spell that multiplies power before casting base spell"""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """return spell only casts if condition(targer, power) is True"""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """return a func casts every spell with same arg"""
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def has_enough_power(target: str, power: int) -> bool:
    """only proceed if power is at least 20"""
    return power >= 20


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    fire_result, heal_result = combined("Dragon", 25)
    print(f"Combined spell result: {fire_result}, {heal_result}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(power_echo, 3)
    original_power = 10
    print(f"Original: {original_power}, "
          f"Amplified: {amplified('Dragon', original_power)}")

    print("\nTesting conditional caster...")
    guarded_fireball = conditional_caster(has_enough_power, fireball)
    print(guarded_fireball("Dragon", 25))
    print(guarded_fireball("Dragon", 5))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    for result in sequence("Dragon", 15):
        print(result)

    print(f"\nIs fireball callable? {callable(fireball)}")
    print(f"Is the string 'fireball' callable? {callable('fireball')}")


if __name__ == "__main__":
    main()
