# $language = "python"
# $interface = "1.0"

# This script demonstrates how to open a text file and read it line by
# line to a server.

#config
ip_loopback = ['10.219.160.226']

BSC = ['10.161.112.20']
RNC = ['10.165.87.140']
MME = ['10.205.41.225', '10.205.42.225', '10.205.43.225']
OM = ['10.24.127.65']

# DO NOT CHANGE
NMS = '10.23.32.67'
RTN = '10.23.32.186'
passwd = 'Ericsson123#'

def main():
	crt.Screen.Synchronous = True
	# crt.Screen.Send('ssh ericsson@' + ip_loopback + '\r')

	# crt.Screen.WaitForString('password:')
	# crt.Screen.Send(passwd + '\r')

# context Abis_IP
	# crt.Screen.ReadString('[local]')	
	crt.Screen.Send('context Abis_IP'+ '\r')
	crt.Screen.WaitForString('context Abis_IP')
	crt.Screen.Send('sh ip route all summary'+ '\r')
	crt.Screen.WaitForString('sh ip route all summary')
	crt.Screen.Send('sh ip arp'+'\r')

	# ping to Sites
	if crt.Screen.ReadString('Host'):
		n1 = crt.Screen.CurrentRow
		result1 = crt.Screen.Get(n1, 1, n1, 15)
		pass
	if crt.Screen.ReadString('[Abis_IP]'):
		n2 = crt.Screen.CurrentRow
		result2 = crt.Screen.Get(n2, 1, n2, 15)		
		pass	
	i_Abis_IP = n2
	d_Abis_IP = 1
	impacted_Abis = []
	while i_Abis_IP > n1:		
		screenrow = crt.Screen.CurrentRow - d_Abis_IP
		result = crt.Screen.Get(screenrow, 1, screenrow, 15)
		d_Abis_IP += 1
		i_Abis_IP -= 1
		impacted_Abis.append(result)
	for ip_Abis in impacted_Abis:
		crt.Screen.Send('ping ' + ip_Abis + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)

	# ping to BSC IP
	crt.Screen.Send('\r')
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
	
	# ping to Sites	
	if crt.Screen.ReadString('Host'):
		n3 = crt.Screen.CurrentRow
		result1 = crt.Screen.Get(n3, 1, n3, 15)
		pass
	if crt.Screen.ReadString('[IuB_UP]'):
		n4 = crt.Screen.CurrentRow
		result2 = crt.Screen.Get(n4, 1, n4, 15)	
		pass
	i2_IuB_UP = n4
	d_IuB_UP = 1
	impacted_IuB_UP = []
	while i2_IuB_UP > n3:		
		screenrow = crt.Screen.CurrentRow - d_IuB_UP
		result = crt.Screen.Get(screenrow, 1, screenrow, 15)
		d_IuB_UP += 1
		i2_IuB_UP -= 1
		impacted_IuB_UP.append(result)
	for ip_IuB in impacted_IuB_UP:
		crt.Screen.Send('ping ' + ip_IuB + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)

	# ping RNC IP
	crt.Screen.Send('\r')
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

	# ping to Sites
	if crt.Screen.ReadString('Host'):
		n5 = crt.Screen.CurrentRow
		result1 = crt.Screen.Get(n5, 1, n5, 15)
		pass

	if crt.Screen.ReadString('[LTE-S1X2]'):
		n6 = crt.Screen.CurrentRow
		result2 = crt.Screen.Get(n6, 1, n6, 15)	
		pass

	i_LTES1X2 = n6
	d_LTES1X2 = 1
	impacted_LTES1X2 = []
	while i_LTES1X2 > n5:		
		screenrow = crt.Screen.CurrentRow - d_LTES1X2
		result = crt.Screen.Get(screenrow, 1, screenrow, 15)
		d_LTES1X2 += 1
		i_LTES1X2 -= 1
		impacted_LTES1X2.append(result)
		
	for ip_LTE in impacted_LTES1X2:
		crt.Screen.Send('ping ' + ip_LTE + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)

	# ping MME IP
	crt.Screen.Send('\r')
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

	# ping to Sites
	if crt.Screen.ReadString('Host'):
		n7 = crt.Screen.CurrentRow
		result1 = crt.Screen.Get(n7, 1, n7, 15)
		pass
	if crt.Screen.ReadString('[OM-HWI]'):
		n8 = crt.Screen.CurrentRow
		result2 = crt.Screen.Get(n8, 1, n8, 15)	
		pass
	i_OMHWI = n8
	d_OMHWI = 1
	impacted_OMHWI = []
	while i_OMHWI > n7:		
		screenrow = crt.Screen.CurrentRow - d_OMHWI
		result = crt.Screen.Get(screenrow, 1, screenrow, 15)
		d_OMHWI += 1
		i_OMHWI -= 1
		impacted_OMHWI.append(result)
	for ip_OM in impacted_OMHWI:
		crt.Screen.Send('ping ' + ip_OM + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)

	# ping OSS IP
	crt.Screen.Send('\r')
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
	# ping to Sites
	if crt.Screen.ReadString('Host'):
		n9 = crt.Screen.CurrentRow
		result1 = crt.Screen.Get(n9, 1, n9, 15)
		pass
	if crt.Screen.ReadString('[OM-Power]'):
		n10 = crt.Screen.CurrentRow
		result2 = crt.Screen.Get(n10, 1, n10, 15)	
		pass
	i_OMPower = n10
	d_OMPower = 1
	impacted_OMPower = []
	while i_OMPower > n9:		
		screenrow = crt.Screen.CurrentRow - d_OMPower
		result = crt.Screen.Get(screenrow, 1, screenrow, 15)
		d_OMPower += 1
		i_OMPower -= 1
		impacted_OMPower.append(result)	
	for ip_OMPower in impacted_OMPower:
		crt.Screen.Send('ping ' + ip_OMPower + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)

	# ping NMS POWER
	crt.Screen.Send('\r')
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
	# ping to Sites
	if crt.Screen.ReadString('Host'):
		n11 = crt.Screen.CurrentRow
		result1 = crt.Screen.Get(n11, 1, n11, 15)
		pass
	if crt.Screen.ReadString('[Inband-RTN]'):
		n12 = crt.Screen.CurrentRow
		result2 = crt.Screen.Get(n12, 1, n12, 15)	
		pass
	i_InbandRTN = n12
	d_InbandRTN = 1
	impacted_InbandRTN = []
	while i_InbandRTN > n11:		
		screenrow = crt.Screen.CurrentRow - d_InbandRTN
		result = crt.Screen.Get(screenrow, 1, screenrow, 15)
		d_InbandRTN += 1
		i_InbandRTN -= 1
		impacted_InbandRTN.append(result)	
	for ip_RTN in impacted_InbandRTN:
		crt.Screen.Send('ping ' + ip_RTN + '\r')
		if crt.Screen.ReadString('5 packets transmitted'):
			pass
		else:
			crt.Screen.WaitForString('round-trip min/avg/max/stddev')
			crt.Sleep(2)
	
	# ping U2000RTN
	crt.Screen.Send('\r')
	crt.Screen.Send('ping '+ RTN +'\r')
	if crt.Screen.ReadString('5 packets transmitted'):
		pass
	else:
		crt.Screen.WaitForString('round-trip min/avg/max/stddev')
		crt.Sleep(2)

	crt.Screen.Synchronous = False

main()