odoo.define('dynamic_customers.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core = require('web.core');
   var qweb = core.qweb;
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_customers',
       willStart: async function() {
            var self = this;
            await rpc.query({
            route: '/total_product_sold',
            }).then((data) => {
                this.data = data;
           });
       },
       start: function() {
            var chunks = _.chunk(this.data, 4)
            chunks[0].is_active = true
            this.$el.find('#items').html(
            qweb.render('hotel.snippet_carousel',{
            chunks}))
       },
   });
   PublicWidget.registry.dynamic_snippet_customers = Dynamic;
   return Dynamic;
});

