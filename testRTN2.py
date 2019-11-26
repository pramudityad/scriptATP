# $language = "python"
# $interface = "1.0"

# This script demonstrates how to open a text file and read it line by
# line to a server.

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


def main():
	crt.Screen.Synchronous = True

# context Abis_IP
	crt.Screen.Send('context Abis_IP'+ '\r')
	crt.Sleep(3)
	crt.Screen.Send('sh ip route all summary'+ '\r')
	crt.Sleep(3)
	crt.Screen.Send('sh ip arp'+ '\r')
	crt.Sleep(3)
	# ping to Sites
	for ip_Abis in impacted_Abis:
		crt.Screen.Send('ping ' + ip_Abis + '\r')
		crt.Sleep(5)
	crt.Sleep(5)
	# ping to BSC IP
	for ip_BSC in BSC:
		crt.Screen.Send('ping '+ ip_BSC +'\r')
		crt.Sleep(5)

	crt.Screen.Synchronous = False

main()