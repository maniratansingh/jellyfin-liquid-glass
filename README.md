# Jellyfin Liquid Glass Theme

> **Note:** This is a personal CSS theme I use for my own Jellyfin server. I am sharing it in case someone else finds it useful, but it is provided as-is. It is highly experimental and might break when Jellyfin updates.

## Credits
This is a direct modification of the **Abyss Jellyfin Theme** by **AumGupta**. I used their work as the foundation and modified it to fit my own needs. Full credit goes to them for the original theme.
Source: https://github.com/AumGupta/abyss-jellyfin

## What exactly does this code do?
If you add this CSS to your Jellyfin server, it will change the following things:

1. **Frosted Glass Overlays:** It changes the background of all menus, sidebars, and pop-up dialogs to look like translucent frosted glass instead of solid dark colors.
2. **Minimalist Video Player:** It hides the "Favorite", "Next Track", and "Previous Track" buttons on the video player to make the control bar look much cleaner and less cluttered.
3. **Better Mobile Text Sizing:** It shrinks the font size of movie and show titles on mobile phones so that long names actually fit on the screen without getting cut off. 
4. **Smooth Screen Rotation:** It adds a smooth transition animation when you rotate your phone sideways, so the video player resizes smoothly instead of instantly snapping.

## How to use
Add this to your **Jellyfin Dashboard -> General -> Custom CSS code**:

```css
@import url('https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@main/liquid-glass-bundle.css');
```
