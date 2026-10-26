# Reverse-Engineering Apple Liquid Glass for Jellyfin (CSS-Only)
**Date:** October 26, 2026  
**Status:** Completed  
**Target:** Jellyfin Web CSS Customization  

---

## 1. Executive Summary & Goals

Apple's **Liquid Glass** represents a major evolution in interface materials, bridging the gap between flat frosted glass (`backdrop-filter: blur`) and dynamic optical lenses that interact with ambient light and underlying content.

The goal of this project is to reverse-engineer the core visual and physical principles of Apple Liquid Glass and translate them into a pure, zero-dependency, CSS-only implementation tailored specifically for **Jellyfin Web**.

---

## 2. Primary-Source Analysis: Apple Design Language

### A. Apple Human Interface Guidelines — Materials & Liquid Glass
1. **Functional Layering:**
   - Liquid Glass forms a distinct, floating functional layer for navigation and control surfaces that floats *above* the content layer.
   - It is intentionally **reserved for controls and navigation** (app bars, toolbars, sidebars, floating player pills, action sheets).
   - It is **not** applied indiscriminately across content cards, thumbnails, or posters. Applying glass over every item creates visual clutter and reduces legibility.
2. **Optical Transparency & Edge Refraction:**
   - Apple's Liquid Glass is not a dense milky blur; it is remarkably clear (often 2%–10% base fill opacity).
   - Rather than obscuring content, it bends light primarily at its **rim and edges**, creating an unmistakable specular highlight that delineates the physical boundary of the glass capsule.
3. **Specular Sheen & Dynamic Highlights:**
   - Light strikes the top and leading edges of glass objects, creating a 0.5px to 1px bright rim (`rgba(255, 255, 255, 0.25)` to `0.45`), coupled with a subtle inner shadow or gradient sheen (`linear-gradient(135deg, rgba(255, 255, 255, 0.12), transparent)`).
4. **Transient Interactivity:**
   - Interactive elements (capsules, buttons, sliders, active tabs) elevate slightly on hover and illuminate smoothly, simulating increased light transmission when manipulated.

### B. SwiftUI Glass Effect (`.glassEffect(_:in:)`)
- In SwiftUI, glass takes parameters for tint, shape (`Capsule`, `RoundedRectangle`), and interactive elevation.
- Glass components automatically handle contrast adaptation against variable backgrounds.

---

## 3. Comparative Analysis of Open-Source References

| Reference | Technique Used | Strengths | Limitations for Pure CSS Web |
| :--- | :--- | :--- | :--- |
| **`abyss-jellyfin`** (AumGupta) | Solid dark tokens, custom fonts, full layout restructure | Excellent Jellyfin DOM coverage, robust selector architecture | Heavy solid backgrounds, no true glass lens physics |
| **`cj-vana/jellyfin-liquid-glass`** | Tiered glass (`control`, `bar`, `panel`, `clear`), multi-layer pseudos (`::before` frost, `::after` rim) | Superb token model, authentic iOS 26 HIG styling, floating capsules | Uses complex build step and SVG displacement filters that add overhead |
| **`lucaperullo/simple-liquid-glass`** | React + WebGL shaders / SVG chromatic aberration | True optical refraction and chromatic aberration | Violates the strict CSS-only constraint (requires JS / WebGL) |
| **Current Baseline** (`liquid-glass-bundle.css`) | Custom OSD floating pills, mobile rotation fixes, frosted dialogs | Great mobile OSD usability, proven stability | Inconsistent glass rim highlights, some overly milky panels, mixed opacity |

---

## 4. Translating Apple Liquid Glass to Pure CSS

Since WebGL, JavaScript, and external SVG displacement maps are prohibited by our non-negotiable constraints, we translate Apple's visual characteristics into pure CSS techniques:

### 1. Dual-Pseudo Architecture
On glass host containers:
- **`host`**: Set `position: relative; isolation: isolate;` so child elements (text, icons) render sharply without inheritance artifacts.
- **`::before` (The Frost & Ambient Light)**:
  - `backdrop-filter: blur(var(--lg-blur)) saturate(var(--lg-saturate))`
  - `background: var(--lg-tint)` (subtle tinted translucent fill)
  - `border-radius: inherit`
  - `z-index: -1`
- **`::after` (The Specular Rim & Lens Sheen)**:
  - `box-shadow`: multi-stop specular rim consisting of an inset top highlight (`inset 0 1px 1px rgba(255,255,255,0.28)`), an inset bottom dark rim (`inset 0 -1px 1px rgba(0,0,0,0.4)`), and an outer soft ambient shadow (`0 8px 32px rgba(0,0,0,0.35)`).
  - `background`: `linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.01) 40%, rgba(0,0,0,0.15) 100%)`
  - `pointer-events: none`

### 2. Tiered Glass Hierarchy
We define three distinct glass tiers:
1. **Control / Pill Tier:**
   - High transparency (fill 4%–8%), fast blur (8px–12px), sharp 9999px capsule radii, bright specular edge. Used on buttons, tab capsules, search bar, and playback orbs.
2. **Bar / Navigation Tier:**
   - Medium transparency (fill 8%–14%), balanced blur (16px–24px), 18px–28px radius. Used on floating app bar, bottom nav bar, and OSD pill bars.
3. **Panel / Overlay Tier:**
   - Higher opacity (fill 18%–26%) for legibility, deep blur (28px–40px), rich saturation (140%–160%), soft outer shadow. Used on modal dialogs, context menus, and navigation drawer.

### 3. Graceful Fallbacks
For browsers lacking `backdrop-filter` support:
```css
@supports not (backdrop-filter: blur(10px)) {
  :root {
    --lg-glass-control-bg: rgba(28, 28, 34, 0.92);
    --lg-glass-bar-bg: rgba(20, 20, 24, 0.94);
    --lg-glass-panel-bg: rgba(16, 16, 20, 0.96);
  }
}
```

### 4. Accessibility & Reduced Motion
- `@media (prefers-reduced-motion: reduce)` removes all transform scale animations and sets transitions to 0s.
- Clear 2px focus ring (`--lg-focus-ring`) with high contrast for keyboard navigation.
