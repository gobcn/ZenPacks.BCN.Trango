######################################################################
#
# TrangoAccessPointDevice modeler plugin
#
######################################################################

__doc__="""TrangoAccessPointDevice

TrangoAccessPointDevice sets up hardware / software manufacturer
and sets other information.

$Id: $"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap, MultiArgs

class TrangoAccessPointDevice(SnmpPlugin):
    maptype = "TrangoAccessPointDevice"

    snmpGetMap = GetMap({
	'.1.3.6.1.4.1.5454.1.30.1.1.1' :  'apversionHW',
        '.1.3.6.1.4.1.5454.1.30.1.1.2' :  'apversionFW',
        '.1.3.6.1.4.1.5454.1.30.1.1.3' :  'apversionFWChecksum',
        '.1.3.6.1.4.1.5454.1.30.1.1.4' :  'apversionFPGA',
        '.1.3.6.1.4.1.5454.1.30.1.1.5' :  'apversionFPGAChecksum',
        '.1.3.6.1.4.1.5454.1.30.1.3.0' :  'BaseID',
        '.1.3.6.1.4.1.5454.1.30.2.1.0' :  'ActiveChannel',
	'.1.3.6.1.4.1.5454.1.30.2.2.0' :  'Antenna',
        '.1.3.6.1.4.1.5454.1.30.2.3.1.0' :  'Chan1Freq',
	'.1.3.6.1.4.1.5454.1.30.2.3.2.0' :  'Chan2Freq',
	'.1.3.6.1.4.1.5454.1.30.2.3.3.0' :  'Chan3Freq',
	'.1.3.6.1.4.1.5454.1.30.2.3.4.0' :  'Chan4Freq',
        })

	   
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results

        log.debug( "Get Data= %s", getdata )
        log.debug( "Table Data= %s", tabledata )
        try:
            om = self.objectMap(getdata)
            om.setOSProductKey = MultiArgs(om.apversionFW, "Trango Systems, Inc.")
            if om.Antenna == "v":
               om.Antenna = "Vertical"
            elif om.Antenna == "h":
               om.Antenna = "Horizontal"
            elif om.Antenna == "e":
               om.Antenna = "External"
            return om
        except:
            log.warn( " Error in getting data for TrangoAccessPointDevice modeler plugin" )

