/** @odoo-module */

    import { Orderline} from 'point_of_sale.models';
    import Registries from 'point_of_sale.Registries';
    const NewOrderline = (Orderline) => class NewOrderline extends Orderline {

            export_for_printing(){
                var line =  super.export_for_printing(arguments);
                line.owner_id = this.get_product().owner_id;
                return line;
            }
    }
    Registries.Model.extend(Orderline, NewOrderline);