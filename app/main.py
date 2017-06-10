"""

Usage:
    dojo-rooms create_room <room_type> <room_name>...
    dojo-rooms add_person <first_name><last_name> <job_type> [--a=<wants_accommodation>] 
    dojo-rooms print_allocations [<filename>]
    dojo-rooms print_room <room_name>
    dojo-rooms load_people <filename>
    dojo-rooms reallocate_person <person_identifier> <room_type> <new_room_name>
    dojo-rooms save_state
    dojo-rooms load_state
    dojo-rooms (-i | --interactive)
    dojo-rooms (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    
"""
import sys
import cmd
from pyfiglet import Figlet
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


class MyInteractive (cmd.Cmd):
    f = Figlet(font='univers')
    intro = f.renderText('    D O J O')

    prompt = ' Dojo '
    file = None
    print(__doc__)

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = args["<room_type>"]
        room_names = args["<room_name>"]

        for name in room_names:
            result = dojo.create_room(room_type.upper(), name.upper())

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name> <job_type> [--a=<wants_accommodation>]"""
        try:

            person_name = args['<first_name>'] + ' ' + args['<last_name>']
            person_name = person_name.upper()
            job_type = args["<job_type>"]
            job_type = job_type.upper()
            accomodation = args["--a"]

            if accomodation == None:
                wants_accommodation = None
            elif (accomodation == 'y') or (accomodation == 'n'):
                wants_accommodation = accomodation.upper()
            else:
                print(
                    'Please enter --a=y(for yes) or --a=n(for no) in the wants accomodation field')

            if (job_type == 'FELLOW') or (job_type == 'STAFF'):

                result = dojo.add_person(
                    person_name, job_type, wants_accommodation)

            else:
                print('Please enter either fellow or staff for the job_type field field')
        except:
            print('Please enter the details in this order <first_name> <last_name>' 
                ' wants_accomodation(--a=y(for yes) or --a=n(for no))')

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        room_name = (args["<room_name>"]).upper()

        result = dojo.print_room(room_name)

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [<filename>]"""
        filename = args["<filename>"]

        dojo.print_allocations(filename)

    @docopt_cmd
    def do_save_state(self, args):
        '''Usage: save_state'''
        dojo.save_state()

    @docopt_cmd
    def do_load_state(self, args):
        '''Usage: load_state'''
        dojo.load_state()

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [<filename>]"""
        filename = args["<filename>"]

        dojo.print_unallocated(filename)

    

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <person_identifier> <room_type> <new_room_name>"""
        person_identifier = int(args['<person_identifier>'])
        new_room_name = (args['<new_room_name>']).upper()
        room_type = (args["<room_type>"]).upper()
    
        dojo.reallocate_person(person_identifier,new_room_name,room_type)

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_people <filename>"""
        filename = args["<filename>"]
        print(filename)

        dojo.load_people(filename)



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
       
        print('\n\n')
        print('THIS IS ANDELA')
        print('\n\n')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    # os.system("clear")
    # intro()
    MyInteractive().cmdloop()

print(opt)
