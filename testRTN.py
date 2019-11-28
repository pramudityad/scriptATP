# $language = "python"
# $interface = "1.0"

# This script demonstrates how to open a text file and read it line by
# line to a server.

# config
impacted_Abis = ['10.108.4.195']
impacted_IuB_UP = ['10.108.4.210']
impacted_LTE = ['10.108.4.226']
impacted_OM = ['10.108.4.242']
impacted_NMS = []
impacted_RTN = []

BSC = ['10.161.112.12']
RNC = ['10.189.95.28']
MME = ['10.205.41.225', '10.205.42.225', '10.205.43.225']
OM = ['10.24.127.65']

# DO NOT CHANGE
NMS = '10.23.32.67'
RTN = '10.23.32.186'


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