# Jellyfin Liquid Glass Theme

This is a personal project created strictly for my own personal use. I created this because the default Jellyfin UI was just too basic for my liking and I needed something more refined with a frosted glass aesthetic. 

If anyone else wants to use it, you are welcome to, but please note I built this solely for my own purposes.

## Credits & Inspiration
I really liked the design of the **Abyss Jellyfin Theme**, and I want to give full credit to the original creator, **AumGupta**. 

I used their work and built this entirely upon their code. This project is essentially a modified version of their theme. You can find their original project here: https://github.com/AumGupta/abyss-jellyfin

## What changes were made?
Starting from the Abyss theme, I made the following modifications for my personal setup:
- Added heavy "frosted glass" (backdrop-filter blur) to the navigation bars, menus, and sidebars.
- Redesigned the Video Player bottom bar to look like an Apple TV (minimalist controls, centered glass play button).
- Shrank the video player typography and icons on mobile devices so full movie names fit on the screen without getting cut off.
- Added smooth morphing animations when rotating the screen on mobile devices.

## How to use
Copy the link to the compiled CSS file and paste it into your **Jellyfin Dashboard -> General -> Custom CSS code** box:

```css
@import url('https://cdn.jsdelivr.net/gh/maniratansingh/jellyfin-liquid-glass@main/liquid-glass-bundle.css');
```
