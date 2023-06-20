odoo.define('pos_due_limit.DueLimit', function (require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const DueLimit = (PaymentScreen) => class DueLimit extends PaymentScreen {

       async _finalizeValidation(){

            if (this.currentOrder.get_partner()!=null){
                    var selected_method = this.env.pos.config.pos_payment_method_id[0];
                    var sum = 0;
                    this.currentOrder.get_paymentlines().forEach(sumFunction);
                    function sumFunction(item) {

                    if(item.payment_method.id == selected_method){
                            sum += item.amount;
                      }
                    }
                    var limit = this.currentOrder.get_partner().pos_due_limit;
                    if(limit == 0){
                       console.log('No Limit');
                    }
                    else if (limit<sum) {
                        const { confirmed, payload } = await this.showPopup('ErrorPopup', {
                            title: this.env._t('Payment Cannot be Validated'),
                            body: this.env._t('Due limit has been exceeded For The Customer !!!'),
                        });
                        return;
                    }

             super._finalizeValidation();
            }
       }
    }
    Registries.Component.extend(PaymentScreen,DueLimit);
    return DueLimit;
});
