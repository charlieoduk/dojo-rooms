"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    dojo-rooms create_room <room_type> <room_name>...
    dojo-rooms add_person <person_name> <job_type> [--a=<wants_accommodation>] 
    dojo-rooms print_allocations [<filename>]
    dojo-rooms print_room <room_name>
    dojo-rooms (-i | --interactive)
    dojo-rooms (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from dojo import Dojo 

dojo = Dojo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

    click.echo('\n')
    click.echo()
    click.echo('*' + ' ' * 98 + '*')
    click.echo('*' + ' ' * 98 + '*')
    click.echo('*' + ' ' * 40 + 'THE WEATHER MAN!! ' + ' ' * 40+ '*')
    click.echo('*' + ' ' * 98 + '*')
    click.echo('*' + ' ' * 98 + '*')
    click.echo('*' * 100)
    click.echo('\n')


class MyInteractive (cmd.Cmd):
    intro = ''
        
    prompt = ' Dojo '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = args["<room_type>"]
        room_names = args["<room_name>"]

     
        for name in room_names:
            result = dojo.create_room(room_type.upper(),name.upper())
        

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <person_name> <job_type> [--a=<wants_accommodation>]"""
        person_name = args["<person_name>"]
        person_name = person_name.upper()
        job_type = args["<job_type>"]
        job_type = job_type.lower()
        accomodation = (args["--a"])
        wants_accommodation = ''
        position = ''
        
        if job_type == 'fellow':
            position = 'FELLOW'
        elif job_type == 'staff':
            position = 'STAFF'
        else:
            print('Please enter staff or fellow for the job_type field')
            return

        if accomodation == None:
            wants_accommodation = 'N'

        elif accomodation == 'n' or 'N':
            wants_accommodation ='N'

        elif accomodation == 'y' or 'Y':
            wants_accommodation = 'Y'
        else:
            print('Please enter either N or Y for wants_accomodation field')
            return
        

        result = dojo.add_person(person_name, position,wants_accommodation)


    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        room_name = (args ["<room_name>"]).upper()

        result = dojo.print_name(room_name)



    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [<filename>]"""
        filename = args["<filename>"]

        dojo.print_allocations(filename)
        

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [<filename>]"""
        filename = args["<filename>"]

        dojo.print_unallocated(filename)



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    # os.system("clear")
    # intro()
    MyInteractive().cmdloop()

print(opt)



