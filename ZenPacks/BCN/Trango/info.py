# This file is the conventional place for "Info" adapters. Info adapters are
# a crucial part of the Zenoss API and therefore the web interface for any
# custom classes delivered by your ZenPack. Examples of custom classes that
# will almost certainly need info adapters include datasources, custom device
# classes and custom device component classes.

# Mappings of interfaces (interfaces.py) to concrete classes and the factory
# (these info adapter classes) used to create info objects for them are managed
# in the configure.zcml file.

from zope.component import adapts
from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.infos.template import RRDDataSourceInfo

from ZenPacks.BCN.Trango.TrangoSubscriberUnit import TrangoSubscriberUnit
from ZenPacks.BCN.Trango.interfaces import ITrangoSubscriberUnitInfo


class TrangoSubscriberUnitInfo(ComponentInfo):
    implements(ITrangoSubscriberUnitInfo)
    adapts(TrangoSubscriberUnit)

    monitor = ProxyProperty("monitor")
    snmpindex = ProxyProperty("snmpindex")
    suID = ProxyProperty("suID")
    suMAC = ProxyProperty("suMAC")
    suIPAddr = ProxyProperty("suIPAddr")
    suRemarks = ProxyProperty("suRemarks")
    suDistance = ProxyProperty("suDistance")
    suDownLinkCIR = ProxyProperty("suDownLinkCIR")
    suUpLinkCIR = ProxyProperty("suUpLinkCIR")
    suDownLinkMIR = ProxyProperty("suDownLinkMIR")
    suUpLinkMIR = ProxyProperty("suUpLinkMIR")
    suAssociation = ProxyProperty("suAssociation")
