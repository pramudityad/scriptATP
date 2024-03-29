# $language = "python"
# $interface = "1.0"

# This script demonstrates how to open a text file and read it line by
# line to a server.

# config
ip_loopback = '10.219.162.34'

impacted_Abis = ['10.126.248.50', '10.126.248.51', '10.126.248.55', '10.126.248.56', '10.126.248.57', '10.126.248.58', '10.126.248.60']
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


def main():
	crt.Screen.Synchronous = True
	crt.Screen.Send('ssh ericsson@' + ip_loopback + '\r')

	crt.Screen.WaitForString('password:')
	crt.Screen.Send(passwd + '\r')

# context Abis_IP
	crt.Screen.ReadString('[local]')
	crt.Screen.Send('context Abis_IP'+ '\r')
	crt.Screen.WaitForString('context Abis_IP')
	crt.Screen.Send('sh ip route all summary'+ '\r')
	crt.Screen.WaitForString('sh ip route all summary')
	crt.Screen.Send('sh ip arp'+ '\r')
	crt.Screen.WaitForString('sh ip arp')
	# ping to Sites
	for ip_Abis in impacted_Abis:
		crt.Screen.Send('ping ' + ip_Abis + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)
	# ping to BSC IP
	for ip_BSC in BSC:
		crt.Screen.Send('ping '+ ip_BSC +'\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)

# context IuB_UP
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('context IuB_UP'+ '\r')
	crt.Screen.Send('sh ip route all summary'+ '\r')
	crt.Screen.WaitForString('sh ip route all summary')
	crt.Screen.Send('sh ip arp'+ '\r')
	crt.Screen.WaitForString('sh ip arp')
	# ping to Sites
	for ip_IuB in impacted_IuB_UP:
		crt.Screen.Send('ping ' + ip_IuB + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)
	# ping RNC IP
	for ip_RNC in RNC:
		crt.Screen.Send('ping '+ ip_RNC +'\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)

# context LTE-S1X2
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('context LTE-S1X2'+ '\r')
	crt.Screen.Send('sh ip route all summary'+ '\r')
	crt.Screen.WaitForString('sh ip route all summary')
	crt.Screen.Send('sh ip arp'+ '\r')
	crt.Screen.WaitForString('sh ip arp')
	# ping to Sites
	for ip_LTE in impacted_LTE:
		crt.Screen.Send('ping ' + ip_LTE + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)
	# ping MME IP
	for ip_MME in MME:
		crt.Screen.Send('ping '+ ip_MME +'\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)

# context OM-HWI
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('context OM-HWI'+ '\r')
	crt.Screen.Send('sh ip route all summary'+ '\r')
	crt.Screen.WaitForString('sh ip route all summary')
	crt.Screen.Send('sh ip arp'+ '\r')
	crt.Screen.WaitForString('sh ip arp')
	# ping to Sites
	for ip_OM in impacted_OM:
		crt.Screen.Send('ping ' + ip_OM + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)
	# ping OSS IP
	for ip_OSS in OM:
		crt.Screen.Send('ping '+ ip_OSS +'\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)

# context OM-Power
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('context OM-Power'+ '\r')
	crt.Screen.Send('sh ip route all summary'+ '\r')
	crt.Screen.WaitForString('sh ip route all summary')
	crt.Screen.Send('sh ip arp'+ '\r')
	crt.Screen.WaitForString('sh ip arp')
	# ping to Sites
	for ip_NMS in impacted_NMS:
		crt.Screen.Send('ping ' + ip_NMS + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)
	# ping NMS POWER
	crt.Screen.Send('ping '+ NMS +'\r')
	if crt.Screen.ReadString('5 packets transmitted'):
		pass
	else:
		crt.Screen.WaitForString('round-trip min/avg/max/stddev')
		crt.Sleep(2)

# context RTN
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('context Inband-RTN'+ '\r')
	crt.Screen.Send('sh ip route all summary'+ '\r')
	crt.Screen.WaitForString('sh ip route all summary')
	crt.Screen.Send('sh ip arp'+ '\r')
	crt.Screen.WaitForString('sh ip arp')
	# ping to Sites
	for ip_RTN in impacted_RTN:
		crt.Screen.Send('ping ' + ip_RTN + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)
	# ping U2000RTN
	crt.Screen.Send('ping '+ RTN +'\r')
	if crt.Screen.ReadString('5 packets transmitted'):
		pass
	else:
		crt.Screen.WaitForString('round-trip min/avg/max/stddev')
		crt.Sleep(2)

	crt.Screen.Synchronous = False

main()