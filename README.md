# Jellyfin Custom CSS

> **Note:** This is a personal CSS file I use for my own Jellyfin server. I am sharing it in case someone else finds it useful, but it is provided as-is. It is highly experimental and might break when Jellyfin updates.

## Credits
This is a direct modification of the **Abyss Jellyfin Theme** by **AumGupta**. I took their codebase and changed specific elements to fit my own needs. Full credit goes to them for the original theme.
Source: https://github.com/AumGupta/abyss-jellyfin

## Technical Changes from Default Jellyfin
If you apply this CSS, here is exactly what it does to the default Jellyfin UI:

1. **Backgrounds:** Adds CSS `backdrop-filter: blur(50px)` to navigation bars, dialog boxes, and sidebars to make them translucent instead of solid colors.
2. **Video Player UI:** Hides the previous track, next track, and favorite buttons via `display: none` to reduce on-screen clutter. Centers the play button.
3. **Mobile Sizing:** Reduces the CSS `font-size` and `width` values for media cards and titles on mobile resolutions (`max-width: 768px`) so that longer movie names fit on the screen without getting cut off.
4. **Performance Fix:** Removes CSS GPU hardware acceleration (`translateZ(0)`) from the login form to prevent a bug where the login screen becomes unclickable on WebKit browsers (Safari/iOS).

## How to use
Add this to your **Jellyfin Dashboard -> General -> Custom CSS code**:

```css
@import url('https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@main/liquid-glass-bundle.css');
```
