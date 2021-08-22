from run import main
from io import StringIO
import sys, io



class TestRuntime:
    def test_run_example_a(self, monkeypatch, capsys):
        example = "PLACE 0,0,NORTH\n" + \
                  "MOVE\n" + \
                  "REPORT\nbye\n"

        monkeypatch.setattr(sys, 'stdin', io.StringIO(example))

        main()
        out, err = capsys.readouterr()
        assert out == "0,1,NORTH\n"

    def test_run_example_b(self, monkeypatch, capsys):
        example = "PLACE 0,0,NORTH\n" + \
                  "LEFT\n" + \
                  "REPORT\n" + \
                  "bye\n"

        monkeypatch.setattr(sys, 'stdin', io.StringIO(example))

        main()
        out, err = capsys.readouterr()
        assert out == "0,0,WEST\n"

    def test_run_example_c(self, monkeypatch, capsys):
        example = "PLACE 1,2,EAST\n" + \
                  "MOVE\n" + \
                  "MOVE\n" + \
                  "LEFT\n" + \
                  "MOVE\n" + \
                  "REPORT\n" + \
                  "bye\n"

        monkeypatch.setattr(sys, 'stdin', io.StringIO(example))

        main()
        out, err = capsys.readouterr()
        assert out == "3,3,NORTH\n"
