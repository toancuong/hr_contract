'''
Created on Sep 20, 2016

@author: phcuong
'''

from openerp import models, fields

class hr_phucap_baohiem(models.Model):
    """
    Dinh nghia them phu cap va bao hiem trong hop dong.
    """
    _name = 'hr.phucapbaohiem'
    _description = 'Thong tin phu cap va bao hiem cua nhan vien'
    
    code = fields.Char('Ma so', required=True)
    name = fields.Char('Ten Phu Cap va Bao Hiem', required=True)
    amount = fields.Float('So Tien', required=True)
    
    _sql_constraints = [
        ('code_uniq', 'unique (code)', "Tag code already exists !"),
    ]
    