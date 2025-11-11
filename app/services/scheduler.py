# algoritmo simples para alocar blocos com base na disponibilidade
def schedule_blocks(availability, total_hours):
    """
    availability: {"monday": ["18:00-20:00"], ...}
    total_hours: int
    returns: list of blocks
    """
    blocks = []
    hours_left = total_hours
    for day, windows in availability.items():
        for w in windows:
            if hours_left <= 0:
                break
            start, end = w.split("-")
            # simplistic: assume 2 hours per window
            blocks.append({"day": day, "start": start, "end": end})
            hours_left -= 2
        if hours_left <= 0:
            break
    return blocks
