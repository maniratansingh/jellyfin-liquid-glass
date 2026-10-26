# Jellyfin Web DOM Selector Inventory

This inventory documents verified CSS selectors in Jellyfin Web (10.9.x – 10.10.x), their parent structures, intended visual treatments under Apple Liquid Glass, and stability ratings.

---

| Component | Target Selector | Parent Hierarchy | Intended Glass Treatment | Stability |
| :--- | :--- | :--- | :--- | :--- |
| **App Header Bar** | `.skinHeader.focuscontainer-x` | `body > .skinHeader` | Floating glass capsule with top/bottom specular rim, 18px blur, translucent fill | High (Core layout) |
| **Header Title / Tabs** | `.headerTabs.sectionTabs` | `.skinHeader` | Inset pill tab group with active indicator capsule | High |
| **Tab Button** | `.emby-tab-button` | `.headerTabs` | Rounded capsule, subtle background glow when focused or active | High |
| **Drawer / Sidebar** | `.mainDrawer` | `body > .mainDrawer` | Vertical glass panel, 28px blur, 0.12 fill, specular right border | High |
| **Drawer Nav Item** | `.navMenuOption` | `.mainDrawerScrollContainer` | Pill item, 10px radius, hover illumination | High |
| **Search Input** | `.searchContainer .emby-input` | `.searchContainer` | Pill-shaped glass container with search icon, subtle inset highlight | High |
| **Poster Card** | `.card` | `.itemsContainer` | Crisp artwork, smooth 14px rounded corners, subtle hover elevation | High |
| **Card Box** | `.cardBox` | `.card` | Transparent background, zero poster obscuration | High |
| **Card Scalable** | `.cardScalable` | `.cardBox` | Overflow hidden with continuous corner curve | High |
| **Card Indicators** | `.indicator` | `.cardScalable` | Floating dark glass pill badge with bright label | High |
| **Detail Ribbon** | `.detailRibbon` | `.itemDetailPage` | Translucent backdrop scrim with smooth gradient bleed | High |
| **Detail Action Buttons** | `.detailButton` | `.detailButtons` | Capsule button with specular rim, active press scale | High |
| **Modal Dialog** | `.dialog` | `body > .dialogContainer` | Elevated glass panel, 32px blur, prominent specular rim and drop shadow | High |
| **Context Menus** | `.actionSheet, .menuContainer`| `body` | Compact floating glass panel with rounded corners | High |
| **Video Player Top OSD** | `.videoOsdTop, .osdHeader` | `.videoPlayerContainer` | Floating top glass pill with back button and media title | High |
| **Video Player Bottom OSD**| `.videoOsdBottom` | `.videoPlayerContainer` | Floating bottom glass pill holding seek bar and playback controls | High |
| **Central Play Orb** | `.osdControls .btnPlay` | `.osdControls` | Circular glass orb (48px/56px), specular highlight, hover glow | High |
| **Sliders / Seekbar** | `.mdl-slider-background-flex` | `.sliderContainer` | Sleek 4px track, glowing accent progress bar, round glass thumb | High |
| **Form Inputs** | `.emby-input, .emby-select` | `.inputContainer` | Recessed glass field with subtle inner shadow and highlight | High |
| **Toggle Switches** | `.emby-checkbox-label` | `.checkboxContainer` | Apple-style rounded toggle switch with smooth slide transition | High |
