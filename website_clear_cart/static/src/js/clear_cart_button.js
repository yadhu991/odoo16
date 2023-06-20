odoo.define('website_clear_cart.clear_cart', function (require) {
"use strict";
     var rpc = require('web.rpc');
     var publicWidget = require('web.public.widget');
     publicWidget.registry.websiteSaleClearCart = publicWidget.Widget.extend({
        selector: '#wrap',
        events: {
                'click #clear_button': '_clear_cart_onclick',
        },
        _clear_cart_onclick: function (ev) {
                 rpc.query({
                       route: '/shop/clear_cart',
                       params: {},
                 }).then(function (result) {
                        location.reload();
                 });
         },
     })

})