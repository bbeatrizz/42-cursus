import alchemy.grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
spell: str = "Fantasy"
args: str = "Earth, wind and fire"
print("Testing record light spell: "
      f"{alchemy.grimoire.light_spell_record(spell, args)}")
