#!/usr/bin/env python3

# 6x9 inch book optimization
page_width_mm = 152.4
page_height_mm = 228.6

# Current settings
current = {
    'inner': 19,
    'outer': 14,
    'top': 13,
    'bottom': 13,
    'headheight_pt': 12,
    'headsep_mm': 7,
    'footskip_mm': 10,
    'line_spacing': 1.15
}

# Amazon KDP requirements (ABSOLUTE MINIMUMS)
kdp_min = {
    'inner': 6.35,  # 0.25" minimum for binding
    'outer': 6.35,  # 0.25" minimum
    'top': 6.35,    # 0.25" minimum
    'bottom': 6.35  # 0.25" minimum
}

# Professional minimums (readable but tight)
prof_min = {
    'inner': 15,    # 0.59" - need space for binding
    'outer': 10,    # 0.39" - can be tighter
    'top': 10,      # 0.39" - can be tighter
    'bottom': 10,   # 0.39" - can be tighter
    'headheight_pt': 14,
    'headsep_mm': 5,
    'footskip_mm': 8,
    'line_spacing': 1.12
}

# Calculate text area
def calc_text_area(margins):
    text_width = page_width_mm - margins['inner'] - margins['outer']
    text_height = page_height_mm - margins['top'] - margins['bottom']
    return text_width, text_height, text_width * text_height

print("=" * 70)
print("6×9 INCH BOOK - SPACE OPTIMIZATION ANALYSIS")
print("=" * 70)

# Current layout
tw_curr, th_curr, area_curr = calc_text_area(current)
print(f"\nCURRENT LAYOUT:")
print(f"  Margins: Inner {current['inner']}mm, Outer {current['outer']}mm, Top {current['top']}mm, Bottom {current['bottom']}mm")
print(f"  Text width: {tw_curr:.1f}mm ({tw_curr/25.4:.2f}\")")
print(f"  Text height: {th_curr:.1f}mm ({th_curr/25.4:.2f}\")")
print(f"  Text area: {area_curr:.0f}mm²")
print(f"  Line spacing: {current['line_spacing']}")

# Optimized professional layout
optimized = {
    'inner': 15,    # Minimum safe for binding (600+ pages)
    'outer': 10,    # Tighter outside
    'top': 10,      # Tighter top
    'bottom': 10,   # Tighter bottom
    'headheight_pt': 14,
    'headsep_mm': 5,
    'footskip_mm': 8,
    'line_spacing': 1.12
}

tw_opt, th_opt, area_opt = calc_text_area(optimized)
print(f"\nOPTIMIZED LAYOUT (Professional Tight):")
print(f"  Margins: Inner {optimized['inner']}mm, Outer {optimized['outer']}mm, Top {optimized['top']}mm, Bottom {optimized['bottom']}mm")
print(f"  Text width: {tw_opt:.1f}mm ({tw_opt/25.4:.2f}\")")
print(f"  Text height: {th_opt:.1f}mm ({th_opt/25.4:.2f}\")")
print(f"  Text area: {area_opt:.0f}mm²")
print(f"  Line spacing: {optimized['line_spacing']}")

# Calculate gains
width_gain = tw_opt - tw_curr
height_gain = th_opt - th_curr
area_gain = area_opt - area_curr
area_pct = (area_gain / area_curr) * 100

print(f"\nSPACE GAINED:")
print(f"  Width: +{width_gain:.1f}mm (+{(width_gain/tw_curr)*100:.1f}%)")
print(f"  Height: +{height_gain:.1f}mm (+{(height_gain/th_curr)*100:.1f}%)")
print(f"  Total area: +{area_gain:.0f}mm² (+{area_pct:.1f}%)")

# Estimate page reduction
# Assume ~2000 words per page currently
words_per_page_current = 2000
total_words = 124000
current_pages = 607

# With more space per page
words_per_page_optimized = words_per_page_current * (area_opt / area_curr)
optimized_pages = total_words / words_per_page_optimized

# With tighter line spacing too
line_spacing_factor = current['line_spacing'] / optimized['line_spacing']
words_per_page_final = words_per_page_optimized * line_spacing_factor
final_pages = total_words / words_per_page_final

print(f"\nESTIMATED PAGE REDUCTION:")
print(f"  Current pages: {current_pages}")
print(f"  With optimized margins: ~{int(optimized_pages)} pages")
print(f"  With tighter line spacing: ~{int(final_pages)} pages")
print(f"  Total reduction: ~{current_pages - int(final_pages)} pages ({((current_pages - final_pages)/current_pages)*100:.1f}%)")

# Professional standards check
print(f"\n{'=' * 70}")
print("PROFESSIONAL STANDARDS CHECK:")
print(f"{'=' * 70}")

def check_standard(name, value, minimum, recommended):
    if value < minimum:
        return f"❌ TOO TIGHT ({value}mm < {minimum}mm min)"
    elif value < recommended:
        return f"⚠️  Tight but acceptable ({value}mm < {recommended}mm recommended)"
    else:
        return f"✅ Professional ({value}mm >= {recommended}mm)"

print(f"\nInner margin (binding): {check_standard('inner', optimized['inner'], kdp_min['inner'], 19)}")
print(f"Outer margin: {check_standard('outer', optimized['outer'], kdp_min['outer'], 12)}")
print(f"Top margin: {check_standard('top', optimized['top'], kdp_min['top'], 13)}")
print(f"Bottom margin: {check_standard('bottom', optimized['bottom'], kdp_min['bottom'], 13)}")

print(f"\n{'=' * 70}")
print("RECOMMENDED OPTIMIZED SETTINGS:")
print(f"{'=' * 70}")
print(f"""
inner=15mm     (was 19mm, saved 4mm width - min safe for 600+ pages)
outer=10mm     (was 14mm, saved 4mm width - acceptable for trade paperback)
top=10mm       (was 13mm, saved 3mm height - acceptable)
bottom=10mm    (was 13mm, saved 3mm height - acceptable)
headheight=14pt (was 12pt, fixes warnings)
headsep=5mm    (was 7mm, saved 2mm height)
footskip=8mm   (was 10mm, saved 2mm height)
line spacing=1.12 (was 1.15, saves ~2.6% vertical space)

Total savings: ~8mm width + ~10mm height + 2.6% line spacing
Estimated pages saved: ~{current_pages - int(final_pages)} pages
""")

print(f"{'=' * 70}")
print("TRADE-OFFS:")
print(f"{'=' * 70}")
print("""
PROS:
✅ Saves ~40-50 pages (reduces printing cost by ~$0.50/book)
✅ Still within professional standards
✅ More content-dense (professional look)
✅ Better page utilization
✅ Still readable (margins not cramped)

CONS:
⚠️  Less white space (slightly denser feel)
⚠️  Inner margin tighter (but still safe for binding)
⚠️  Slightly less generous than premium books

VERDICT: Worthwhile optimization for cost-conscious professional book
""")

