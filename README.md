# Jellyfin Liquid Glass Theme

> **Note:** A luxury, Apple-inspired Liquid Glass CSS theme for Jellyfin media servers, featuring refractive frosted glass optics, an animated multi-color shifting mesh gradient, and minimalist floating controls.

## Credits

This theme is built upon the foundation of the **Abyss Jellyfin Theme** by **AumGupta**. Full credit goes to them for the original groundwork and architecture.  
Source: https://github.com/AumGupta/abyss-jellyfin

---

## Comprehensive Explanation of Features & Design

If you add this CSS to your Jellyfin server, here is a breakdown of the design language and visual transformations:

### 1. Animated Multi-Color Shifting Mesh Gradient
- **Fluid Luminous Backdrop:** Features an 8-color glowing mesh gradient (emerald, coral pink, cyan, amber, violet, royal blue, sunset orange, and indigo) flowing across a deep `#040612` midnight base.
- **20s Keyframe Morphing (`liquidMultiColorFlow`):** Generates subtle fluid movement behind all frosted glass panels, giving the UI depth and life.
- **Hardware-Accelerated & Accessible:** Automatically turns off on devices with `prefers-reduced-motion` enabled to conserve battery and eliminate visual distractions.

### 2. Apple Tahoe Liquid Glass Optics
- **High Refraction & Saturation:** Deep frosted glass panels utilizing `backdrop-filter: blur(48px) saturate(280%) brightness(125%)` to refract background lighting dynamically.
- **Dual-Axis Specular Sheens:** 135° and 180° lighting highlights along top borders with subpixel razor bevels and fading lower edges.
- **Applied Universally:** Restyles the main navigation header, sidebar drawer, dialogs, user profiles, action sheets, and modal menus into cohesive floating glass surfaces.

### 3. Video Player OSD — Floating Glass Pills
- **Pill-Shaped Controls:** Both top (navigation and title) and bottom (playback slider and controls) bars are detached and styled as floating rounded capsule pills.
- **Glass Play Orb:** The central play/pause button is an Apple-standard circular glass orb (`border-radius: 50%`) with dedicated specular highlights.
- **Zero Double-Glass Layering:** The parent player overlay is transparent to eliminate muddy, stacked blur artifacts.
- **Cinema-Grade Subtitles:** Proportional caption scaling with Apple SF Pro typography, high-contrast outlines, and responsive bounds to prevent oversized wrapping.

### 4. Minimalist 3-Button Media Detail Pages
- **Clutter Elimination:** Hides cluttered secondary buttons on movie and episode detail pages, prioritizing a clean, distraction-free 3-button layout:
  1. ▶ **Play / Resume**
  2. ↓ **Download** (visible if user has download rights)
  3. ⋮ **More Options (Three-Dot)**
- **Apple Capsule Action Buttons:** Medium 42px height with full pill radius, dual-layer bevel rims, and tactile press micro-interactions.

### 5. macOS Thin Overlay Scrollbar
- **Discreet & Functional:** Replaces bulky 14px scrollbars with a sleek, 6px semi-transparent rounded scrollbar that seamlessly fades when not in active use.

### 6. Mobile & Client Optimizations
- **Performance Budget:** Lightened blur and reduced gradient overhead on mobile clients (`layout-mobile`) and native wrappers (`html.cordova`, `html.android`, `html.ios`) for 60fps scrolling.
- **Orientation Transitions:** Smooth 0.5s CSS transition for video controls when rotating between portrait and landscape modes.
- **Clean Poster Cards:** Clutter-free media cards with unobtrusive badges.

---

## How to Use

Add the following to your **Jellyfin Dashboard → General → Custom CSS**:

```css
@import url("https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@main/liquid-glass-bundle.css");
```

---

### Note on Caching (Force Updating)

CDNs and browsers cache CSS files. To bypass the cache and load updates immediately, append a version parameter to the end of the URL:

```css
@import url("https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@main/liquid-glass-bundle.css?v=2");
```
