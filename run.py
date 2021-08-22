from myrobot.robot import Robot

def main():
    """Robot is ready to run!"""
    robot = Robot()

    # prompt = "\nPlease input a command (Enter 'bye' to quit):"
    prompt = ""

    while True:
        line = input(prompt)

        if line.lower() == 'bye':
            break
        else:
            try:
                (cmd, coords) = robot.parse(line)

                if cmd == 'PLACE' and robot.valid_position(coords):
                    robot.update_position(coords)
                elif not robot.init_place(): # the first command to the robot is a PLACE command?
                    raise ValueError('InvalidCommand')
                elif cmd == 'REPORT':
                    # print (robot)
                    robot.report()
                elif cmd == 'MOVE':
                    robot.move()
                else: # LEFT or RIGHT
                    robot.turn(cmd)
            except ValueError:
                print ("ERROR: InvalidCommand, Please try again!")

if __name__ == "__main__":
    main()
