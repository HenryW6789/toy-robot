from myrobot.robot import Robot
import pytest

robot = Robot()
class TestParsing:
    
    def test_valid_place_cmd(self):
        (cmd, args) = robot.parse('PLACE 1,2,NORTH\n')
        assert cmd == 'PLACE'
        assert args['x'] == 1
        assert args['y'] == 2
        assert args['f'] == 'NORTH'

    def test_valid_move_cmd(self):
        (cmd, args) = robot.parse('MOVE\n')
        assert cmd == 'MOVE'
        assert args is None

    def test_valid_left_cmd(self):
        (cmd, args) = robot.parse('LEFT\n')
        assert cmd == 'LEFT'
        assert args is None

    def test_valid_right_cmd(self):
        (cmd, args) = robot.parse('RIGHT\n')
        assert cmd == 'RIGHT'
        assert args is None

    def test_valid_report_cmd(self):
        (cmd, args) = robot.parse('REPORT\n')
        assert cmd == 'REPORT'
        assert args is None

    def test_invalid_cmd(self):
        with pytest.raises(ValueError):
            (cmd, args) = robot.parse('BAD ROBOT\n')

    def test_missing_coordinates(self):
        with pytest.raises(ValueError):
            (cmd, args) = robot.parse('PLACE\n')

    def test_bad_facing_value(self):
        with pytest.raises(ValueError):
            (cmd, args) = robot.parse('PLACE 0,0,DOWN\n')

    def test_bad_x_value(self):
        with pytest.raises(ValueError):
            (cmd, args) = robot.parse('PLACE a,0,NORTH\n')

    def test_bad_y_value(self):
        with pytest.raises(ValueError):
            (cmd, args) = robot.parse('PLACE 0,b,NORTH\n')
