# -*- coding: utf-8 -*-
from openerp import api, fields, tools, models, _
import logging


_logger = logging.getLogger(__name__)

class KnowledgeBase(models.Model):
    _name = 'knowledge.base'

    name = fields.Char(string="Name")
    date = fields.Date('Date Create', default=lambda self: fields.Datetime.now())
    text_body = fields.Text(string="Text")
    section_ids = fields.Many2one('section.section', string="Section Name")
    general_concept = fields.Text(string='General Concept')
    where_applicable = fields.Text(string='Where Applicable')
    information_url_ids = fields.Many2one('sources.information', string="External links")
    literature = fields.Text(string="Literature")
    code = fields.Char(string='Code')

class SourcesOfInformation(models.Model):
    _name = 'sources.information'

    name = fields.Char(string='URL')

class Section(models.Model):
    _name = 'section.section'

    name = fields.Char(string='Section Name')