# Jellyfin Liquid Glass Theme

> **Note:** This is a personal CSS theme I use for my own Jellyfin server. I am sharing it in case someone else finds it useful, but it is provided as-is. It is highly experimental and might break when Jellyfin updates.

## Credits
This is a direct modification of the **Abyss Jellyfin Theme** by **AumGupta**. I used their work as the foundation and modified it heavily to fit my own needs. Full credit goes to them for the original theme. 
Source: https://github.com/AumGupta/abyss-jellyfin

## Comprehensive Explanation of Changes
If you add this CSS to your Jellyfin server, here is a comprehensive list of exactly what it changes compared to the stock Jellyfin UI:

### 1. Frosted Glass UI (Backdrop Filters)
- Replaces solid dark backgrounds with translucent frosted glass (`backdrop-filter: blur`) across the entire application.
- This applies to the main sidebar, pop-up dialog boxes, the user profile drawer, action sheets, and the mobile bottom navigation bar.

### 2. Video Player Clean-Up (OSD)
- **Hidden Buttons:** Completely removes the "Favorite (Heart)", "Next Track", "Previous Track", "Cast", and "SyncPlay" buttons from the video player to reduce screen clutter.
- **Kept Buttons:** You will only see the Play/Pause orb, Rewind, Fast Forward, Volume, Settings, Subtitles, and Fullscreen.
- **Resizing:** Slightly shrinks the top-bar icons and the main Play/Pause button so they take up less space on the screen.

### 3. Mobile Device Optimizations
- **Text Sizing:** Reduces the font size of movie and TV show titles specifically on mobile phones. This prevents long titles from getting cut off or hidden.
- **Poster Sizing:** Adjusts the width of media cards on mobile so they fit the screen better.
- **Screen Rotation:** Adds a smooth 0.5-second CSS transition animation to the video player. When you rotate your phone from portrait to landscape, the video controls resize smoothly instead of instantly snapping and glitching.
- **Bottom Navigation:** Adds a subtle top border to the mobile bottom navigation bar to separate it from the main content.

### 4. General Tweaks & Bug Fixes
- **Hidden Badges:** Hides the small "Watched" (Checkmark) and "Favorite" (Heart) badge indicators that usually sit on top of movie posters.
- **Login Screen Bug Fix:** Removes aggressive CSS GPU hardware acceleration (`translateZ(0)` and `isolation`) specifically from the login form. This fixes a known bug where WebKit browsers (like Safari and iPhones) would freeze or ignore clicks on the username and password fields.

## How to use
Add this to your **Jellyfin Dashboard -> General -> Custom CSS code**:

```css
@import url('https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@main/liquid-glass-bundle.css');
```
