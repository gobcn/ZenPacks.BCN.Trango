######################################################################
#
# TrangoSubscriberUnit modeler plugin
#
######################################################################

__doc__="""TrangoSubscriberUnit

TrangoSubscriberUnit maps subscriber units on a Trango M-900S AP

$Id: $"""

__version__ = '$Revision: $'[11:-2]

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class TrangoSubscriberUnit(SnmpPlugin):

    relname = "trangoSubscriberUnit"
    modname = "ZenPacks.BCN.Trango.TrangoSubscriberUnit"
    deviceProperties = SnmpPlugin.deviceProperties + ('getSUVolatileData',)
    
# snmpGetTableMaps gets tabular data

    snmpGetTableMaps = (


        GetTableMap('suInfoTable', '1.3.6.1.4.1.5454.1.30.3.6.1', {
            '.1': 'suID',
            '.2': 'suMAC',
	    '.3': 'suPolling',
	    '.4': 'suGroupID',
	    '.5': 'suIPAddr',
	    '.6': 'suSubnetMask',
	    '.7': 'suGateWay',
	    '.8': 'suRemarks',
	    '.9': 'suHWVer',
	    '.10': 'suFWVer',
            '.11': 'suFWChecksum',
            '.12': 'suFPGAVer',
            '.13': 'suFPGAChecksum',
            '.14': 'suAssociation',
            '.15': 'suDistance',
            '.34': 'suDownLinkCIR',
            '.35': 'suUpLinkCIR',
            '.36': 'suDownLinkMIR',
            '.37': 'suUpLinkMIR',
            }),

    )
	   
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)

        log.info("All results = %s", str(results))
        log.info("Volatile data = %s", getattr(device,'getSUVolatileData', None))
        getdata, tabledata = results
        
        log.debug( "Get Data= %s", getdata )
        log.debug( "Table Data= %s", tabledata )

        suInfoTable = tabledata.get("suInfoTable")

# If no data returned then simply return
        if ( not suInfoTable ): 
                log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
                return

        ifIndex = 1

        rm = self.relMap()
        
        for data in suInfoTable.values():

            try:
                om = self.objectMap(data)
                om.id = self.prepId("suid%s" % str(om.suID))
                om.snmpindex = int(om.suID)
                if hasattr(om, 'suMAC'):
                   if isinstance(om.suMAC, basestring):
                      om.suMAC = self.asmac(om.suMAC)
                   else:
                        log.debug("The MAC address for interface %s is invalid (%s)" \
                         " -- ignoring", om.id, om.suMAC)
		if om.suAssociation != 1:
		   om.suRemarks = "Remarks Unavailable (SU was offline during remodel)"
		   om.suIPAddr = "Unavailable"
                   om.suDistance = -1
            except AttributeError, errorInfo:
                log.warn( " Attribute error in TrangoSubscriberUnit modeler plugin %s", errorInfo)
                continue
	    #log.warn ("Appending data: %s", str(om))
            rm.append(om) 
        return rm
