###########################################################################
#
# Trango Interface Map to Map Interfaces to AP-900 devices
# Extends and replaces default Zenoss InterfaceMap
#
###########################################################################

__doc__ = """TrangoInterfaceMap

Gather IP network interface information from SNMP, and create DMD interface objects

"""

import re

from Products.ZenUtils.Utils import cleanstring, unsigned
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.zenoss.snmp.InterfaceMap import InterfaceMap

class TrangoInterfaceMap(InterfaceMap):
    """
    Map IP network names and aliases to DMD 'interface' objects
    """

    # gets data for Ethernet and Radio interfaces
    columns = {
             '.1.3.6.1.4.1.5454.1.30.1.8' : 'ipAddress',
             '.1.3.6.1.4.1.5454.1.30.1.9' : 'netmask',
             '.1.3.6.1.4.1.5454.1.30.1.2' : 'macaddress',
             '.1.3.6.1.4.1.5454.1.30.1.5' : 'apsystemDefOpMode',
             '.1.3.6.1.4.1.5454.1.30.1.6' : 'apsystemCurOpMode',
             '.1.3.6.1.4.1.5454.1.30.1.14' : 'apsystemMIRThreshold'
             }
    snmpGetMap = GetMap(columns)

    def process(self, device, results, log):
        """
        From SNMP info gathered from the device, convert them
        to interface objects.
        """
        getdata, tabledata = results
        log.info('Modeler %s processing data for device %s', self.name(), device.id)
        log.debug( "%s tabledata = %s" % (device.id,tabledata) )
        log.debug( "%s getdata = %s" % (device.id,getdata) )

        rm = self.relMap()

        for key in getdata.keys():
            if getdata[key] is None:
               log.debug( "%s is None, deleting from results." % (key) )
               del getdata[key]

        if getdata:
           if not self.checkColumns(getdata, self.columns, log):
              return
           log.info( "Device uses non-standard OIDs for eth and rf interface details, creating interfaces based on the non-standard OIDs." )
           eth0 = self.objectMap()
           rf0 = self.objectMap()
           eth0.ifindex = 0
           eth0.id = self.prepId('Ethernet')
           eth0.description = 'Ethernet interface on AP'
           eth0.type='TrangoAccessPointEthernet'
           eth0.adminStatus = 1
           eth0.operStatus = 1
	   eth0.speed = 3145728
           eth0.mtu = 1500
           if 'macaddress' in getdata:
              eth0.macaddress = getdata['macaddress']
           if not ('setIpAddresses' in getdata):
               eth0.setIpAddresses = []
           if 'ipAddress' in getdata:
               ip = getdata['ipAddress']
               if 'netmask' in getdata:
                   ip = ip + "/" + str(self.maskToBits(getdata['netmask'].strip()))
               # Ignore IP addresses with a 0.0.0.0 netmask.
               if ip.endswith("/0"):
                   log.warn("Ignoring IP address with 0.0.0.0 netmask: %s", ip)
               else:
                   eth0.setIpAddresses.append(ip)
           rf0.ifindex = 0
           rf0.id = self.prepId('Radio')
           rf0.description = 'RF Interface on AP'
           rf0.type='TrangoAccessPointRadio'
	   rf0.speed=3145728
           rf0.mtu=1500
	   if 'apsystemDefOpMode' in getdata:
              if getdata['apsystemDefOpMode'] == 0:
                 rf0.adminStatus = 1
              else:
                 rf0.adminStatus = 2
           if 'apsystemCurOpMode' in getdata:
              rf0.operStatus = not getdata['apsystemCurOpMode']
           om = self.processInt(log, device, rf0)
	   om.type=rf0.type
           if om: rm.append(om)
           om = self.processInt(log, device, eth0)
	   om.type=eth0.type
           if om: rm.append(om)
        else:
           log.info( "Device appears to use standard OIDs for Ethernet and RF Interfaces, skipping because these will be / have been mapped by the main zenoss.snmp.InterfaceMap plugin." )

        return rm
