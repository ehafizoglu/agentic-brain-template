---
project: "PROJECT_NAME"
role: "UI/UX Designer"
last_updated: 2026-07-02
tags:
  - role/design
  - design-system
  - typography
  - colors
---

# 🎨 UI/UX: Design System & Styling Tokens

◀️ Back to [[Project_Hub]] | Requirements: [[business_requirements]]

This document defines the branding identity, styling tokens, typography, and visual rules for **PROJECT_NAME**. All frontend code must use these variables.

---

## 🎨 1. Premium Color System (HSL Palette)

We use custom HSL variables to support clean light/dark modes and consistent overlays:

| Token Name | HSL Value | Hex Equivalent | Role / Use Case |
| :--- | :--- | :--- | :--- |
| `--color-bg-primary` | `hsl(220, 15%, 8%)` | `#0f1216` | Main application background (sleek dark mode) |
| `--color-bg-surface` | `hsl(220, 15%, 12%)` | `#161a22` | Cards, sidebars, modal surfaces |
| `--color-text-primary`| `hsl(210, 20%, 98%)` | `#f8f9fa` | Titles, body text (high contrast) |
| `--color-text-muted` | `hsl(215, 12%, 60%)` | `#8c96a5` | Subtitles, labels, disabled statuses |
| `--color-primary` | `hsl(255, 85%, 65%)` | `#6d5bfa` | Buttons, links, primary highlights (Vibrant Purple) |
| `--color-accent` | `hsl(180, 85%, 45%)` | `#14ebd9` | Secondary alerts, notifications (Glassmorphism cyan) |

---

## 🔤 2. Typography Hierarchy
We use **Inter** or **Outfit** as our main typography font family, with browser system fallbacks:

*   **Header 1 (Page Titles)**: `font-size: 2.25rem (36px) | line-height: 1.2 | font-weight: 800`
*   **Header 2 (Section Subheaders)**: `font-size: 1.5rem (24px) | line-height: 1.3 | font-weight: 700`
*   **Body Text (Standard)**: `font-size: 1rem (16px) | line-height: 1.5 | font-weight: 400`
*   **Small Caption (Footnotes, labels)**: `font-size: 0.85rem (13px) | line-height: 1.4 | font-weight: 500`

---

## 📐 3. Grid & Spacing System
All margins, padding, and layout columns must follow a base-8 grid:

*   `--spacing-2xs`: `4px`
*   `--spacing-xs`: `8px`
*   `--spacing-sm`: `16px`
*   `--spacing-md`: `24px`
*   `--spacing-lg`: `32px`
*   `--spacing-xl`: `48px`

---

## ✨ 4. Component Styling & Glassmorphism

### Cards & Surfaces
```css
.premium-card {
  background: rgba(22, 26, 34, 0.7);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: var(--spacing-sm);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
}
```

### Micro-Animations (Button Hover Example)
```css
.button-primary {
  transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s ease;
}
.button-primary:hover {
  transform: translateY(-2px);
  background-color: hsl(255, 85%, 70%);
}
.button-primary:active {
  transform: translateY(0);
}
```
