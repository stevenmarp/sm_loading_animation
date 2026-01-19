# Screenshots Required for Odoo Apps

To complete the module publishing, you need to add the following screenshot images to this directory:

## Required Images:

### 1. banner.png
- **Size**: 1200 x 600 pixels
- **Format**: PNG
- **Content**: Main banner showing the module name "SM Custom Loading Animation" with attractive background
- **Purpose**: Main banner image shown in Odoo Apps store
- ✅ **Status**: Already exists

### 2. icon.png  
- **Size**: 256 x 256 pixels
- **Format**: PNG
- **Content**: Module icon/logo (can use loading animation icon)
- **Purpose**: Module icon in Apps list
- ✅ **Status**: Already exists

### 3. screenshot_1.png
- **Size**: 1200 x 900 pixels (or similar aspect ratio)
- **Format**: PNG
- **Content**: Screenshot of the configuration interface in Settings → Loading Animation
- **Should show**: 
  - Settings menu
  - Animation type dropdown (showing some of the 56 options)
  - Position options
  - Color pickers
  - Loading text options
- **Purpose**: Show users how easy it is to configure

### 4. screenshot_2.png
- **Size**: 1200 x 900 pixels
- **Format**: PNG
- **Content**: Showcase of different animation types
- **Should show**:
  - Grid/collage of 6-12 different animation types
  - Labels for each animation category (Spinners, Progress, Wavy, etc.)
  - Visual variety to show the 56 options available
- **Purpose**: Show the variety of animations available

### 5. screenshot_3.png
- **Size**: 1200 x 900 pixels
- **Format**: PNG
- **Content**: Customization examples
- **Should show**:
  - Same animation in different colors
  - Same animation in different positions
  - Before/after comparison
- **Purpose**: Demonstrate customization capabilities

### 6. screenshot_4.png
- **Size**: 1200 x 900 pixels
- **Format**: PNG
- **Content**: Loading animation in action on Odoo interface
- **Should show**:
  - Actual Odoo screen (e.g., Sales, Inventory, etc.)
  - Loading animation overlay active
  - Show how it looks in real usage
- **Purpose**: Show the module in actual use

## How to Create Screenshots:

1. **Install the module** in your Odoo 18.0 instance
2. **Configure different animations** to capture variety
3. Use **screenshot tools**:
   - Windows: Snipping Tool, Win + Shift + S
   - Mac: Cmd + Shift + 4
   - Linux: gnome-screenshot, flameshot, or Shutter
4. **Edit/crop** to the recommended sizes using:
   - GIMP (free, cross-platform)
   - Photoshop
   - Online tools: Canva, Photopea
5. **Optimize PNG files** to reduce size:
   - Use TinyPNG (https://tinypng.com/)
   - Or optipng/pngcrush command-line tools

## Quick Screenshot Commands:

### Capture Settings Page:
1. Navigate to Settings → General Settings
2. Scroll to "Loading Animation" section
3. Take full screenshot showing all options

### Capture Animation in Action:
1. Open any Odoo page (Sales Orders, Customers, etc.)
2. Trigger loading (refresh page, submit form)
3. Quickly take screenshot while animation is showing

### Create Animation Showcase:
1. Take multiple screenshots of different animations
2. Use image editor to create a grid/collage
3. Add labels for each animation type

## Tips for Good Screenshots:

- ✓ Use clean test data (no real customer information)
- ✓ Use default Odoo theme for consistency
- ✓ Ensure high resolution and clarity
- ✓ Show the full interface context
- ✓ Use professional-looking dummy data
- ✓ Avoid cluttered screens
- ✓ Highlight the module features clearly

## After Creating Screenshots:

1. Save all files in this directory (`static/description/`)
2. Ensure filenames match exactly: `screenshot_1.png`, `screenshot_2.png`, etc.
3. Verify file sizes (should be < 1MB each after optimization)
4. Test by viewing `index.html` in browser to ensure images display correctly
5. Commit and push to GitHub

---

**Current Status:**
- ✅ banner.png - EXISTS
- ✅ icon.png - EXISTS  
- ❌ screenshot_1.png - NEEDS TO BE CREATED
- ❌ screenshot_2.png - NEEDS TO BE CREATED
- ❌ screenshot_3.png - NEEDS TO BE CREATED
- ❌ screenshot_4.png - NEEDS TO BE CREATED

Once all screenshots are added, the module will be ready for Odoo Apps submission!
