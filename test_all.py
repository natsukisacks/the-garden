"""
Unit tests for The Garden.
"""
from telnetlib import GA
import pytest
import pygame
from model import GardenModel

pygame.init()
screen = pygame.display.set_mode((800, 500))

level_example = GardenModel.Level(screen)

points_cases = [
    (21, True),
    (1, False),
]


@pytest.mark.parametrize("points, game_over",
                         points_cases)
def test_points(points, game_over):
    """
    Test different numbers of points.

    When there are over 20 points, the game should end.

    When there are below 20 points, the game should continue.
    """
    level_example.points = points
    level_example.delete_produce()
    assert level_example.gameover == game_over


collide_cases = [
    ((400, 200), (400, 200), 6),
    ((400, 200), (400, 100), 5),
]


@pytest.mark.parametrize("player_coords, tile_coords, points",
                         collide_cases)
def test_collide(player_coords, tile_coords, points):
    """
    Test whether a collision adds 1 point.
    """
    level_example.points = 5
    player_example = GardenModel.Player(player_coords)
    tile_example = GardenModel.Tile(
        tile_coords, "graphics/potato.png", (32, 16))

    level_example.player = player_example
    level_example.kill_tiles.add(tile_example)

    level_example.delete_produce()
    assert level_example.points == points
    # pylint questions
    # test veggie pick up
