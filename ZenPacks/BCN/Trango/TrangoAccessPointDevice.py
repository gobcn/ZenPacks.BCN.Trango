from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from copy import deepcopy
from AccessControl import Permissions

class TrangoAccessPointDevice(Device):
    """
    TrangoAccessPointDevice device subclass
    """

    meta_type = portal_type = 'TrangoAccessPointDevice'

    # Extra property for a Trango device of Base ID
    #   (BaseID is a standard property on a device)
    # also activechannel and channel table

    apversionHW = ''
    apversionFW = ''
    apversionFWChecksum = ''
    apversionFPGA = ''
    apversionFPGAChecksum = ''
    BaseID = ''
    ActiveChannel = 0
    Antenna = ''
    Chan1Freq = 0
    Chan2Freq = 0
    Chan3Freq = 0
    Chan4Freq = 0

    _properties = Device._properties + (
        {'id':'apversionHW', 'type':'string', 'mode':''},
        {'id':'apversionFW', 'type':'string', 'mode':''},
        {'id':'apversionFWChecksum', 'type':'string', 'mode':''},
        {'id':'apversionFPGA', 'type':'string', 'mode':''},
        {'id':'apversionFPGAChecksum', 'type':'string', 'mode':''},
        {'id':'BaseID', 'type':'string', 'mode':''},
        {'id':'ActiveChannel', 'type':'int', 'mode':''},
        {'id':'Antenna', 'type':'string', 'mode':''},
        {'id':'Chan1Freq', 'type':'int', 'mode':''},
	{'id':'Chan2Freq', 'type':'int', 'mode':''},
	{'id':'Chan3Freq', 'type':'int', 'mode':''},
	{'id':'Chan4Freq', 'type':'int', 'mode':''},
        )

    # This is where we extend the standard relationships of a device to add
    # our "trangoSubscriberUnit" relationship that must be filled with components
    # of our custom "TrangoSubscriberUnit" class.
    # NOTE: class starts upper case; relationship starts lower case

    _relations = Device._relations + (
        ('trangoSubscriberUnit', ToManyCont(ToOne,
            'ZenPacks.BCN.Trango.TrangoSubscriberUnit.TrangoSubscriberUnit',
            'trangoAccessPointDevice',
            ),
        ),
    )

    factory_type_information = deepcopy(Device.factory_type_information)
    factory_type_information[0]['actions'] += (
            { 'id' : 'trangoAccessPointDevice'
            , 'name' : 'Access Point Details'
            , 'action' : 'TrangoAccessPointDetails'
            , 'permissions' : ( Permissions.view,) },
            )

    def getSUVolatileData(self):
        """Return the volatile data on existing SUs for modeler use
        """
        myvolatiledata = {}
        for su in self.trangoSubscriberUnit():
           suinfo = { 'suRemarks' : su.suRemarks, 'suIPAddr' : su.suIPAddr, 'suDistance' : su.suDistance }
	   myvolatiledata[su.suID] = suinfo
        return myvolatiledata

