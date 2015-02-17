import random

class Rat:
    DEFAULT_MAX_HEALTH = 100
    DEFAULT_SNIFF_DISTANCE = 5
    DEFAULT_HEALTH_DECAY = 5

    color = 1
    name = ""
    health = DEFAULT_MAX_HEALTH
    max_health = DEFAULT_MAX_HEALTH
    health_decay = DEFAULT_HEALTH_DECAY
    sniff_distance = DEFAULT_SNIFF_DISTANCE
    direction = None
    row = 0
    col = 0

    def __init__(self, color, row, col, name, max_health, health_decay, sniff_distance):
        self.color = color
        self.name = name
        self.health = max_health
        self.max_health = max_health
        self.health_decay = health_decay
        self.sniff_distance = sniff_distance
        self.row = row
        self.col = col
        self.direction = random.randint(1, 8)