# $language = "python"
# $interface = "1.0"

# This script demonstrates how to open a text file and read it line by
# line to a server.

#config
ip_loopback = '10.219.160.226'

impacted_Abis = ['10.126.248.50', '10.126.248.51', '10.126.248.50', '10.126.248.55', '10.126.248.56', '10.126.248.57', '10.126.248.58', '10.126.248.60']
impacted_IuB_UP = ['10.126.248.114', '10.126.248.115', '10.126.248.117', '10.126.248.119', '10.126.248.120', '10.126.248.121', '10.126.248.123']
impacted_LTE = ['10.126.248.178', '10.126.248.179', '10.126.248.181', '10.126.248.183', '10.126.248.184', '10.126.248.185', '10.126.248.187']
impacted_OM = ['10.126.248.242', '10.126.248.243', '10.126.248.245', '10.126.248.247', '10.126.248.248', '10.126.248.249', '10.126.248.251']
impacted_NMS = []
impacted_RTN = ['10.104.35.42']

BSC = ['10.161.112.67', '10.161.112.68']
RNC = ['10.189.49.12', '10.189.49.196']
MME = ['112.215.164.1', '112.215.164.16']
OM = ['10.24.127.75']

# DO NOT CHANGE
NMS = '10.23.32.67'
RTN = '10.23.32.186'
passwd = 'Ericsson123#'

# hut kediri 
def main():
	crt.Screen.Synchronous = True
	# crt.Screen.Send('ssh ericsson@' + ip_loopback + '\r')

	# crt.Screen.WaitForString('password:')
	# crt.Screen.Send(passwd + '\r')

# context Abis_IP
	# crt.Screen.ReadString('[local]')
	# start_Abis_IP = crt.Screen.ReadString('Host')
	# stop_Abis_IP = crt.Screen.ReadString('[Abis_IP]')
	
	crt.Screen.Send('context Abis_IP'+ '\r')
	crt.Screen.WaitForString('context Abis_IP')
	crt.Screen.Send('sh ip route all summary'+ '\r')

	crt.Screen.WaitForString('sh ip route all summary')

	crt.Screen.Send('sh ip arp'+'\r')
	crt.Screen.ReadString('Host')
	n1 = crt.Screen.CurrentRow + 1
	crt.Dialog.MessageBox(str(n1))
	
	# result = crt.Screen.Get(n1, 1, n1, 40)
	
	# crt.Dialog.MessageBox(str(n1))
	# start_Abis_IP = crt.Screen.ReadString('Host')
	# stop_Abis_IP = crt.Screen.ReadString('[Abis_IP]')

	# ip_impacted = []
	# while crt.Screen.ReadString('Host'):
	# 	screenrow = crt.Screen.CurrentRow - 1
	# 	result = crt.Screen.Get(screenrow, 1, screenrow, 15)
	# 	# result ='10.126.248.51'
	# 	# ip_impacted =+ [result]
	# 	pass
	# 	if crt.Screen.ReadString('[Abis_IP]'):
	# 		n2 = crt.Screen.CurrentRow - 1
	# 		result = crt.Screen.Get(36, 1, 36, 15)
	# 		# n = n2 - n1
			
	# 		crt.Dialog.MessageBox(result)
	# 		# ip_impacted.append(result)
	# 		# for ip_Abis in ip_impacted:
	# 		# 	crt.Screen.Send('ping ' + ip_Abis + '\r')
	# 		# 	if crt.Screen.ReadString('5 packets transmitted'):
	# 		# 		pass
	# 		# 	else:
	# 		# 		crt.Screen.WaitForString('round-trip min/avg/max/stddev')
	# 		# 		crt.Sleep(2)
	# 		break

	crt.Screen.Synchronous = False

main()