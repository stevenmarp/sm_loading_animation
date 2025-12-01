# SNK Custom Loading Animation

**Beautiful, modern loading animations for Odoo 18.0**

Transform your Odoo user experience with 56 stunning pure CSS loading animations. No external dependencies, fully customizable, and designed to seamlessly integrate with your Odoo instance.

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-purple.svg)
![License](https://img.shields.io/badge/License-LGPL--3-blue.svg)
![CSS Only](https://img.shields.io/badge/CSS-Pure-orange.svg)

---

## 🎯 Features

### ✨ 56 Beautiful Animations

All animations are pure CSS - **no external libraries or dependencies required!**

**🔄 Spinner Animations (5 types)**
- Half Circle Spinner
- Dual Color Spinner
- Segmented Spinner
- Masked Spinner
- Triple Ring Spinner

**📊 Progress Animations (5 types)**
- Simple Progress Bar
- Striped Progress
- Stepped Progress
- Circular Progress
- Column Bars

**🎪 Wobbling Animations (3 types)**
- Pendulum Motion
- Sliding Dot
- Radial Slide

**🌊 Wavy Animations (5 types)**
- Continuous Wave
- Growing Wave
- Center Wave
- Dual Wave
- Blurred Wave

**📈 Filling Animations (5 types)**
- Linear Fill
- Segment Fill
- Diagonal Fill
- Center Fill
- Letter by Letter

**♾️ Continuous Animations (2 types)**
- Radial Circles
- Light Beam

**⭕ Circle Animations (6 types)**
- Two Circles
- Three Circles
- Box Shadow
- Square Path
- Triangle Path
- Wave Pattern

**🌿 Nature Animations (5 types)**
- Star Pulse
- Sun Glow
- Moon Phase
- Rainbow
- Leaves

**⏰ Time Animations (4 types)**
- Clock Hands
- Hourglass
- Clock Fill
- Bell

**🏭 Factory Animations (6 types)**
- Conveyor Belt
- Assembly Line
- Dual Belt
- Mixed Belt
- Bottle Filling
- Elevator

### 🎨 Full Customization

- **5 Position Options**: Bottom Right, Bottom Left, Top Right, Top Left, Center Screen
- **Custom Colors**: Set primary animation color and background color
- **Loading Text**: Show/hide and customize loading message
- **Instant Apply**: Changes take effect immediately after save

### ⚡ Performance

- **Pure CSS**: No JavaScript animation overhead
- **Lightweight**: Minimal file size, fast loading
- **Smooth**: Hardware-accelerated animations
- **Mobile Responsive**: Works great on all devices
- **No External Dependencies**: Everything runs locally

---

## 📦 Installation

### Method 1: Direct Installation

1. Download the module from Odoo Apps Store
2. Extract to your Odoo addons directory
3. Restart Odoo server
4. Go to Apps → Update Apps List
5. Search for "SNK Custom Loading Animation"
6. Click Install

### Method 2: Git Clone

```bash
cd /path/to/odoo/addons
git clone https://github.com/sinerka/snk_loading_animation.git
```

Then restart Odoo and install from Apps menu.

---

## ⚙️ Configuration

Navigate to: **Settings → Loading Animation**

![Settings Screenshot](static/description/settings_screenshot.png)

### Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| Animation Type | Choose from 56 animation styles | Spinner 1 - Half Circle |
| Position | Where to show the loading indicator | Bottom Right |
| Primary Color | Main animation color (hex) | #714B67 (Odoo Purple) |
| Background Color | Background of loading box | #FFFFFF |
| Show Loading Text | Toggle loading text visibility | Enabled |
| Loading Text | Custom loading message | "Loading..." |

---

## 🖼️ Animation Gallery

### Spinners
| Spinner 1 | Spinner 2 | Spinner 3 | Spinner 4 | Spinner 5 |
|:---------:|:---------:|:---------:|:---------:|:---------:|
| Half Circle | Dual Color | Segmented | Masked | Triple Ring |

### Progress
| Progress 1 | Progress 2 | Progress 3 | Progress 4 | Progress 5 |
|:----------:|:----------:|:----------:|:----------:|:----------:|
| Simple Bar | Striped | Stepped | Circular | Column Bars |

### And 46 more animations across different categories!

---

## 🚀 Usage

Once installed and configured, the custom loading animation will **automatically replace** Odoo's default loading indicator and appear during:

- ✅ Page navigation
- ✅ AJAX requests  
- ✅ Form submissions
- ✅ Report generation
- ✅ Data exports
- ✅ Any background processing

**No additional code required!**

---

## 🔧 Technical Details

### Files Structure

```
snk_loading_animation/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── res_config_settings.py
├── views/
│   └── res_config_settings_views.xml
├── static/
│   ├── description/
│   │   └── icon.png
│   └── src/
│       ├── scss/
│       │   └── loading_animation.scss
│       └── webclient/
│           ├── loading_indicator.js
│           └── loading_indicator.xml
└── README.md
```

### Dependencies

- **Odoo 18.0** (Community or Enterprise)
- **web** module (core Odoo module)

### Browser Support

- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+
- ✅ Opera 67+

---

## 🐛 Troubleshooting

### Animation not showing?

1. Clear browser cache (Ctrl+Shift+R)
2. Restart Odoo server
3. Check if module is properly installed

### Colors not updating?

1. Clear browser cache
2. Check hex color format (e.g., #714B67)
3. Re-save settings

### Animation position wrong?

1. Some themes may override positioning
2. Try "Center Screen" position as fallback

---

## 📝 Changelog

### Version 1.0.0 (2024-12-01)
- 🎉 Initial release
- ✨ 56 pure CSS animation types
- 🎨 Full color customization
- 📍 5 position options
- 💬 Custom loading text
- 📱 Mobile responsive design
- ⚡ Zero external dependencies

---

## 🤝 Support

For support, customization, or feature requests:

- 📧 **Email**: support@sinerka.id
- 🌐 **Website**: [https://www.sinerka.id](https://www.sinerka.id)
- 🐛 **Issues**: [GitHub Issues](https://github.com/sinerka/snk_loading_animation/issues)

---

## 📜 License

This module is licensed under **LGPL-3** (GNU Lesser General Public License v3.0)

You are free to:
- ✅ Use commercially
- ✅ Modify
- ✅ Distribute
- ✅ Use privately

---

## 👨‍💻 Author

**Sinerka Network**

- 🏢 Professional Odoo Implementation Partner
- 🛠️ Custom Module Development
- 📚 Training & Consulting
- 🔧 Technical Support

---

## ⭐ Rate Us!

If you find this module useful, please rate us on the Odoo Apps Store! Your feedback helps us improve.

---

<p align="center">
  Made with ❤️ by <strong>Sinerka Network</strong>
</p>

<p align="center">
  <a href="https://www.sinerka.id">www.sinerka.id</a>
</p>
