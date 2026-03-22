# -*- coding: utf-8 -*-
{
    'name': 'Loading Animation',
    'version': '19.0.1.0.0',
    'category': 'Tools',
    'summary': '56 Beautiful Pure CSS Loading Animations — Customizable Colors, Positions & Text',
    'description': """
Loading Animation
============================

Transform your Odoo user experience with 56 stunning pure CSS loading animations!

FEATURES
===========

56 Beautiful Animations (Pure CSS - No Dependencies!)
--------------------------------------------------------
• Spinners (5 types) - Half Circle, Dual Color, Segmented, Masked, Triple Ring
• Progress (5 types) - Simple Bar, Striped, Stepped, Circular, Column Bars
• Wobbling (3 types) - Pendulum, Sliding Dot, Radial Slide
• Wavy (5 types) - Continuous, Growing, Center, Dual, Blurred Wave
• Filling (5 types) - Linear, Segment, Diagonal, Center, Letter by Letter
• Continuous (2 types) - Radial Circles, Light Beam
• Circles (6 types) - Two Circles, Three Circles, Box Shadow, Square/Triangle Path, Wave Pattern
• Nature (5 types) - Star Pulse, Sun Glow, Moon Phase, Rainbow, Leaves
• Time (4 types) - Clock Hands, Hourglass, Clock Fill, Bell
• Factory (6 types) - Conveyor Belt, Assembly Line, Dual Belt, Mixed Belt, Bottle Filling, Elevator


    """,
    'author': 'Steven Marp',
    'license': 'LGPL-3',
    'depends': ['web', 'base_setup'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sm_loading_animation/static/src/scss/loading_animation.scss',
            'sm_loading_animation/static/src/webclient/loading_indicator.xml',
            'sm_loading_animation/static/src/webclient/loading_indicator.js',
        ],
    },
    'images': [
        'static/description/banner.gif',
        'static/description/icon.png',
        'static/description/screenshot_1.png',
        'static/description/screenshot_2.png',
        'static/description/screenshot_3.gif',
        'static/description/screenshot_4.gif',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 9.00,
    'currency': 'USD'
}
