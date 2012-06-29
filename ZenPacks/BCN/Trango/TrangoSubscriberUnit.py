from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class TrangoSubscriberUnit(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "TrangoSubscriberUnit"

    # Attributes specific to this component
    suID=0
    suMAC = ''
    suPolling=0
    suGroupID=0
    suIPAddr=''
    suSubnetMask=''
    suGateWay=''
    suRemarks = ''
    suHWVer=''
    suFWVer = ''
    suFWChecksum = ''
    suFPGAVer = ''
    suFPGAChecksum = ''
    suAssociation = ''
    suDistance = 0
    suDownLinkCIR=0
    suUpLinkCIR=0
    suDownLinkMIR=0
    suUpLinkMIR=0

    _properties = ManagedEntity._properties + (
        {'id': 'suID', 'type': 'int', 'mode': ''},
        {'id': 'suMAC', 'type': 'string', 'mode': ''},
        {'id': 'suPolling', 'type': 'int', 'mode': ''},
        {'id': 'suGroupID', 'type': 'int', 'mode': ''},
        {'id': 'suIPAddr', 'type': 'string', 'mode': ''},
        {'id': 'suSubnetMask', 'type': 'string', 'mode': ''},
        {'id': 'suGateWay', 'type': 'string', 'mode': ''},
        {'id': 'suRemarks', 'type': 'string', 'mode': ''},
        {'id': 'suHWVer', 'type': 'string', 'mode': ''},
	{'id': 'suFWVer', 'type': 'string', 'mode': ''},
	{'id': 'suFWChecksum', 'type': 'string', 'mode': ''},
	{'id': 'suFPGAVer', 'type': 'string', 'mode': ''},
	{'id': 'suFPGAChecksum', 'type': 'string', 'mode': ''},
	{'id': 'suAssociation', 'type': 'string', 'mode': ''},
	{'id': 'suDistance', 'type': 'int', 'mode': ''},
	{'id': 'suDownLinkCIR', 'type': 'int', 'mode': ''},
	{'id': 'suUpLinkCIR', 'type': 'int', 'mode': ''},
	{'id': 'suDownLinkMIR', 'type': 'int', 'mode': ''},
	{'id': 'suUpLinkMIR', 'type': 'int', 'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('trangoAccessPointDevice', ToOne(ToManyCont,
            'ZenPacks.BCN.Trango.TrangoAccessPointDevice.TrangoAccessPointDevice',
            'trangoSubscriberUnit',
            ),
        ),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
        },),
    },)

    # Custom components must always implement the device method. The method
    # should return the device object that contains the component.
    def device(self):
        return self.trangoAccessPointDevice()

    def getStatus(self):
        return self.suAssociation

    def convertStatus(self, statusCode):
        if statusCode == 1:
           return "Up"
        else:
           return "Down"

    def getDistance(self):
        if self.suDistance == 1:
           return str(self.suDistance) + " mile"
        elif self.suDistance == 0:
           return str(self.suDistance) + "< 1 mile"
        elif self.suDistance == -1:
           return "Unavailable"
        else:
           return str(self.suDistance) + " miles"

    def getPolling(self):
        if self.suPolling == 1:
           return "Regular"
        else:
           return "Priority"

    def getGroupID(self):
        if self.suGroupID == 0:
           return "No Group"
        else:
           return str(self.suGroupID)

    def primarySortKey(self):
        """Sort by suID"""
        return self.suRemarks

    def getInstDescription(self):
        return self.suRemarks

    def manage_deleteComponent(self, REQUEST=None):
        """
        Delete trangoSubscriberUnit component
        """
        url = None
        if REQUEST is not None:
            url = self.device().trangoSubscriberUnit.absolute_url()
        self.getPrimaryParent()._delObject(self.id)

        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(url)


