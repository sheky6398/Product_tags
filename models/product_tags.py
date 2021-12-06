from odoo import models,fields
from random import randint
import logging

_logger = logging.getLogger(__name__)


class Tags(models.Model):
    _name = "product.tags"
    _description = "User can create product tags"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string='Name',required=True)
    sequence = fields.Integer(string="Sequence" ,required=True)
    color = fields.Integer('Color', default=_get_default_color)
    product_ids = fields.Many2many('product.template',string="Product")