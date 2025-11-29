#!/usr/bin/env python3
"""
Apply GTMstack.pro Brand System to all HTML files
Navigate Your GTM Journey Theme
"""

import os
import glob
import re

def apply_brand_system(html_content):
    """Apply brand system transformations to HTML content"""
    
    # Add custom brand CSS if not already present
    if '/brand-system.css' not in html_content:
        css_injection = '<link rel="stylesheet" href="/brand-system.css"/>'
        html_content = html_content.replace('</head>', f'{css_injection}</head>')
    
    # Define all brand system replacements
    replacements = {
        # === HERO SECTIONS ===
        'class="relative bg-gradient-to-br from-blue-50 via-white to-orange-50 overflow-hidden"': 
        'class="relative hero-navy overflow-hidden bg-topographic"',
        
        # === TYPOGRAPHY (Hero Headings) ===
        'class="text-5xl md:text-6xl lg:text-7xl font-bold tracking-tight text-slate-900 leading-tight"':
        'class="text-5xl md:text-6xl lg:text-7xl font-bold tracking-tight text-white leading-tight"',
        
        'class="text-4xl md:text-5xl font-bold text-slate-900 mb-4"':
        'class="text-4xl md:text-5xl font-bold text-white mb-4"',
        
        # === BODY TEXT ===
        'class="text-xl text-slate-600 leading-relaxed max-w-2xl"':
        'class="text-xl text-white/90 leading-relaxed max-w-2xl"',
        
        'class="text-xl text-slate-600 max-w-3xl mx-auto"':
        'class="text-xl text-white/90 max-w-3xl mx-auto"',
        
        # === GRADIENT TEXT ===
        'class="bg-gradient-to-r from-blue-600 via-purple-600 to-orange-600 bg-clip-text text-transparent"':
        'class="text-gradient-brand"',
        
        'class="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent"':
        'class="text-gradient-brand"',
        
        'class="bg-gradient-to-r from-orange-600 to-purple-600 bg-clip-text text-transparent"':
        'class="text-gradient-brand"',
        
        # === BADGES / TAGS ===
        'class="inline-flex items-center gap-2 rounded-full bg-blue-100 px-4 py-2 text-sm font-semibold text-blue-700 shadow-sm"':
        'class="inline-flex items-center gap-2 rounded-full bg-white/20 backdrop-blur px-4 py-2 text-sm font-semibold text-white shadow-sm"',
        
        'class="bg-blue-600 text-white px-4 py-2 rounded-full text-sm font-semibold"':
        'class="bg-white/20 backdrop-blur text-white px-4 py-2 rounded-full text-sm font-semibold border border-white/30"',
        
        # === STATISTICS / METRICS ===
        'class="text-3xl font-bold text-blue-600"':
        'class="text-3xl font-bold text-electric-blue"',
        
        'class="text-3xl font-bold text-orange-600"':
        'class="text-3xl font-bold text-electric-blue"',
        
        'class="text-3xl font-bold text-purple-600"':
        'class="text-3xl font-bold text-electric-purple"',
        
        'class="text-sm text-slate-600 mt-1"':
        'class="text-sm text-white/80 mt-1"',
        
        # === BUTTONS (Update gradients) ===
        'class="inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg:not([class*=&#x27;size-&#x27;])]:size-4 shrink-0 [&amp;_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive bg-primary text-primary-foreground hover:bg-primary/90 h-10 rounded-md has-[&gt;svg]:px-4 text-lg px-8 py-6 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 shadow-lg hover:shadow-xl btn-hover"':
        'class="inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg:not([class*=&#x27;size-&#x27;])]:size-4 shrink-0 [&amp;_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive bg-primary text-primary-foreground hover:bg-primary/90 h-10 rounded-md has-[&gt;svg]:px-4 text-lg px-8 py-6 btn-primary-brand shadow-lg hover:shadow-xl btn-hover"',
        
        'bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700':
        'btn-primary-brand',
        
        # === DARK SECTIONS ===
        'class="section-spacing bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 text-white"':
        'class="section-spacing bg-navy text-white bg-topographic"',
        
        'class="section-spacing bg-gradient-to-r from-blue-600 via-purple-600 to-orange-600 text-white relative overflow-hidden"':
        'class="section-spacing hero-navy text-white relative overflow-hidden bg-route-lines"',
        
        # === FOOTER ===
        'class="border-t border-slate-200 py-12 bg-slate-50"':
        'class="border-t border-slate-200 py-12 bg-navy"',
        
        'class="font-bold text-xl mb-4 text-slate-900"':
        'class="font-bold text-xl mb-4 text-white"',
        
        'class="font-semibold mb-4 text-slate-900"':
        'class="font-semibold mb-4 text-white"',
        
        'class="text-sm text-slate-600"':
        'class="text-sm text-white/70"',
        
        'class="text-slate-600 hover:text-blue-600 transition-colors"':
        'class="text-white/70 hover:text-electric-blue transition-colors"',
        
        'class="border-t border-slate-200 pt-8 text-center text-sm text-slate-500"':
        'class="border-t border-white/10 pt-8 text-center text-sm text-white/50"',
        
        # === SECTION HEADINGS ON DARK BACKGROUNDS ===
        'class="text-4xl md:text-5xl font-bold mb-4"':
        'class="text-4xl md:text-5xl font-bold mb-4 text-white"',
        
        'class="text-xl text-blue-100 max-w-3xl mx-auto"':
        'class="text-xl text-white/90 max-w-3xl mx-auto"',
        
        # === GRID OVERLAYS (Add to existing patterns) ===
        'class="absolute inset-0 bg-grid-white/[0.05] bg-[size:32px_32px]"':
        'class="absolute inset-0 bg-grid-overlay"',
        
        'class="absolute inset-0 bg-grid-slate-900/[0.04] bg-[size:32px_32px]"':
        'class="absolute inset-0 bg-grid-overlay"',
    }
    
    # Apply all replacements
    for old, new in replacements.items():
        html_content = html_content.replace(old, new)
    
    return html_content

def process_html_file(filepath):
    """Process a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply brand system
        updated_content = apply_brand_system(content)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True, filepath
    except Exception as e:
        return False, f"{filepath}: {str(e)}"

def main():
    """Main execution"""
    print("🎨 Applying GTMstack.pro Brand System...")
    print("=" * 60)
    
    # Find all HTML files
    html_files = []
    html_files.append('index.html')  # Root level
    html_files.append('404.html')
    
    # Find HTML in subdirectories
    for pattern in ['*/index.html', '*/*/index.html']:
        html_files.extend(glob.glob(pattern))
    
    success_count = 0
    error_count = 0
    
    for html_file in html_files:
        if not os.path.exists(html_file):
            continue
            
        success, result = process_html_file(html_file)
        
        if success:
            success_count += 1
            print(f"✅ {result}")
        else:
            error_count += 1
            print(f"❌ {result}")
    
    print("=" * 60)
    print(f"✅ Successfully updated: {success_count} files")
    if error_count > 0:
        print(f"❌ Errors: {error_count} files")
    print("\n🎉 Brand system applied successfully!")

if __name__ == "__main__":
    main()
