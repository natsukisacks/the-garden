WIDTH = 1230
HEIGHT = 720
FPS = 60
TILESIZE = 64

WORLD_MAP = [
  # the topleft of the first x has the position (0, 0)
  # the second on has position (64, 0) since tile size = 64
  ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
  ["x", " ", " ", " ", " ", " ", " ", " ", "x"],
  # TL of player is at (128 128)
  ["x", "x", "p", " ", "x", " ", " ", " ", "x"],
  ["x", "x", " ", " ", "x", " ", " ", " ", "x"],
  ["x", "x", " ", " ", "x", " ", " ", " ", "x"],
  ["x", "x", " ", " ", "x", " ", " ", " ", "x"],
  ["x", "x", " ", " ", "x", "x", "x", " ", "x"],
  ["x", "x", " ", " ", " ", " ", " ", " ", "x"],
  ["x", "x", "x", "x", "x", "x", "x", "x", "x"]
]