# Jellyfin Liquid Glass Theme — `beta` Branch

> [!CAUTION]
> ### ⚠️ EXPERIMENTAL BRANCH — DO NOT USE / DO NOT TRY
> **Please do not use or try this `beta` branch on a regular or daily Jellyfin server.**
> 
> This branch is an **unstable, highly experimental testing playground with heavy mix-and-match customizations** (deep engine modifications, conflicting experiment merges, desktop vs mobile divergence, custom subtitle patches, and local test harnesses). There is too much mix-and-match occurring here—elements may break, jump, or behave unexpectedly at any time.
> 
> 👉 **For regular, stable, and plug-and-play daily usage, please stick strictly to the [`main`](https://github.com/maniratansingh/jellyfin-liquid-glass/tree/main) branch.**

---

## ⚖️ Branch Comparison: `beta` vs `main`

The `beta` branch is an architectural evolution compared to `main`. Here is how they differ:

| Feature / Aspect | `main` Branch (Legacy Base) | `beta` Branch (Next-Gen Liquid Glass) |
| :--- | :--- | :--- |
| **Theme Engine** | Abyss-derived base (~2.5k lines) | Full Apple Liquid Glass HIG Engine (`dist/jellyfin-liquid-glass.css`, 9.5k+ lines) |
| **Wallpaper** | Animated 8-color moving CSS gradient loop (`liquidMultiColorFlow`) | Static 3D Rendered Glass Art (**`iridescent.webp`**) screen-blended over deep ambient tint |
| **Performance & Battery** | Continuous GPU keyframe animation loop | **Zero continuous background animation overhead** (completely static, smooth 60fps scrolling, no battery drain) |
| **Desktop Player OSD** | Modified pill overlay | **100% Stock Desktop Liquid Glass OSD** (pristine desktop controls, authentic scrubber, zero distortion) |
| **Mobile Player OSD** | Generic mobile controls | **Dedicated Centered Frosted Glass Play/Pause Orb** (`border-radius: 50%`) with matched OSD transparency + intact bottom bar |
| **Subtitles / Closed Captions** | Standard browser placement | **Centered Apple TV Cinema Subtitles** with proportional SF Pro typography, dark contrast halo, and responsive bounds |
| **Design System** | Basic custom CSS variables | **Apple iOS 26 / macOS Tahoe HIG Dark Appearance** ladder (`--lg-accent`, `--lg-bg`, 3-tier material system, dual-axis rim lighting) |

---

## 💎 Features in `beta`

### 1. Rendered 3D Iridescent Glass Background
- **Zero-CPU Rendered Glass:** Uses the official 3D rendered glass artwork ([`iridescent.webp`](https://cdn.jsdelivr.net/gh/cj-vana/jellyfin-liquid-glass@v1.2.0/wallpapers/iridescent.webp)) rather than heavy CSS animation loops.
- **Multi-Layer Optical Compositing:**
  - **Screen Blend Layer:** Blends the glass render with a deep ambient blue/violet radial tint (`--lg-wallpaper-tint`).
  - **Specular Calibration:** Fine-tuned brightness and saturation filter (`--lg-wallpaper-filter`) to keep text crisp.
  - **Organic Veil:** Subtle grain texture and radial vignette (`--lg-wallpaper-veil`) for authentic depth.
- **Context-Aware Stepping:** The wallpaper automatically steps aside when media backdrops are active (`.withBackdrop`) or during fullscreen video playback (`.backgroundContainer-transparent`).

### 2. Dual-Experience Video Player OSD
- **Desktop (Web & PC Clients):** Restores and maintains 100% of the desktop Liquid Glass OSD interface. Floating glass pills for header and footer with full timeline scrubbing, audio/subtitle selectors, next/previous controls, and volume slider.
- **Mobile Devices (Smartphones & Tablets):**
  - **Center Play/Pause Glass Orb:** An Apple-style circular frosted glass orb positioned dead-center for quick one-thumb playback control.
  - **Matched Transparency:** The center orb transparency is calibrated to match the OSD bar, eliminating jarring contrast differences.
  - **Zero Layout Jumps:** Fixed containing-block positioning prevents layout thrashing, jumping, or clipping when toggling play/pause or rotating screens.
  - **Intact Bottom OSD:** Both the center orb AND the bottom OSD controls remain fully functional and accessible simultaneously.

### 3. Cinema-Grade Apple TV Subtitles
- **Centered Alignment:** Subtitles and closed captions are centered on the screen, eliminating awkward far-right drift.
- **Apple TV Typography:** Uses clean `-apple-system` font sizing with balanced letter spacing and line heights.
- **High-Contrast Glow Halo:** Soft dark halo behind text guarantees readability against both bright scenes and dark backgrounds without hard black boxes.

### 4. Apple Human Interface Guidelines (HIG) Glass System
- **3-Tier Material System:** Ultra-thin, regular, and thick glass materials applied contextually across app bars, dialogs, cards, and drawers.
- **Subpixel Rim Bevels:** Dual-axis top and bottom specular edge reflections mimic real refractive curved glass.
- **Tactile Physics:** SwiftUI-derived `.bouncy` and `.snappy` spring curves for responsive hover and tap micro-interactions.

---

## 🚀 How to Use `beta` (Testers & Developers Only)

> [!WARNING]
> **Reminder:** Only import this branch if you are actively participating in testing. Because this branch contains aggressive mix-and-match overrides, elements may conflict or break across Jellyfin releases. If you want a reliable daily driver, use `@main` instead.

Add one of the following `@import` rules to your **Jellyfin Dashboard → General → Custom CSS code**:

### 1. Mobile, Tablet & Desktop (Web & Native Apps)
```css
@import url("https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@beta/liquid-glass-bundle.css");
```

### 2. Android TV / Fire TV
Specifically optimized for 10-foot television screens and D-Pad remote focus navigation:
```css
@import url("https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@beta/liquid-glass-tv.css");
```

### 3. Direct Paste (No External CDN Dependency)
If you prefer not to rely on jsDelivr or external CDNs, copy the entire contents of [`dist/jellyfin-liquid-glass.css`](dist/jellyfin-liquid-glass.css) and paste it directly into your Jellyfin Custom CSS box.

---

## ⚡ Force Updating & Cache Busting

Browsers and CDN networks (jsDelivr) cache CSS files aggressively. When updating your theme or testing changes, append a version query parameter (`?v=...`) to force an immediate reload:

```css
@import url("https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@beta/liquid-glass-bundle.css?v=2");
```

Increase the version number (e.g. `?v=3`, `?v=4`) whenever you want clients to pull fresh updates.

---

## 👏 Credits & Attribution

- **Apple Liquid Glass Engine:** Built upon the design architecture and CSS engine by **cj-vana** ([jellyfin-liquid-glass](https://github.com/cj-vana/jellyfin-liquid-glass)).
- **Abyss Jellyfin Theme:** Original theme foundation by **AumGupta** ([abyss-jellyfin](https://github.com/AumGupta/abyss-jellyfin)).
