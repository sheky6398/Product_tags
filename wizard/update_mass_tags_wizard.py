from odoo import models,fields,api
import logging

_logger = logging.getLogger(__name__)

class MassTags(models.TransientModel):
    _name = "update.mass.tags.wizard"
    _description = "User can update mass product tags."

    update_method = fields.Selection([('add','Add'),('replace','Replace')],default='add', string='Update Method')
    product_tag_ids = fields.Many2many('product.tags',string='Product_tags',required=True)


    def action_update_mass_tags(self):
        active_ids = self.env.context.get('active_ids')
        active_records = self.env['product.template'].browse(active_ids)
        _logger.info(f'\n Context={self.env.context}\n')
        update_method_add = self.update_method == 'add'
        update_method_replace = self.update_method == 'replace'

        for record in active_records:
            if update_method_add:
                result = record.update({
                    'tag_ids': [(6, 0, self.product_tag_ids.ids)]
                })
            elif update_method_replace:
                result = record.pop({
                    'tag_ids': [(6, 0, self.product_tag_ids.ids)]
                })
            _logger.info(f'\n Result:{result} \n')