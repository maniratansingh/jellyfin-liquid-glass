# Jellyfin Liquid Glass Theme — `test` Branch

> [!CAUTION]
> ### 🛑 DO NOT USE THIS BRANCH — ALWAYS IN-FLIGHT / UNSTABLE
> **Users should NEVER use or import from this `test` branch.**
> 
> This branch is an **unstable, internal development staging ground that is ALWAYS in between something**. Code here frequently represents incomplete features, work-in-progress refactors, experimental debugging sessions, or broken interim commits. It is not maintained for direct consumption and can break your Jellyfin UI at any moment without warning.
> 
> 👉 **Which branch should you use?**
> - **[`main`](https://github.com/maniratansingh/jellyfin-liquid-glass/tree/main)**: The official **stable branch** for normal, daily, plug-and-play usage.
> - **[`beta`](https://github.com/maniratansingh/jellyfin-liquid-glass/tree/beta)**: The **experimental preview branch** featuring the next-generation Apple Liquid Glass engine.

---

## ⚖️ Branch Architecture Overview

The `test` branch tracks active in-flight experiments cloned from `beta`. Here is how the branches relate:

| Feature / Aspect | `main` Branch (Stable) | `beta` Branch (Staged Preview) | `test` Branch (Internal In-Flight) |
| :--- | :--- | :--- | :--- |
| **Status** | 🟢 **Stable & Daily Driver** | 🟡 **Experimental Preview** | 🔴 **DO NOT USE (Always Mid-Work)** |
| **Theme Engine** | Abyss-derived base (~2.5k lines) | Full Apple Liquid Glass HIG Engine (`dist/jellyfin-liquid-glass.css`, 9.5k+ lines) | Cloned from `beta` with active in-flight changes |
| **Wallpaper** | Animated 8-color moving CSS gradient loop (`liquidMultiColorFlow`) | Static 3D Rendered Glass Art (**`iridescent.webp`**) | Static 3D Rendered Glass Art or active test renders |
| **Performance** | Continuous GPU keyframe animation loop | **Zero continuous background animation overhead** (static, 60fps scrolling) | Unoptimized / fluctuating profiling state |
| **Desktop Player OSD** | Modified pill overlay | **100% Stock Desktop Liquid Glass OSD** | In-flight testing modifications |
| **Mobile Player OSD** | Generic mobile controls | **Dedicated Centered Frosted Glass Play/Pause Orb** (`border-radius: 50%`) | In-flight testing modifications |
| **Subtitles / CC** | Standard browser placement | **Centered Apple TV Cinema Subtitles** | In-flight testing adjustments |

---

## 💎 Features Inherited from `beta`

### 1. Rendered 3D Iridescent Glass Background
- **Zero-CPU Rendered Glass:** Uses official 3D rendered glass artwork ([`iridescent.webp`](https://cdn.jsdelivr.net/gh/cj-vana/jellyfin-liquid-glass@v1.2.0/wallpapers/iridescent.webp)) rather than heavy CSS animation loops.
- **Multi-Layer Optical Compositing:** Blends glass render with deep ambient tint (`--lg-wallpaper-tint`), calibrated filter (`--lg-wallpaper-filter`), and grain veil (`--lg-wallpaper-veil`).
- **Context-Aware Stepping:** Wallpaper steps aside when media backdrops are active (`.withBackdrop`) or during fullscreen video playback (`.backgroundContainer-transparent`).

### 2. Dual-Experience Video Player OSD
- **Desktop (Web & PC Clients):** 100% stock desktop Liquid Glass OSD interface.
- **Mobile Devices (Smartphones & Tablets):** Centered floating frosted glass Play/Pause Orb (`border-radius: 50%`) with matched transparency and zero layout shifts, while keeping bottom OSD intact.

### 3. Cinema-Grade Apple TV Subtitles
- Centered alignment, Apple `-apple-system` typography, and soft dark glow halo.

### 4. Apple HIG Glass Design System
- 3-tier material system, subpixel rim bevels, and SwiftUI-derived physics curves.

---

## ⚠️ Branch Import References (Internal Testing Only)

> [!WARNING]
> Again: **Do not add these links to your production Jellyfin server.** Use `main` instead.

```css
/* DO NOT USE - Test branch bundle (constantly fluctuating) */
@import url("https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@test/liquid-glass-bundle.css");
```

---

## 👏 Credits & Attribution

- **Apple Liquid Glass Engine:** Built upon the design architecture and CSS engine by **cj-vana** ([jellyfin-liquid-glass](https://github.com/cj-vana/jellyfin-liquid-glass)).
- **Abyss Jellyfin Theme:** Original theme foundation by **AumGupta** ([abyss-jellyfin](https://github.com/AumGupta/abyss-jellyfin)).
