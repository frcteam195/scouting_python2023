# parser to choose the database where the table will be written
parser = argparse.ArgumentParser()
parser.add_argument("-db", "--database", help = "Choices: dev1, dev2, testing, production", required=True)
parser.add_argument("-host", "--host", help = "Host choices: aws, localhost", required=True)
args = parser.parse_args()
input_db = args.database
input_host = args.host

if input_host == "aws":
    server = "scouting.team195.com"
elif input_host == "pi-10":
    server = "10.0.20.195"
elif input_host == "localhost":
    server = "localhost"
else:
    print(input_host + " is not a invalid choice. See --help for choices")
    sys.exit()

# Read the configuration file
config = configparser.ConfigParser()
config.read('../helpers/config.ini')

# Get the database login information from the configuration (ini) file
host = config[input_host+"-"+input_db]['host']
user = config[input_host+"-"+input_db]['user']
passwd = config[input_host+"-"+input_db]['passwd']
database = config[input_host+"-"+input_db]['database']
print(host + " " + user + " " + passwd + " " + database)