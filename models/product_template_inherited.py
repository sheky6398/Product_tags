from odoo import models,fields
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"


    tag_ids = fields.Many2many('product.tags',string='Tags')

    



