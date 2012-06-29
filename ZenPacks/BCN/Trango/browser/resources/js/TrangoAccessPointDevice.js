/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at a TrangoAccessPointDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');


/*
 * Friendly names for the components. First parameter is the meta_type in your
 * custom component class. Second parameter is the singular form of the
 * friendly name to be displayed in the UI. Third parameter is the plural form.
 */
ZC.registerName('TrangoSubscriberUnit', _t('Trango Subscriber Unit'), _t('Trango Subscriber Units'));


/*
 * Custom component grid panel. This controls the grid that gets displayed for
 * components of the type set in "componentType".
 */
ZC.TrangoSubscriberUnitPanel = Ext.extend(ZC.ComponentGridPanel, {
/* new for zenoss 4 Ext.define('Zenoss.component.TrangoSubscriberUnitPanel', {
    extend: 'Zenoss.component.ComponentGridPanel', */
    subComponentGridPanel: false,

    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'suRemarks',
            componentType: 'TrangoSubscriberUnit',
	    /*alias:['widget.TrangoSubscriberUnitPanel'],*/
	    enableSort: true,
	    /* autoLoad: true, */
	    defaultSort: { field: 'suID', direction: 'ASC'},
	    sortInfo: {
                field: 'suID',
                direction: 'ASC'
            },
            fields: [
                {name: 'suID', type: 'int', sortType: 'asInt'},
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
		{name: 'status'},
                {name: 'snmpindex'},
		{name: 'distance'},
                {name: 'suRemarks'},
                {name: 'suIPAddr'},
                {name: 'suMAC'},
                {name: 'suUpLinkCIR'},
                {name: 'suDownLinkCIR'},
                {name: 'suUpLinkMIR'},
                {name: 'suDownLinkMIR'},
                {name: 'suDistance'},
                {name: 'suAssociation'}
            ],
	    /*sortInfo: {
		field: 'suID',
		direction: 'ASC'
	    },*/
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                /*sortable: true,*/
                width: 50
 /*           },{ 
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true,
                width: 50
 */           },{
                id: 'suID',
                dataIndex: 'suID',
                header: _t('SUID'),
                sortable: true,
                width: 50
            },{
                id: 'suRemarks',
                dataIndex: 'suRemarks',
                header: _t('Remarks'),
                /*sortable: true,*/
                width: 200
            },{
                id: 'suIPAddr',
                dataIndex: 'suIPAddr',
                header: _t('SU Management IP'),
                /*sortable: true,*/
                width: 120
            },{
                id: 'suMAC',
                dataIndex: 'suMAC',
                header: _t('SU Device ID'),
                /*sortable: true,*/
                width: 120
            },{
                id: 'suUpLinkCIR',
                dataIndex: 'suUpLinkCIR',
                header: _t('CIR up'),
                /*sortable: true,*/
                width: 50
            },{
                id: 'suDownLinkCIR',
                dataIndex: 'suDownLinkCIR',
                header: _t('CIR dn'),
                /*sortable: true,*/
                width: 50
            },{
                id: 'suUpLinkMIR',
                dataIndex: 'suUpLinkMIR',
                header: _t('MIR up'),
                /*sortable: true,*/
                width: 50
            },{
                id: 'suDownLinkMIR',
                dataIndex: 'suDownLinkMIR',
                header: _t('MIR dn'),
                /*sortable: true,*/
                width: 50
            },{
/*                id: 'suDistance',
                dataIndex: 'suDistance',
                header: _t('SU Distance'),
		renderer: function(suD) {
                             if (suD==1) {
                               return suD + " mile";
			     } else if (suD==0) {
                               return "< 1 mile";
                             } else if (suD==-1) {
                               return "Unavailable";
                             } else {
                               return suD + " miles";
                             }
                },
                sortable: true,
                width: 70
            },{ */
                id: 'distance',
                dataIndex: 'distance',
                header: _t('SU Distance'),
                /*sortable: true,*/
                width: 70
            },{
                id: 'status',
                dataIndex: 'status',
                header: _t('Status'),
                renderer: Zenoss.render.pingStatus,
                width: 60
	    },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                width: 60
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons
            }]
        });
        /* new for zenoss 4 this.callParent([config]); */
        ZC.TrangoSubscriberUnitPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('TrangoSubscriberUnitPanel', ZC.TrangoSubscriberUnitPanel);

})();
