# $language = "python"
# $interface = "1.0"

# Connect to an SSH server using the SSH2 protocol. Specify the
# username and password and hostname on the command line as well as
# some SSH2 protocol specific options.

host = "10.23.38.198"
user = "eiddayat"

def main():
	# Prompt for a password instead of embedding it in a script...
	#
	passwd = crt.Dialog.Prompt("Enter password for " + host, "Login", "", True)

	# Build a command-line string to pass to the Connect method.
	cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user, passwd, host)
	crt.Session.Connect(cmd)


main()