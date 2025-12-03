============================
SM Custom Loading Animation
============================

.. |badge1| image:: https://img.shields.io/badge/maturity-Production-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production
.. |badge2| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge3| image:: https://img.shields.io/badge/Odoo-18.0-purple.png
    :alt: Odoo 18.0

|badge1| |badge2| |badge3|

Transform your Odoo user experience with 56 stunning pure CSS loading animations! No external dependencies, fully customizable, and designed to seamlessly integrate with your Odoo instance.

**Key Features:**

* **56 Beautiful Animations**: Pure CSS animations across 10 categories
* **Zero Dependencies**: No external JavaScript libraries required
* **Full Customization**: Custom colors, positions, and loading text
* **Mobile Responsive**: Hardware-accelerated smooth animations
* **Lightweight**: Minimal performance impact with pure CSS
* **Instant Apply**: Changes take effect immediately after save

**Animation Categories:**

* **Spinners** (5 types) - Half Circle, Dual Color, Segmented, Masked, Triple Ring
* **Progress** (5 types) - Simple Bar, Striped, Stepped, Circular, Column Bars
* **Wobbling** (3 types) - Pendulum, Sliding Dot, Radial Slide
* **Wavy** (5 types) - Continuous, Growing, Center, Dual, Blurred Wave
* **Filling** (5 types) - Linear, Segment, Diagonal, Center, Letter by Letter
* **Continuous** (2 types) - Radial Circles, Light Beam
* **Circles** (6 types) - Two Circles, Three Circles, Box Shadow, Square/Triangle Path, Wave Pattern
* **Nature** (5 types) - Star Pulse, Sun Glow, Moon Phase, Rainbow, Leaves
* **Time** (4 types) - Clock Hands, Hourglass, Clock Fill, Bell
* **Factory** (6 types) - Conveyor Belt, Assembly Line, Dual Belt, Mixed Belt, Bottle Filling, Elevator

**Table of contents**

.. contents::
   :local:

Installation
============

To install this module, simply:

1. Download or clone this module to your Odoo addons directory
2. Update the apps list in Odoo
3. Install "SM Custom Loading Animation" from the Apps menu
4. Navigate to Settings → Loading Animation to configure

Dependencies: web, base_setup (core Odoo modules)

Configuration
=============

Navigate to **Settings → Loading Animation** to configure:

**Available Options:**

* **Animation Type**: Choose from 56 animation styles
* **Position**: Bottom Right, Bottom Left, Top Right, Top Left, Center Screen
* **Primary Color**: Main animation color (hex format, e.g., #714B67)
* **Background Color**: Background of loading indicator (hex format)
* **Show Loading Text**: Toggle loading text visibility
* **Loading Text**: Custom loading message (default: "Loading...")

**Quick Setup:**

1. Go to Settings → General Settings
2. Scroll to "Loading Animation" section
3. Select your preferred animation type
4. Choose position on screen
5. (Optional) Customize colors to match your brand
6. (Optional) Set custom loading text
7. Click Save

Changes take effect immediately - no restart required!

Usage
=====

Once installed and configured, the custom loading animation will **automatically replace** Odoo's default loading indicator.

**The animation appears during:**

* Page navigation
* AJAX requests
* Form submissions
* Report generation
* Data exports
* Any background processing

**No additional code or configuration required!**

**Example Configuration:**

::

    Animation Type: Spinner 1 - Half Circle
    Position: Bottom Right
    Primary Color: #714B67 (Odoo Purple)
    Background Color: #FFFFFF
    Show Loading Text: Yes
    Loading Text: "Loading..."

**Customization Tips:**

* Use your company brand colors for primary color
* Try "Center Screen" for important operations
* Disable loading text for cleaner look
* Test different animations to find your favorite style

Performance
===========

This module is optimized for performance:

* **Pure CSS**: All animations use CSS3, no JavaScript animation overhead
* **Hardware Accelerated**: GPU-accelerated transforms for smooth animations
* **Lightweight**: Minimal file size (~50KB total including all 56 animations)
* **Zero External Calls**: No CDN, no external libraries, works completely offline
* **Fast Loading**: No HTTP requests for animation libraries

Browser Compatibility
=====================

* Chrome 80+
* Firefox 75+
* Safari 13+
* Edge 80+
* Opera 67+

All modern browsers with CSS3 animation support.

Troubleshooting
===============

**Animation not showing?**

1. Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
2. Restart Odoo server
3. Check if module is properly installed in Apps menu
4. Verify settings in Settings → Loading Animation

**Colors not updating?**

1. Clear browser cache
2. Verify hex color format (must start with # and have 6 characters)
3. Re-save settings
4. Refresh browser

**Animation position wrong?**

1. Some custom themes may override positioning
2. Try "Center Screen" position as fallback
3. Check for CSS conflicts in browser developer tools

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/stevenmarp/sm_loading_animation/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smash it by providing detailed and welcomed feedback.

Credits
=======

Authors
~~~~~~~

* Stevenmarp

Contributors
~~~~~~~~~~~~

* stevenmarp <stevenoctavianusmarpung@gmail.com>

Maintainers
~~~~~~~~~~~

This module is maintained by Stevenmarp

Stevenmarp is a professional Odoo implementation partner specializing in:

* Custom module development
* Odoo implementation and customization
* Technical support and training
* System integration

For support or custom development requests:

* Email: stevenoctavianusmarpung@gmail.com

This module is part of our commitment to the Odoo community and open-source software.
