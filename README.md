# Apple Liquid Glass for Jellyfin

> **Personal Note:** This is a personal project created strictly for my personal use. The default Jellyfin UI felt a bit too basic, so I needed something more premium and refined. If anyone else wants to use it, you are more than welcome to, but I primarily created this for my own purposes. I really liked the design that I got inspired from. Full credit goes to AumGupta and the original Abyss Jellyfin Theme. I built this entirely upon their hard work, so please check out their repository.

A modular, high-performance, pure CSS theme inspired by macOS Tahoe, visionOS, and iOS 26. This theme completely overhauls the Jellyfin UI to provide a floating, translucent, and highly polished Apple aesthetic without requiring JavaScript injections or third-party fonts.

## Features
- **True Apple Glassmorphism:** Three layers of glass (thin, regular, thick) modeled precisely after Apple's design language with 36-48px blurs, high saturation, and edge lighting.
- **Floating UI:** Detached sidebars, floating capsule headers, and a floating player that hovers over media artwork.
- **Apple TV Cards:** Scalable media cards with hidden borders, large radii (24px), and soft hover shadows.
- **Accessible & Responsive:** Adapts to all screen sizes automatically and provides fallback solid backgrounds for browsers without `backdrop-filter` support.
- **OLED Dark Mode:** Optional pitch-black base background to save battery and increase contrast on OLED screens.

## Installation

1. Copy the `liquid-glass-bundle.css` file to a directory accessible by your Jellyfin server, or use the CDN link below.
2. In Jellyfin, navigate to **Dashboard -> General -> Custom CSS code**.
3. Paste the following import statement (Recommended):
   ```css
   @import url('https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@main/liquid-glass-bundle.css');
   ```

## Customization

You can easily modify the design tokens by overriding the variables located in `variables.css`.

- **To adjust the blur intensity:** Modify `--glass-blur-thin`, `--glass-blur-regular`, `--glass-blur-thick`.
- **To change the accent color:** This theme inherits from Abyss base tokens, so you can change `--abyss-accent`.
- **To enable OLED Dark Mode:** Add the `.theme-oled` class to the body tag, or append this line to your Jellyfin Custom CSS box:
  ```css
  html, body { --bg-color-base: #000000 !important; }
  ```

## Browser Support
- **Full Support:** Safari 15+, Chrome 76+, Edge 79+, Firefox 103+.
- **Graceful Degradation:** Browsers without `backdrop-filter` support will automatically fall back to translucent solid backgrounds for readability.
- **Accessibility:** Respects OS-level `prefers-reduced-motion` to instantly disable all animations.

## Known Limitations
- Pure CSS cannot sample underlying pixels dynamically to change text color based on the background. We rely on translucent dark gradients over bright posters to maintain text readability.
- Animations are limited to CSS transitions. Advanced spring physics are approximated using `cubic-bezier(.2, .8, .2, 1)`.

## Credits

This project is a derivative work based on the excellent Abyss Jellyfin Theme by AumGupta. The original project provided the foundation for this work. This repository restructures the theme into a modular architecture and redesigns the interface toward an Apple Liquid Glass aesthetic while preserving the spirit of the original project. Many thanks to the original author for making the project open source and enabling community improvements.

Original project:
https://github.com/AumGupta/abyss-jellyfin
