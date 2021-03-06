from myrobot.robot import Robot
import pytest

robot = Robot()

class TestPlacement:
    # Seamingly low value tests, since the implementation uses set membership
    # to restrict values. However, we do need to assert that the program meets
    # the "5x5 table" part of the brief, and that postioning off the table
    # should not be possible.

    def test_valid_middle(self, robot, capsys):

        robot.update_position({'x': 1, 'y': 3, 'f': 'SOUTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '1,3,SOUTH\n'

    def test_valid_edges(self, robot, capsys):

        robot.update_position({'x': 0, 'y': 3, 'f': 'SOUTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,3,SOUTH\n'

        robot.update_position({'x': 2, 'y': 0, 'f': 'SOUTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '2,0,SOUTH\n'

        robot.update_position({'x': 4, 'y': 2, 'f': 'SOUTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '4,2,SOUTH\n'

        robot.update_position({'x': 3, 'y': 4, 'f': 'SOUTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '3,4,SOUTH\n'

    def test_valid_corners(self, robot, capsys):

        robot.update_position({'x': 0, 'y': 0, 'f': 'SOUTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,SOUTH\n'

        robot.update_position({'x': 4, 'y': 0, 'f': 'SOUTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '4,0,SOUTH\n'

        robot.update_position({'x': 0, 'y': 4, 'f': 'SOUTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,4,SOUTH\n'

        robot.update_position({'x': 4, 'y': 4, 'f': 'SOUTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '4,4,SOUTH\n'

    def test_valid_direction(self, robot, capsys):

        robot.update_position({'x': 0, 'y': 0, 'f': 'NORTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,NORTH\n'

        robot.update_position({'x': 0, 'y': 0, 'f': 'WEST'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,WEST\n'

        robot.update_position({'x': 0, 'y': 0, 'f': 'SOUTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,SOUTH\n'

        robot.update_position({'x': 0, 'y': 0, 'f': 'EAST'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,EAST\n'

    def test_invalid_position(self, robot, capsys):

        # Set to known valid position.  All invalid attempts at positioning
        # should silently fail and not change the current position
        robot.update_position({'x': 0, 'y': 0, 'f': 'NORTH'})
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,NORTH\n'

class TestMovement:

    def test_valid_circuit(self, robot, capsys):
        """Traverse the edges of the board clockwise"""

        robot.update_position({'x': 0, 'y': 0, 'f': 'NORTH'})
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,4,NORTH\n'

        # robot.right()
        # robot.move()
        # robot.move()
        # robot.move()
        # robot.move()
        # robot.report()
        # out, err = capsys.readouterr()
        # assert out == '4,4,EAST\n'

        # robot.right()
        # robot.move()
        # robot.move()
        # robot.move()
        # robot.move()
        # robot.report()
        # out, err = capsys.readouterr()
        # assert out == '4,0,SOUTH\n'

        # robot.right()
        # robot.move()
        # robot.move()
        # robot.move()
        # robot.move()
        # robot.report()
        # out, err = capsys.readouterr()
        # assert out == '0,0,WEST\n'

    def test_valid_reverse_circuit(self, robot, capsys):
        """Traverse the edges of the board anti-clockwise"""

        robot.update_position({'x': 0, 'y': 0, 'f': 'EAST'})
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.report()
        out, err = capsys.readouterr()
        assert out == '4,0,EAST\n'

        robot.turn("LEFT")
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.report()
        out, err = capsys.readouterr()
        assert out == '4,4,NORTH\n'

        robot.turn("LEFT")
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,4,WEST\n'

        robot.turn("LEFT")
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,SOUTH\n'


class TestExamples:
    def test_a(self, robot, capsys):
        robot.update_position({'x': 0, 'y': 0, 'f': 'NORTH'})
        robot.move()
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,1,NORTH\n'

    def test_b(self, robot, capsys):
        robot.update_position({'x': 0, 'y': 0, 'f': 'NORTH'})
        robot.turn("LEFT")
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,WEST\n'

    def test_c(self, robot, capsys):
        robot.update_position({'x': 1, 'y': 2, 'f': 'EAST'})
        robot.move()
        robot.move()
        robot.turn("LEFT")
        robot.move()
        robot.report()
        out, err = capsys.readouterr()
        assert out == '3,3,NORTH\n'
