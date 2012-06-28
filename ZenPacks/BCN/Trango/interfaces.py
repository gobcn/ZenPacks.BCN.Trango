from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces.template import IRRDDataSourceInfo

# ZuulMessageFactory is the translation layer. You will see strings intended to
# been seen in the web interface wrapped in _t(). This is so that these strings
# can be automatically translated to other languages.
from Products.Zuul.utils import ZuulMessageFactory as _t

# In Zenoss 3 we mistakenly mapped TextLine to Zope's multi-line text
# equivalent and Text to Zope's single-line text equivalent. This was
# backwards so we flipped their meanings in Zenoss 4. The following block of
# code allows the ZenPack to work properly in Zenoss 3 and 4.

# Until backwards compatibility with Zenoss 3 is no longer desired for your
# ZenPack it is recommended that you use "SingleLineText" and "MultiLineText"
# instead of schema.TextLine or schema.Text.
from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version
if Version.parse('Zenoss %s' % ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class ITrangoSubscriberUnitInfo(IComponentInfo):
    
    suID = schema.Int(title=_t(u"SUID"))
    suMAC = SingleLineText(title=_t(u"SU Device ID"))
    polling = SingleLineText(title=_t(u"SU Polling Type"))
    groupid = SingleLineText(title=_t(u"Group ID"))
    suIPAddr = SingleLineText(title=_t(u"SU Management IP"))
    suSubnetMask = SingleLineText(title=_t(u"SU Subnet Mask"))
    suGateWay = SingleLineText(title=_t(u"SU Default Gateway"))
    suRemarks = SingleLineText(title=_t(u"Remarks"))
    suHWVer = SingleLineText(title=_t(u"SU Hardware Version"))
    suFWVer = SingleLineText(title=_t(u"SU Firmware Version"))
    suFWChecksum = SingleLineText(title=_t(u"SU Firmware Checksum"))
    suFPGAVer = SingleLineText(title=_t(u"SU FPGA Version"))
    suFPGAChecksum = SingleLineText(title=_t(u"SU FPGA Checksum"))
    distance = SingleLineText(title=_t(u"SU Distance"))
    suDownLinkCIR = schema.Int(title=_t(u"CIR dn (Kbps)"))
    suUpLinkCIR = schema.Int(title=_t(u"CIR up (Kbps)"))
    suDownLinkMIR = schema.Int(title=_t(u"MIR dn (Kbps)"))
    suUpLinkMIR = SingleLineText(title=_t(u"MIR up (Kbps)"))
