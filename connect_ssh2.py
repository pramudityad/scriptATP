# $language = "python"
# $interface = "1.0"

# Connect to an SSH server using the SSH2 protocol. Specify the
# username and password and hostname on the command line as well as
# some SSH2 protocol specific options.

ip_loopback = '10.219.165.151'
user = "ericsson"
passwd = 'Ericsson123#'

def main():
	crt.Screen.Synchronous = True

	# for ip_loopback in open("C:\\Users\\eprmdmr\\Documents\\CSR XL\\Script\\txt\\ip_loopback.txt"):
	crt.Screen.Send('ssh ericsson@' + ip_loopback + '\r')
	# crt.Screen.WaitForString('password:')
	# crt.Screen.Send(passwd + '\r')
	# crt.Screen.Send('exit' + '\r')

	nIndex = crt.Screen.WaitForStrings('Are you sure you want to continue connecting (yes/no)?')
	
	if nIndex == 1:
		crt.Screen.Send('yes' + '\r')
	elif nIndex == 2:
		pass
	return nIndex

	crt.Screen.Send(passwd + '\r')
	
	crt.Screen.Synchronous = False

main()