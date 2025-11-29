# GTMstack.pro Component Library Guide
## Navigate Your GTM Journey - Reusable HTML/CSS Components

---

## 📚 Library Overview

This component library provides production-ready HTML/CSS patterns that strictly follow the GTMstack.pro Global Brand System. All components are pure HTML—no React, no JavaScript frameworks—designed to be copy-pasted into static HTML pages.

**View Live Library:** Open `/component-library.html` in your browser

---

## 🎨 Brand System Compliance

All components enforce:
- **Deep Navy (#0A0F1F)** - Primary dark backgrounds
- **Electric Blue → Purple Gradients** - CTAs and accents (#3A7DFF → #A855FF)
- **Navigation Motifs** - Topographic patterns, grid overlays, route lines
- **Consulting Typography** - Bold headings (700-800 weight), clean body text
- **Premium Interactions** - Card hovers, button animations, smooth transitions
- **No Plain Sections** - Every component includes visual elements

---

## 📦 Component Categories

### 1. **Hero Components**
- **Primary Hero** - Full-width navy background with stats, dual CTAs
  - Use on: Homepage, major landing pages
  - Includes: Badge, H1, subheadline, CTAs, statistics grid
  
- **Secondary Hero** - Simpler gradient header
  - Use on: About, Industries, Contact pages
  - Includes: H1, supporting text, subtle motifs

### 2. **Navigation Bar**
- Sticky deep navy navigation
- Logo + menu links + CTA button
- Use on: Every page (site-wide)

### 3. **Section Headers**
- Gradient strip with navy background
- Badge + H2 + description
- Use on: Major section introductions

### 4. **Card Components**

**Service Card:**
- Icon + title + description + CTA link
- Use on: Expertise overview pages
- Variants: 3-column grid layout

**Industry Card:**
- Gradient background with bullet list
- Use on: Industries overview page
- Includes: Icon, title, 3 bullets, CTA

**Case Study Card:**
- Image/gradient top, content bottom
- Challenge → Solution → Outcome format
- Use on: Projects page, case study listings

### 5. **Content Sections**

**Two-Column Feature:**
- Text left, visual right (or reversed)
- Badge + H2 + body + bullet list + CTA
- Use on: Service pages, about page

**Statistics Module:**
- 4-stat grid with large numbers
- Navy gradient background
- Use on: Homepage, about page, landing pages

**Alternating Content Blocks:**
- Visual + text alternating sides
- Use on: Long-form pages to create rhythm

### 6. **GTM Framework Components**

**4-Pillar Framework:**
- Four cards with numbered pillars (01-04)
- Icon, title, description, bullet list per card
- Use on: Homepage, expertise overview

**Journey/Process Module:**
- 4-step horizontal journey
- Connecting line between steps
- Numbered badges + icons + descriptions
- Use on: Homepage, about page, process pages

### 7. **CTA Components**

**Primary CTA Block:**
- Full-width navy background with route lines
- Large headline, subheadline, dual CTAs
- Use on: Bottom of major pages before footer

**Secondary CTA:**
- Lighter background, simpler layout
- Use on: Mid-page conversions

### 8. **Footer**
- 4-column layout: Brand + Navigation + Services + Connect
- Navy background with dividers
- Legal links at bottom
- Use on: Every page (site-wide)

---

## 🚀 How to Use Components

### Step 1: Open Component Library
```bash
Open: /app/component-library.html in browser
```

### Step 2: Find Component
Browse to the section you need (Hero, Cards, CTAs, etc.)

### Step 3: Copy HTML
Copy the entire component block including styles

### Step 4: Paste into Page
Insert into your target HTML file

### Step 5: Customize
- Replace placeholder text with real content
- Update href links to match your site structure
- Change icon colors if needed (maintain brand colors)
- Adjust grid columns for your content (3-col → 2-col, etc.)

### Step 6: Test
- Check desktop (1280px+)
- Check tablet (768px - 1024px)
- Check mobile (<768px)

---

## 📝 Customization Guidelines

### ✅ DO:
- Use exact brand colors (#0A0F1F, #3A7DFF, #7A4BFF, #A855FF, #4FD1C5)
- Maintain spacing (padding: 6rem for sections, 2rem for cards)
- Keep typography hierarchy (H1: 3.5-4rem, H2: 2.5-3rem, Body: 1.125rem)
- Use navigation motifs (.bg-topographic, .bg-grid-overlay, .bg-route-lines)
- Include visual elements in every section

### ❌ DON'T:
- Change brand colors to off-brand values
- Use thin font weights (<600 for headings)
- Create plain, text-only sections
- Remove navigation motifs from backgrounds
- Use cartoon or playful design elements
- Reduce spacing below minimum values

---

## 🎯 Page-Specific Usage Recommendations

### Homepage
1. Primary Hero (with stats)
2. Value Proposition Cards (3 service cards)
3. 4-Pillar Framework
4. Statistics Module
5. Industry Cards (2-column)
6. Journey Process (4-step)
7. Primary CTA Block
8. Footer

### Expertise Overview Page
1. Secondary Hero
2. Section Header ("Our Expertise")
3. Service Cards Grid (16 specialties in 4x4 grid)
4. Two-Column Feature (approach/methodology)
5. Primary CTA Block
6. Footer

### Individual Expertise Page
1. Secondary Hero (specialty name)
2. Two-Column Feature (what we do)
3. Two-Column Feature (how we do it)
4. Case Study Cards (related projects)
5. Primary CTA Block
6. Footer

### Industries Page
1. Secondary Hero
2. Industry Cards Grid (6 industries in 3x2 grid)
3. Statistics Module
4. Primary CTA Block
5. Footer

### Projects Page
1. Secondary Hero
2. Case Study Cards Grid (9 projects in 3x3 grid)
3. Statistics Module
4. Primary CTA Block
5. Footer

### About Page
1. Secondary Hero
2. Two-Column Feature (story)
3. Two-Column Feature (approach)
4. Journey Process (4-step)
5. Statistics Module
6. Primary CTA Block
7. Footer

### Contact Page
1. Secondary Hero
2. Two-Column Layout (form left, info right)
3. Footer

---

## 🔧 Technical Implementation

### Required CSS Files
```html
<link rel="stylesheet" href="/brand-system.css">
```

### Component Classes Reference

**Background Patterns:**
```css
.bg-topographic    /* Contour map pattern */
.bg-grid-overlay   /* Grid coordinate pattern */
.bg-route-lines    /* Dashed route pattern */
```

**Brand Sections:**
```css
.hero-navy         /* Navy hero background */
.bg-navy           /* Navy section background */
.btn-primary-brand /* Primary CTA button */
.text-gradient-brand /* Gradient text effect */
.card-hover        /* Card hover effect */
```

### Inline Styles Used
Most styling is inline for portability. Key patterns:

**Navy Section:**
```html
<section style="background: #0A0F1F; color: white; padding: 6rem 3rem;">
```

**Gradient Background:**
```html
<div style="background: linear-gradient(135deg, #0A0F1F 0%, #3A7DFF 100%);">
```

**Card Layout:**
```html
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
```

---

## 📐 Spacing Standards

### Section Padding
- Desktop: `padding: 6rem 3rem;`
- Mobile: `padding: 3rem 1.5rem;`

### Card Padding
- Standard: `padding: 2rem;`
- Large: `padding: 2.5rem;`

### Grid Gaps
- Card grids: `gap: 2rem;`
- Content columns: `gap: 4rem;`

### Margins
- Section H2 bottom: `margin-bottom: 1.5rem;`
- Paragraph bottom: `margin-bottom: 1.5rem;`
- List item bottom: `margin-bottom: 0.75rem;`

---

## 🎨 Color Usage by Component

| Component | Background | Text | Accents |
|-----------|------------|------|---------|
| **Primary Hero** | #0A0F1F | White | #3A7DFF (stats) |
| **Secondary Hero** | Navy → Purple gradient | White | - |
| **Navbar** | #0A0F1F | White/rgba | #3A7DFF (CTA) |
| **Service Cards** | White | #0A0F1F | #3A7DFF gradients |
| **Industry Cards** | Navy → Blue gradient | White | #4FD1C5 (bullets) |
| **Case Study Cards** | White | #0A0F1F | Gradient headers |
| **Statistics** | Navy → Blue gradient | White | #3A7DFF, #A855FF |
| **4-Pillar Framework** | White | #0A0F1F | Border colors vary |
| **Journey Process** | White | #0A0F1F | Gradient badges |
| **Primary CTA** | #0A0F1F | White | White button |
| **Footer** | #0A0F1F | rgba(255,255,255,0.7) | #3A7DFF (links) |

---

## 🔍 Quality Checklist

Before using any component, verify:

- [ ] Uses brand colors (#0A0F1F, #3A7DFF, #7A4BFF, #A855FF)
- [ ] Includes navigation motif in background
- [ ] Typography follows hierarchy (bold headings, clean body)
- [ ] Spacing is generous and consulting-quality
- [ ] Has visual elements (not plain text-only)
- [ ] Buttons use gradient styling
- [ ] Links have proper hover states
- [ ] Responsive on mobile, tablet, desktop
- [ ] Card hovers work smoothly
- [ ] Content is meaningful (no lorem ipsum)

---

## 🚨 Common Mistakes to Avoid

1. **Forgetting Navigation Motifs**
   - ❌ Plain navy background
   - ✅ Navy with `.bg-topographic` or `.bg-grid-overlay`

2. **Wrong Button Styling**
   - ❌ Plain blue button
   - ✅ `.btn-primary-brand` with gradient

3. **Insufficient Spacing**
   - ❌ `padding: 2rem 1rem;`
   - ✅ `padding: 6rem 3rem;`

4. **Text-Only Sections**
   - ❌ Section with just text, no visuals
   - ✅ Section with gradient background + pattern

5. **Off-Brand Colors**
   - ❌ Using #2563EB (standard Tailwind blue)
   - ✅ Using #3A7DFF (electric blue)

---

## 📄 Files Reference

| File | Purpose |
|------|---------|
| `/app/component-library.html` | Live component showcase |
| `/app/brand-system.css` | Brand CSS (colors, patterns, utilities) |
| `/app/COMPONENT-LIBRARY-GUIDE.md` | This documentation |
| `/app/apply-brand-system.py` | Script to apply brand to existing pages |

---

## 🎓 Example Usage

### Example: Adding Service Cards to Expertise Page

1. **Open component library:**
   - Navigate to section "4. Card Components"
   - Find "Service Card (Expertise)"

2. **Copy HTML:**
```html
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
    <div class="card-hover" style="background: white; border: 2px solid #E5E7EB; border-radius: 12px; padding: 2rem;">
        <!-- Card content -->
    </div>
</div>
```

3. **Paste into `/app/expertise/index.html`:**
   - Find appropriate section
   - Paste after section header

4. **Customize:**
   - Change title: "Account-Based Marketing" → Your specialty
   - Update description
   - Change link: `/expertise/account-based-marketing/` → Your URL
   - Adjust icon color if needed

5. **Test:**
   - View page in browser
   - Check hover effect works
   - Verify responsive layout

---

## ✅ Ready to Use

All components are production-ready and can be used immediately. The library is designed to maintain brand consistency across all pages while allowing content customization.

**Next Steps:**
1. Browse `/component-library.html`
2. Copy needed components
3. Paste into target pages
4. Customize content
5. Test and verify

---

**Component Library Version:** 1.0  
**Last Updated:** 2025-11-29  
**Brand System:** GTMstack.pro "Navigate Your GTM Journey"
