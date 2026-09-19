# Design System Specification: Editorial Precision & Depth

## 1. Overview & Creative North Star
The "Creative North Star" for this design system is **The Dimensional Curator**. This system moves beyond the flat, utilitarian nature of standard fintech and utility apps, opting instead for a high-end editorial feel that prioritizes visual breathing room, sophisticated layering, and intentional asymmetry.

We reject the "boxed-in" look. By utilizing a generous `1rem` (16px) corner radius and a scale of "Tonal Layering," we create a UI that feels like a collection of floating glass and paper elements. The goal is to provide a sense of premium security through depth rather than density.

### Key Principles:
* **Intentional Asymmetry:** Break the grid with staggered card layouts and overlapping navigation elements (like the prominent central AI action).
* **Depth via Tone:** We use color shifts, not borders, to define space.
* **Editorial Scale:** Bold headers against refined, readable body text using the Manrope typeface.

---

## 2. Colors
Our palette is curated to balance professional trust with futuristic energy.

### Primary & Functional
* **Primary Blue (`#2563EB`):** Used for "Primary Container" surfaces and high-impact actions. It represents the core of the user's data.
* **Secondary Success (`#22C55E`):** Reserved for positive growth, "Recommended" badges, and completed states. Use as a subtle wash (Secondary Fixed) for background accents.
* **Accent AI Purple (`#7C3AED`):** The "Spirit" of the system. Used for the central AI hub and energetic gradients.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders to separate sections.
Boundaries must be defined through:
1. **Background Shifts:** Place a `surface_container_lowest` card on a `surface_container_low` background.
2. **Tonal Transitions:** Use soft shifts in gray to denote the end of a list or the start of a new module.

### Signature Textures & Glass
* **The AI Gradient:** Transitions from `tertiary` (#7C3AED) to `primary` (#004ac6). Use this for high-value AI interactions.
* **Glassmorphism:** For the navigation bar and floating headers, use semi-transparent surface colors (`surface` at 80% opacity) with a `24px` backdrop-blur to allow the content underneath to "bleed" through softly.

---

## 3. Typography
We use **Manrope**, a modern geometric sans-serif, to bridge the gap between technical precision and human friendliness.

* **Display (lg/md/sm):** High-impact, used for balances and hero headlines. Use `tight` letter-spacing (-0.02em).
* **Headline (lg/md/sm):** Bold, authoritative section titles.
* **Title (lg/md/sm):** Semibold weights for card headers and navigation items.
* **Body (lg/md/sm):** Regular weight with generous line-height (1.6) for maximum readability.
* **Labels:** All-caps or tracked-out labels (`0.05em`) for utility text like "TOTAL BALANCE" or "RECOMMENDED."

---

## 4. Elevation & Depth
In this design system, elevation is an environmental property, not just a shadow effect.

### The Layering Principle
Depth is achieved by "stacking" the surface-container tiers.
* **Level 0 (Base):** `surface` (#f8f9fa).
* **Level 1 (Sections):** `surface_container_low` (#f3f4f5).
* **Level 2 (Cards):** `surface_container_lowest` (#ffffff).
* **Level 3 (Interactive):** `primary_container` (#2563eb) for high-focus elements like the balance card.

### Ambient Shadows
When a floating effect is required (e.g., the central AI button), use **Ambient Shadows**:
* **Blur:** 32px to 64px.
* **Opacity:** 4% - 8%.
* **Color:** Tint the shadow with the `on_surface` color (#191c1d) rather than using pure black.

### The Ghost Border Fallback
If a border is required for accessibility (e.g., an input field), use the `outline_variant` at **15% opacity**. Never use 100% opaque borders.

---

## 5. Components

### Primary Cards
Cards use a `xl` (1.5rem/24px) or `lg` (1rem/16px) radius.
* **Style:** No borders. High-contrast backgrounds (`primary_container` or `surface_container_lowest`).
* **Padding:** Always use `spacing.6` (1.5rem) or `spacing.8` (2rem) for internal card breathing room.

### Buttons
* **Primary:** `primary_container` background with `on_primary` text. `xl` roundedness.
* **AI Button:** Floating, circular (`full` roundedness) with the AI Gradient and an extra-diffused ambient shadow. It should overlap the navigation bar, breaking the horizontal plane.
* **Secondary:** Glass-style. `surface_container_high` with 40% opacity and a subtle backdrop blur.

### Navigation Bar (STRICT RULE)
The bottom navigation bar is a FIXED, REUSABLE component.
- It must be copied EXACTLY from the Dashboard screen
- It must NOT be redesigned, restyled, or regenerated
- It must remain identical across ALL screens
This includes:
- Same icons
- Same labels
- Same spacing
- Same blur effect
- Same active state behavior
The navigation bar is NOT part of the creative layout system.
It is a global UI component and must remain consistent.
No asymmetry, no variation, no reinterpretation is allowed for the navbar.
---

## 6. Do's and Don'ts

### Do:
* **DO** use whitespace as a separator. If you feel you need a line, add `16px` of padding instead.
* **DO** stagger elements. An asymmetrical layout feels "custom" and premium.
* **DO** use the `secondary_container` (#6bff8f) for subtle success banners to create a fresh, "minty" aesthetic.
* **DO** overlap the AI action over other components to signify its importance as a "global layer."

### Don't:
* **DON'T** use 1px solid dividers. They clutter the editorial feel.
* **DON'T** use harsh drop shadows. If it looks like a "box shadow" from 2010, it's too heavy.
* **DON'T** crowd the edges. Respect the `spacing.6` (1.5rem) gutter at all times.
* **DON'T** use pure black (#000000) for text. Always use `on_surface` (#191c1d) to maintain tonal softness.


IMPORTANT: Reuse the bottom navigation bar from the Dashboard screen on every page.
- Do NOT redesign it
- Do NOT change icons or labels
- Do NOT adjust spacing or style
It must remain identical across all screens to maintain UI consistency.