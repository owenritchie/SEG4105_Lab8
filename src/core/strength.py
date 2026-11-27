"""Core logic: estimate colony strength (frames of bees) from sensor readings."""

CONTRACT_MIN_FRAMES = 8.0
EMPTY_HIVE_KG = 18.0      # boxes, frames and comb with no bees
KG_PER_FRAME = 0.9        # approx. bee + brood mass per covered frame
BROOD_TEMP_C = 34.5       # a strong colony holds the brood near this temperature


def estimate_frames(weight_kg: float, temp_c: float, sound_db: float) -> float:
    """Return estimated frames of bees, clamped to 0-20."""
    weight_part = max(weight_kg - EMPTY_HIVE_KG, 0) / KG_PER_FRAME
    temp_factor = max(0.0, 1 - abs(temp_c - BROOD_TEMP_C) / 10)
    sound_factor = min(max((sound_db - 30) / 30, 0.0), 1.0)
    frames = weight_part * (0.6 + 0.25 * temp_factor + 0.15 * sound_factor)
    return round(min(max(frames, 0.0), 20.0), 1)


def meets_contract(frames: float) -> bool:
    return frames >= CONTRACT_MIN_FRAMES


def status(frames: float) -> str:
    if frames >= CONTRACT_MIN_FRAMES:
        return "OK"
    if frames >= CONTRACT_MIN_FRAMES - 1:
        return "WATCH"
    return "ALERT"
