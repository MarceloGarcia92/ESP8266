import network
routercon = network.WLAN(network.STA_IF)
if routercon.active() == False:
	routercon.active(True)

routercon.connect('MARCELO GC', '90210TVD')