odoo.define('discount_pos.DiscountPOS', function (require) {
    'use strict';

    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');

    const DiscountPOS = (ProductScreen) => class DiscountPOS extends ProductScreen {

            async _displaydiscountPopup() {

                if(this.currentOrder.orderlines.length == 0){
                    return;
                }else{
                    const { confirmed, payload } = await this.showPopup('NumberPopup', {
                    title: this.env._t('Apply Discount'),
                    });
                    if (confirmed) {
                        if(this.env.pos.config.discount_type ==='percentage'){
                            this.currentOrder.get_selected_orderline().set_discount(payload);

                        }else if(this.env.pos.config.discount_type ==='amount'){
                            var selected_orderline = this.currentOrder.get_selected_orderline();
                            var new_price = selected_orderline.price-payload;
                            selected_orderline.set_unit_price(new_price);
                            selected_orderline.get_price_reduce(payload);


                        }
                    }
                }
           }
    }
    Registries.Component.extend(ProductScreen,DiscountPOS);
    return DiscountPOS;
});