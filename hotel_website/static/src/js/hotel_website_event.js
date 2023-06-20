odoo.define('hotel_website.example', function (require) {
"use strict";
    var Dialog = require('web.Dialog');
    var core = require('web.core');
    var _t = core._t;
    var rpc = require('web.rpc');

    const publicWidget = require('web.public.widget')
    publicWidget.registry.websiteEvents = publicWidget.Widget.extend({
         selector:'.hotel_booking',
         events: {
            'change #browser': '_alert_onclick',
            'change #appointment_date': '_alert_date'
        },
        _alert_onclick: function (ev) {
           var self = this;
           self.$el.find('#phone').val("");
           self.$el.find('#email').val("");
           var partner = $('#browser').val()

           rpc.query({
               route: '/partner_details',
               params: {'id': partner },
           }).then(function (result) {
                self.$el.find('#browser').val(result['name']);
                self.$el.find('#cust_id').val(result['id']);
                if (result['phone']!= false){
                self.$el.find('#phone').val(result['phone']);}

                if (result['email']!= false) {
                self.$el.find('#email').val(result['email']);
                }

           });
        },
        _alert_date: function (ev) {
            let currentDate = new Date().toJSON().slice(0, 10);
            var date = this.$el.find('#appointment_date').val();
            if (date < currentDate) {
                Dialog.alert(self, _t("Date must be an upcoming date!"), {
                title: _t('Invalid date'),
                });
                this.$el.find('#appointment_date').val("");
            }

        },
    })
});