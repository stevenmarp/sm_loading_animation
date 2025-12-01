# -*- coding: utf-8 -*-
{
    'name': 'SNK Custom Loading Animation',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': '56 Beautiful Pure CSS Loading Animations for Odoo 18 - Customizable Colors, Positions & Text',
    'description': """
SNK Custom Loading Animation
============================

Transform your Odoo user experience with 56 stunning pure CSS loading animations!

🎯 FEATURES
===========

✨ 56 Beautiful Animations (Pure CSS - No Dependencies!)
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

🎨 Full Customization
--------------------
• 5 Position Options: Bottom Right, Bottom Left, Top Right, Top Left, Center
• Custom Primary Color (hex)
• Custom Background Color (hex)
• Show/Hide Loading Text
• Custom Loading Message

⚡ Performance
-------------
• Pure CSS - No JavaScript animation overhead
• Zero external dependencies
• Lightweight and fast
• Hardware-accelerated smooth animations
• Mobile responsive

📦 Easy Installation
-------------------
1. Install module from Odoo Apps
2. Go to Settings → Loading Animation
3. Choose your preferred animation style
4. Save and enjoy!

🔧 Technical
-----------
• Odoo 18.0 (Community & Enterprise)
• License: LGPL-3
• Dependencies: web (core module only)
• Browser Support: Chrome, Firefox, Safari, Edge, Opera

💼 Perfect For
-------------
• Branding your Odoo instance
• Better user experience
• Professional appearance
• Custom client implementations

📞 Support
---------
• Email: support@sinerka.id
• Website: https://www.sinerka.id
    """,
    'author': 'Sinerka Network',
    'website': 'https://www.sinerka.id',
    'support': 'support@sinerka.id',
    'license': 'LGPL-3',
    'depends': ['web', 'base_setup'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'snk_loading_animation/static/src/scss/loading_animation.scss',
            'snk_loading_animation/static/src/webclient/loading_indicator.xml',
            'snk_loading_animation/static/src/webclient/loading_indicator.js',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 0.00,
    'currency': 'EUR',
}
