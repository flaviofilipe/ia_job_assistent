from tasks import configure, get_acction, execute_command, get_assistent_name
from robo import Robo


def run_assistent(robo: Robo):
    try:
        command = get_acction(robo.listen())
        execute_command(command, robo)
    except Exception as e:
        print(e)
        
    run_assistent(robo)

def main():
    configure()
    assistent_name = get_assistent_name()
    robo = Robo(assistent_name)
    run_assistent(robo)


if __name__ == '__main__':
    main()
