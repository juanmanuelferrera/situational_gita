#!/usr/bin/env python3

# Assumptions for a 607-page book
total_pages = 607
avg_paragraphs_per_page = 12  # Conservative estimate

# Current style: Indented paragraphs
indent_vertical_cost = 0  # No extra vertical space
indent_horizontal_cost = 1.5  # 1.5em indent (doesn't affect page count)

# Alternative style: Vertical spacing
parskip_vertical_cost = 4  # 4pt between paragraphs
parskip_horizontal_cost = 0  # No indent

# Calculate total vertical space added
total_paragraphs = total_pages * avg_paragraphs_per_page
vertical_space_added_pt = total_paragraphs * parskip_vertical_cost

# Convert to pages (assuming ~700pt per page in 6x9 format)
points_per_page = 700  # Approximate usable height in points
extra_pages = vertical_space_added_pt / points_per_page

print("=" * 60)
print("PARAGRAPH SPACING ANALYSIS")
print("=" * 60)
print(f"\nBook Statistics:")
print(f"  Current pages: {total_pages}")
print(f"  Estimated paragraphs/page: {avg_paragraphs_per_page}")
print(f"  Total paragraphs in book: {total_paragraphs:,}")
print(f"\nStyle 1: INDENTED PARAGRAPHS (Current)")
print(f"  Vertical space per paragraph: 0pt")
print(f"  Total extra vertical space: 0pt")
print(f"  Extra pages needed: 0")
print(f"  TOTAL PAGES: {total_pages}")
print(f"\nStyle 2: VERTICAL SPACING")
print(f"  Vertical space per paragraph: {parskip_vertical_cost}pt")
print(f"  Total extra vertical space: {vertical_space_added_pt:,.0f}pt")
print(f"  Extra pages needed: {extra_pages:.1f}")
print(f"  TOTAL PAGES: {total_pages + int(extra_pages)}")
print(f"\n{'=' * 60}")
print(f"SPACE SAVED WITH INDENTATION: ~{int(extra_pages)} pages")
print(f"Percentage saved: {(extra_pages/total_pages)*100:.1f}%")
print(f"{'=' * 60}")

# Additional analysis
print(f"\nPRACTICAL IMPACT:")
print(f"  - Printing cost: ~${int(extra_pages) * 0.015:.2f} more per book")
print(f"  - Weight: ~{int(extra_pages) * 2.5:.0f}g heavier")
print(f"  - Thickness: ~{int(extra_pages) * 0.1:.1f}mm thicker")

print(f"\nPROFESSIONAL STANDARDS:")
print(f"  ✓ Indented paragraphs = Industry standard for books")
print(f"  ✗ Vertical spacing = More common in web/digital")
print(f"  ✓ Current choice (indent) = Correct for print")
