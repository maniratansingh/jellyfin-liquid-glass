# Experimental Branch — Changelog & Diff from `main`

> **Branch:** `experimental`  
> **Status:** Active development — do not merge to `main` without review  
> **CDN link:**
> ```
> https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@experimental/liquid-glass-bundle.css
> ```

---

## What is `experimental`?

`experimental` is the active design lab for the Jellyfin Liquid Glass theme. It receives all new visual features, glass physics improvements, and layout experiments **before** they are considered stable enough for `main`.

`main` is the last known-good, stable release. It is **never touched** during experimental development.

---

## How to use `experimental`

Paste into **Jellyfin → Dashboard → General → Custom CSS**:

```css
@import url("https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@experimental/liquid-glass-bundle.css");
```

Hard-refresh after saving: `Ctrl+Shift+R` / `Cmd+Shift+R`

> **Note:** jsDelivr caches for up to 12 hours. If you don't see changes immediately, wait or use a cache-busted URL.

---

## Commits in `experimental` not in `main`

| Commit | Description |
|--------|-------------|
| *latest* | **Fix:** Un-hide `.pageTitle`, disable displaced `.detailLogo`, and enforce bold white typography for movie, TV series, season, and episode titles (`.nameContainer`, `.itemName`, `.parentName`) |
| `7f68ad0` | **Fix:** Restore movie, TV show, season, and episode titles on detail pages |
| `bfa1f4a` | **Fix:** Remove `.paging ~ div` rule which was hiding detail page contents |
| `20acdb4` | **Docs:** Add `EXPERIMENTAL.md` documentation guide |
| `795d750` | **Polish:** Clean rewrite — no cascade conflicts, refined glass, thin scrollbar, strict 3-button layout |
| `9489cf3` | **Fix:** Strict 3-button layout (Play, Download, Three-Dot) and Apple Tahoe liquid glass optics |
| `cf0a9cd` | **Feature:** Restrict to only Play, Download, and Three-Dot buttons; hide all others |
| `fa6f294` | **Feature:** Medium button sizing, re-hide extra buttons, ultra-prominent liquid glass optics |
| `517d95b` | **Feature:** Refine pill size, boost multi-colour liquid spectrum, amplify glass optics |
| `8a3c3e4` | **Feature:** Unhide Download & More actions, implement iPhone Fold liquid glass capsule aesthetic |
| `13f8fb4` | **Feature:** Accentuated Apple Tahoe liquid glass refraction & luminous fluid background |
| `e8fa9e4` | **Feature:** Animated liquid mesh gradient based on shader colour palette |

---

## What changed vs `main` — Feature by Feature

### 1. Animated Liquid Gradient Background
- **`main`:** Static dark Abyss-theme background
- **`experimental`:** 8-colour animated mesh gradient — deep navy, cobalt, violet, teal — smoothly morphing with CSS keyframes. Gives the backdrop a living, fluid quality that interacts with the glass panels above it.

---

### 2. Apple Tahoe Liquid Glass Panels
- **`main`:** Default Abyss theme panel backgrounds (flat dark)
- **`experimental`:** Full liquid glass physics on all panels — dialogs, drawers, detail page containers, action sheets, skin header:
  - `backdrop-filter: blur(48px) saturate(280%) brightness(125%) contrast(112%)`
  - Dual-axis specular gradient (135° + 180°)
  - Chromatic bevel rim — bright `border-top`, fading `border-bottom`
  - Layered inset glow + deep ambient drop shadow
  - Glass tint: `rgba(10, 16, 36, 0.25)` — dark navy, low opacity, lets background bleed through

---

### 3. Strict 3-Button Layout on Detail Page
- **`main`:** All default Jellyfin buttons visible (Play, Restart, Trailer, Instant Mix, Shuffle, Delete, Record, Played, Favourite, SyncPlay, Rating, Edit)
- **`experimental`:** **Only 3 buttons shown:**
  1. ▶ **Play / Resume**
  2. ↓ **Download** (only if user has download permission)
  3. ⋮ **Three-Dot / More**

  All other buttons are hidden with `display: none !important`. Logic uses a clean **A → B cascade**:
  - **A:** `#itemDetailPage .mainDetailButtons > *` → `display: none` (nuke all)
  - **B:** Whitelist exactly the 3 buttons → `display: inline-flex`

---

