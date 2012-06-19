===================
ZenPacks.BCN.Trango
===================

.. contents::
   :depth: 3

This project is a Zenoss_ extension (ZenPack) that allows for monitoring of
Trango M-900S Access Points and Subscriber Units.

Requirements & Dependencies
---------------------------
This ZenPack is known to be compatible with Zenoss version 3.2.1.

Installation
------------
You must first have, or install, Zenoss 3.2.1. Core and Enterprise
versions are supported. You can download the free Core version of Zenoss from
http://community.zenoss.org/community/download .

Normal Installation (packaged egg)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Depending on what version of Zenoss you're running you will need a different
package. Download the appropriate package for your Zenoss version from the list
below.

* Zenoss 3.2.1: `Latest Package for Python 2.6`_

Then copy it to your Zenoss server and run the following commands as the zenoss
user::

    zenpack --install <package.egg>
    zenoss restart

Developer Installation (link mode)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you wish to further develop and possibly contribute back you should clone
the git repository, then install the ZenPack in developer mode using the
following commands::

    git clone git://github.com/zenoss/ZenPacks.BCN.Trango.git
    zenpack --link --install ZenPacks.BCN.Trango
    zenoss restart

Usage
-----
Installing the ZenPack will add the following objects to your Zenoss system.

* Device Classes

  * /Devices/Network/Wireless/Trango/M900S-AP

* Monitoring Templates

  * TrangoAccessPointEthernet in /Network/Wireless/Trango/M900S-AP
  * TrangoAccessPointRadio in /Network/Wireless/Trango/M900S-AP
  * TrangoSubscriberUnit in /Network/Wireless/Trango/M900S-AP

* Event Classes (each with transforms)

  * /Perf/TrangoAccessPoint
  * /Perf/TrangoSubscriberUnit
  * /Status/TrangoSubscriberUnit
  * /Status/TrangoSubscriberUnit/instances/suLinkDown
  * /Status/TrangoSubscriberUnit/instances/suLinkUp

* MIBs

  * /mibs/TRANGOM900S-MIB
  * /mibs/TRANGOM900S-FIX-MIB

Access Point Monitoring
~~~~~~~~~~~~~~~~~~~~~~~
As the Trango Access Points lack support for IEEE interface tables, this script includes an interface modeler script that maps the primary Ethernet and Radio interfaces into the existing os.interfaces for the device in Zenoss.

The following graphs are included:

* Ethernet Interface - Throughput graph

  * Standard throughput graph with Inbound and Outbound from the perspective of
    the Ethernet interface

* Radio Interface - Packets Graph

  * Indicates Packets per second inbound/outbound/dropped from the perspective
    of the Radio interface on the AP

* Radio Interface - SU Count

  * GAUGE graph displays the current SU count on the AP as well as a threshold
    for high su count

* Radio Interface - Signal - RSSI

  * Signal graph includes Rx Threshold and Target RSSI

* Radio Interface - Signal - Transmit Power

  * Signal graph includes Power Max/Min/Current


Subscriber Unit Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~
The plugin adds a "Trango Subscriber Units" component type under Components for devices in the M900S-AP class. The following fields are provided:

  * Events - Shows active events for the SU
  * SUID - An integer containing the SUID number of the SU
  * Remarks - A string to describe the SU - set on the SU manually
  * SU Management IP - IP address for the SU's management interface
  * SU Device ID - MAC address for the SU
  * CIR up/down - Committed Information Rate Up/Down in kbit/sec
  * MIR up/down - Maximum Information Rate Up/Down in kbit/sec
  * Distance - Estimated distance in miles, calculated by AP
  * Status - Custom status field for Up/Down status of SU
  * Monitored - true/false to enable/disable monitoring
  * Locking - component locking settings

The following graphs are provided for the Subscriber Units:

* Throughput

  * Displays the current SU traffic. On the SU itself, due to the fact that the
    SU measures traffic from the POV of the Ethernet interface, the inbound
    counters represent the outbound traffic and the outbound counters represent 
    the inbound traffic; as a result, to make the graph more understandable,
    the graph itself has been inverted. Therefore, the Inbound graph correctly
    represents the AP-SU traffic and the Outbound graph correctly represents
    the SU-AP traffic.
  * Includes high utilization outbound and inbound thresholds based on MIR.

* Packets

  * Displays the current packets/sec Inbound and Outbound on the SU

* Errors

  * RF Dropped Packets, RF Retries at AP/SU, RF Retry maxed out at AP/SU

* Signal - RSSI

  * RSSI at AP (dBm), RSSI at SU (dBm)

* Signal - Transmit Power

  * Transmit Power at SU (dB)

Status monitoring for subscriber stations is also provided. Active polling is
carried out, in addition to SNMP traps. A custom "Status" field was used for the
status indicator rather than built-in status field due to the fact that the
built in field uses events to determine up/down status.

The event transforms handle the various up/down states as well as signal level. If an SU goes up or down, the transforms will change the status attribute in the
DMD for the SU and then commit the change. To prevent all of the "customer is
offline" events from filling up the event console and making the device yellow, 
the transforms are configured to drop any event where the suRemarks of the 
corresponding Subscriber Unit does not start with "vip-". In this way, you can 
receive events for VIP customers without events being created for non-VIP
customers. Up/Down status is handled before the event is dropped, for non-VIP
SU's, ensuring that the Status attribute is set correctly before the event is
deleted.

Some Trango M900S-AP units will use the wrong trap OID for some suLinkUp and 
suLinkDown traps. To correct for this, an extra fake MIB has been included to 
map these two trap OIDs to the existing suLinkup and suLinkDown transforms.

Known Issues
------------
If an Access Point is remodeled while a subscriber is offline, their Remarks
and IP address will disappear. This is due to the fact that the AP no longer
provides these values. The possibility is being investigated to pull the
existing values for Remarks and IP address into the modeler script such that,
if the subscriber unit is offline, the old Remarks and IP address stored in
Zenoss for the SU will be used instead of those pulled by the modeler script.
The distance also displays as "< 1 mile" for offline SU's.

Automatic sorting of the list of Subscriber Units by SUID number is not working.
Alphabetical sort is occuring, leading to wrong sorting. Clicking on the column
header for SUID after opening the list causes it to sort correctly and can be
used as a workaround until the cause of this issue is determined.

Screenshots
-----------
|Access Point Monitoring and Ethernet Graph|
|Access Point Radio Graphs|
|Subscriber Unit Monitoring|
|Subscriber Unit Graphs|


.. _Zenoss: http://www.zenoss.com/
.. _Latest Package for Python 2.6: https://github.com/downloads/zenoss/ZenPacks.BCN.Trango/ZenPacks.BCN.Trango-1.5-py2.6.egg

.. |Access Point Monitoring and Ethernet Graph| image:: https://github.com/zenoss/ZenPacks.BCN.Trango/tree/master/docs/apmonitoring.png
.. |Access Point Radio Graphs| image:: https://github.com/zenoss/ZenPacks.BCN.Trango/tree/master/docs/aprfinterface.png
.. |Subscriber Unit Monitoring| image:: https://github.com/zenoss/ZenPacks.BCN.Trango/tree/master/docs/sumonitoring.png
.. |Subscriber Unit Graphs| image:: https://github.com/zenoss/ZenPacks.BCN.Trango/tree/master/docs/sugraphs.png
