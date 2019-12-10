# $language = "python"
# $interface = "1.0"

# This script demonstrates how to open a text file and read it line by
# line to a server.

impacted_Abis_IP = ['10.108.223.66']
impacted_IuB_UP = ['10.108.223.82']
impacted_LTE = ['10.108.223.98']
impacted_OM = ['10.108.223.114']
impacted_NMS = []
impacted_Ipaso = []

BSC = ['10.161.216.27']
RNC = ['10.188.121.156']
MME = ['112.215.164.121','112.215.164.136']
OM = ['10.24.127.55']

# DO NOT CHANGE
NMS = '10.23.32.67'
IPASO = '10.23.40.200'

def main():
	crt.Screen.Synchronous = True

# context Abis_IP
	crt.Screen.Send('context Abis_IP'+ '\r')
	crt.Screen.WaitForString('context Abis_IP')
	crt.Screen.Send('sh ip route all summary'+ '\r')
	crt.Screen.WaitForString('sh ip route all summary')
	crt.Screen.Send('sh ip arp'+ '\r')
	crt.Screen.WaitForString('sh ip arp')
	# ping to Sites
	for ip_Abis in impacted_Abis_IP:
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

# context IPASO
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('\r')
	crt.Screen.Send('context Inband-IPaso'+ '\r')
	crt.Screen.Send('sh ip route all summary'+ '\r')
	crt.Screen.WaitForString('sh ip route all summary')
	crt.Screen.Send('sh ip arp'+ '\r')
	crt.Screen.WaitForString('sh ip arp')
	# ping to Sites
	for ip_ipaso in impacted_Ipaso:
		crt.Screen.Send('ping ' + ip_ipaso + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)
	# ping NMS IPASO
	crt.Screen.Send('ping '+ IPASO +'\r')
	if crt.Screen.ReadString('5 packets transmitted'):
		pass
	else:
		crt.Screen.WaitForString('round-trip min/avg/max/stddev')
		crt.Sleep(2)

main()