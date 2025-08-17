MEMORY_MAP = {
    # Pokémon in party
    "party_count": 0x020244E9,

    # Pokémon 1 (each party Pokémon struct is 0x64 bytes apart)
    "party_pokemon_1": {
        "species": 0x020244EC,  # National Dex ID
        "level":   0x0202450E,  # Level
        "hp":      0x02024510,  # Current HP
        "hp_max":  0x02024514,  # Max HP
        "exp":     0x02024518,  # Experience points
        "status":  0x0202450C,  # Status condition
    },

    "money": 0x0202573C,  # 3-byte value, little endian

    # Coordinates
    "player_x": 0x02036E38,
    "player_y": 0x02036E3C,

    # Battle State
    "battle_flag": 0x02022B4C,  # 0 = overworld, >0 = in battle
}