### 4. Liquid Glass Action Buttons
- **`main`:** Default Jellyfin/Abyss flat buttons
- **`experimental`:** All 3 detail-page buttons styled as Apple Tahoe liquid glass pills:
  - Height: `42px` (medium — Apple standard)
  - Border-radius: `9999px` (full pill)
  - Glass body: `rgba(255,255,255,0.14)` base + dual specular gradient
  - `backdrop-filter: blur(40px) saturate(360%) brightness(148%)`
  - Specular razor rim: bright `border-top: 1.5px solid rgba(255,255,255,0.92)`
  - Inset glow + ambient outer glow
  - Hover: `translateY(-2px) scale(1.03)` with spring easing
  - Active press: `scale(0.97)` — tactile snap
  - Three-Dot is a **42×42px circular glass orb**, same material

---

### 5. Video Player OSD — Floating Glass Pills
- **`main`:** Default full-width OSD bars
- **`experimental`:**
  - Top bar + bottom controls styled as **floating pill-shaped glass** (`border-radius: 50px`, `width: max-content`, `margin: 14px auto`)
  - Play/Pause button is a dedicated **glass orb** with `border-radius: 50%`
  - OSD container itself is transparent — no double-glass stacking
  - Smooth rotation/resize transition: `all 0.45s cubic-bezier(0.25, 1, 0.5, 1)`

---

### 6. Scrollbar — Mac Thin Style
- **`main`:** Default browser scrollbar or Abyss scrollbar (14px wide)
- **`experimental`:** Thin Mac-style overlay scrollbar — `6px` wide, fully rounded, semi-transparent, invisible track. Disappears into the UI, appears on hover.

---

### 7. Card & List Clutter Removed
- **`main`:** Overlay buttons (Played, Favourite, More) appear on poster cards and list rows on hover
- **`experimental`:** All overlay buttons hidden. Only the primary play FAB (`.cardOverlayFab-primary`) is kept. List items show no side buttons. Poster indicators (watched checkmark, heart) are hidden.

---

### 8. Library Header Cleaned
- **`main`:** View controls (Play All, Sort, Filter, Layout toggle) shown in library headers
- **`experimental`:** All hidden — `button[data-action="playall"]`, `button[data-action="sort"]`, `button[data-action="filter"]`, `.btnChangeLayout`, `.headerTabs`

---

### 9. Mobile & Native App Optimisations
- **`main`:** Standard web styling for all screen sizes
- **`experimental`:**
  - Mobile (`max-width: 768px`): lighter `blur(44px) saturate(220%)`, no double gradient, no big shadows — keeps it fast
  - OSD on mobile: `backdrop-filter: none` — pure speed
  - Native app (`html.cordova`, `html.ios`, `html.android`): reduced gradient complexity for GPU budget
  - `.layout-mobile`: `user-select: none`, `-webkit-touch-callout: none`, native momentum scrolling

---

### 10. Action Sheet
- **`main`:** Default Abyss action sheet
- **`experimental`:** Full glass action sheet — `border-radius: 24px`, liquid glass body, bright top rim, deep ambient shadow. Menu items get `border-radius: 14px` with a subtle hover highlight (`rgba(255,255,255,0.12)`).

---

### 11. Login Form
- **`main`:** Default login card
- **`experimental`:** Glass login card — `blur(50px) saturate(220%)`, dark navy tint, top/left specular edges.

---

## Files Changed

| File | Role |
|------|------|
| `src/dark-physics-port.css` | All experimental custom CSS — source of truth |
| `src/theme.css` | Base Abyss theme (minor tweaks only) |
| `liquid-glass-bundle.css` | **Compiled output** — `theme.css` + `dark-physics-port.css` concatenated. This is what the CDN serves. |
| `liquid-glass-tv.css` | TV layout variant — untouched in this branch |

---

## Design Language

The experimental branch follows the **Apple Tahoe / iPhone Fold** glass aesthetic:

- **Material:** Crystalline refractive glass — bright top specular, fading downward, dark bottom edge
- **Blur:** High (`blur(40–48px)`) with `saturate(280–360%)` to pull vivid colour from the background through the glass
- **Colour:** No solid fills — everything reads the background through the glass
- **Motion:** Expo-out (`cubic-bezier(0.32, 0.72, 0, 1)`) for settles; spring-bounce (`cubic-bezier(0.34, 1.2, 0.64, 1)`) for pops
- **Sizing:** Apple standard medium — `42px` height, `22px` horizontal padding

---

*Last updated: experimental commit `795d750`*
