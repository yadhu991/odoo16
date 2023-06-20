odoo.define('discount_pos.Discount_amountPOS', function (require) {
    'use strict';

    const {Orderline} = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');

    const Discount_amountPOS = (Orderline) => class Discount_amountPOS extends Orderline {

     get_price_reduce(deducted_amount){

        this.deduce = deducted_amount;

    }
    get_price_reduce_str(){
        return this.deduce;
    }


    }
    Registries.Model.extend(Orderline,Discount_amountPOS);
    return Discount_amountPOS;
});