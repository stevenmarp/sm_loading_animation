# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    snk_loading_animation_type = fields.Selection([
        ('default', 'Default Odoo'),
        # Spinner Animations
        ('spinner_1', 'Spinner 1 - Half Circle'),
        ('spinner_2', 'Spinner 2 - Dual Color'),
        ('spinner_3', 'Spinner 3 - Segmented'),
        ('spinner_4', 'Spinner 4 - Masked'),
        ('spinner_5', 'Spinner 5 - Triple Ring'),
        # Progress Animations
        ('progress_1', 'Progress 1 - Simple Bar'),
        ('progress_2', 'Progress 2 - Striped'),
        ('progress_3', 'Progress 3 - Stepped'),
        ('progress_4', 'Progress 4 - Circular'),
        ('progress_5', 'Progress 5 - Column Bars'),
        # Wobbling Animations
        ('wobbling_1', 'Wobbling 1 - Pendulum'),
        ('wobbling_2', 'Wobbling 2 - Sliding Dot'),
        ('wobbling_3', 'Wobbling 3 - Radial Slide'),
        # Wavy Animations
        ('wavy_1', 'Wavy 1 - Continuous Wave'),
        ('wavy_2', 'Wavy 2 - Growing Wave'),
        ('wavy_3', 'Wavy 3 - Center Wave'),
        ('wavy_4', 'Wavy 4 - Dual Wave'),
        ('wavy_5', 'Wavy 5 - Blurred Wave'),
        # Filling Animations
        ('filling_1', 'Filling 1 - Linear Fill'),
        ('filling_2', 'Filling 2 - Segment Fill'),
        ('filling_3', 'Filling 3 - Diagonal Fill'),
        ('filling_4', 'Filling 4 - Center Fill'),
        ('filling_5', 'Filling 5 - Letter by Letter'),
        # Continuous Animations
        ('continuous_1', 'Continuous 1 - Radial Circles'),
        ('continuous_2', 'Continuous 2 - Light Beam'),
        # Circle Animations
        ('circle_1', 'Circle 1 - Two Circles'),
        ('circle_2', 'Circle 2 - Three Circles'),
        ('circle_3', 'Circle 3 - Box Shadow'),
        ('circle_4', 'Circle 4 - Square Path'),
        ('circle_5', 'Circle 5 - Triangle Path'),
        ('circle_6', 'Circle 6 - Wave Pattern'),
        # Nature Animations
        ('nature_1', 'Nature 1 - Star Pulse'),
        ('nature_2', 'Nature 2 - Sun Glow'),
        ('nature_3', 'Nature 3 - Moon Phase'),
        ('nature_4', 'Nature 4 - Rainbow'),
        ('nature_5', 'Nature 5 - Leaves'),
        # Time Animations
        ('time_1', 'Time 1 - Clock Hands'),
        ('time_2', 'Time 2 - Hourglass'),
        ('time_3', 'Time 3 - Clock Fill'),
        ('time_4', 'Time 4 - Bell'),
        # Factory Animations
        ('factory_1', 'Factory 1 - Conveyor Belt'),
        ('factory_2', 'Factory 2 - Assembly Line'),
        ('factory_3', 'Factory 3 - Dual Belt'),
        ('factory_4', 'Factory 4 - Mixed Belt'),
        ('factory_5', 'Factory 5 - Bottle Filling'),
        ('factory_6', 'Factory 6 - Elevator'),
    ], string='Loading Animation Type', default='spinner_1',
        config_parameter='snk_loading_animation.animation_type')

    snk_loading_position = fields.Selection([
        ('bottom-right', 'Bottom Right'),
        ('bottom-left', 'Bottom Left'),
        ('top-right', 'Top Right'),
        ('top-left', 'Top Left'),
        ('center', 'Center Screen'),
    ], string='Loading Position', default='bottom-right',
        config_parameter='snk_loading_animation.position')

    snk_loading_color = fields.Char(
        string='Loading Color',
        default='#714B67',
        config_parameter='snk_loading_animation.color',
        help='Primary color for loading animation (hex format)'
    )

    snk_loading_bg_color = fields.Char(
        string='Background Color',
        default='#FFFFFF',
        config_parameter='snk_loading_animation.bg_color',
        help='Background color for loading indicator'
    )

    snk_loading_show_text = fields.Boolean(
        string='Show Loading Text',
        default=True,
    )

    snk_loading_text = fields.Char(
        string='Loading Text',
        default='Loading...',
        config_parameter='snk_loading_animation.text'
    )

    @api.model
    def get_values(self):
        res = super().get_values()
        ICP = self.env['ir.config_parameter'].sudo()
        show_text = ICP.get_param('snk_loading_animation.show_text', 'True')
        res['snk_loading_show_text'] = show_text.lower() == 'true'
        return res

    def set_values(self):
        super().set_values()
        ICP = self.env['ir.config_parameter'].sudo()
        ICP.set_param('snk_loading_animation.show_text', str(self.snk_loading_show_text))
