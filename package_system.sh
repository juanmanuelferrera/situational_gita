#!/bin/bash
# Package the complete Situational Gita Article Generator system

echo "======================================================================"
echo "  Packaging Situational Gita Article Generator"
echo "======================================================================"
echo ""

# Create package directory
PACKAGE_NAME="situational_gita_complete_$(date +%Y%m%d)"
mkdir -p "$PACKAGE_NAME"

echo "Creating package: $PACKAGE_NAME"
echo ""

# Copy essential files
echo "Copying files..."

# Documentation
cp QUICK_START.md "$PACKAGE_NAME/" 2>/dev/null
cp COMPLETE_GUIDE.md "$PACKAGE_NAME/" 2>/dev/null
cp README.md "$PACKAGE_NAME/" 2>/dev/null
cp WRITING_STYLE_GUIDE.md "$PACKAGE_NAME/" 2>/dev/null

# Source book
cp situational_gita.txt "$PACKAGE_NAME/" 2>/dev/null
cp situational_gita.pdf "$PACKAGE_NAME/" 2>/dev/null

# Python scripts
cp extract_themes.py "$PACKAGE_NAME/" 2>/dev/null
cp narrative_strategies.py "$PACKAGE_NAME/" 2>/dev/null
cp article_generator.py "$PACKAGE_NAME/" 2>/dev/null
cp gita_ui.py "$PACKAGE_NAME/" 2>/dev/null

# Make scripts executable
chmod +x "$PACKAGE_NAME"/*.py

# Create articles directory
mkdir -p "$PACKAGE_NAME/articles"

# Copy extracted data if it exists
if [ -f "comprehensive_gita_data.json" ]; then
    echo "  ✓ Including pre-extracted content data"
    cp comprehensive_gita_data.json "$PACKAGE_NAME/"
fi

# Create requirements.txt
echo "Creating requirements.txt..."
cat > "$PACKAGE_NAME/requirements.txt" << 'EOF'
anthropic>=0.18.0
EOF

# Create setup script
echo "Creating setup script..."
cat > "$PACKAGE_NAME/setup.sh" << 'EOF'
#!/bin/bash
# Setup script for Situational Gita Article Generator

echo "======================================================================"
echo "  Situational Gita Article Generator - Setup"
echo "======================================================================"
echo ""

# Check Python
echo "Checking Python..."
if command -v python3 &> /dev/null; then
    echo "  ✓ Python 3 found: $(python3 --version)"
else
    echo "  ✗ Python 3 not found. Please install Python 3.7+"
    exit 1
fi

# Install dependencies (optional - only needed for standalone mode)
echo ""
echo "Install dependencies? (only needed if NOT using Claude Code)"
read -p "Install anthropic package? (y/n): " install_deps

if [ "$install_deps" = "y" ]; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    echo "  ✓ Dependencies installed"
fi

# Extract content
echo ""
echo "Extract content from book? (recommended, takes 2-3 minutes)"
read -p "Extract now? (y/n): " extract_now

if [ "$extract_now" = "y" ]; then
    echo "Extracting content..."
    python3 extract_themes.py
    echo "  ✓ Content extracted"
fi

# API key setup
echo ""
echo "======================================================================"
echo "  API Key Setup (Optional - only for standalone mode)"
echo "======================================================================"
echo ""
echo "If using Claude Code: Skip this (press n)"
echo "If using standalone scripts: Set your Anthropic API key"
echo ""
read -p "Set API key now? (y/n): " set_key

if [ "$set_key" = "y" ]; then
    read -p "Enter your Anthropic API key: " api_key
    echo ""
    echo "Add this line to your ~/.zshrc or ~/.bashrc:"
    echo "  export ANTHROPIC_API_KEY='$api_key'"
    echo ""
    echo "Or run this command:"
    echo "  echo \"export ANTHROPIC_API_KEY='$api_key'\" >> ~/.zshrc"
    echo "  source ~/.zshrc"
fi

echo ""
echo "======================================================================"
echo "  Setup Complete!"
echo "======================================================================"
echo ""
echo "Next steps:"
echo ""
echo "Option 1 - Using Claude Code (Recommended):"
echo "  1. Open this folder in Claude Code"
echo "  2. Say: 'Generate an article about Anger'"
echo ""
echo "Option 2 - Using standalone scripts:"
echo "  1. Run: python3 gita_ui.py"
echo "  2. Follow the interactive menu"
echo ""
echo "Read QUICK_START.md for detailed instructions"
echo ""
EOF

chmod +x "$PACKAGE_NAME/setup.sh"

# Create README for package
cat > "$PACKAGE_NAME/START_HERE.txt" << 'EOF'
================================================================================
  SITUATIONAL GITA ARTICLE GENERATOR
  Ancient Wisdom for Modern Life
================================================================================

Thank you for downloading this system!

QUICK START (2 steps):
======================

1. Run setup:
   ./setup.sh

2. Choose your method:

   METHOD A - Claude Code (Easiest, Recommended):
   - Open this folder in Claude Code
   - Say: "Generate an article about Anger"

   METHOD B - Standalone Scripts:
   - Run: python3 gita_ui.py
   - Follow the interactive menu

WHAT'S INCLUDED:
================

Documentation:
  - START_HERE.txt .............. This file
  - QUICK_START.md .............. Fast start guide
  - COMPLETE_GUIDE.md ........... Comprehensive documentation
  - README.md ................... System overview
  - WRITING_STYLE_GUIDE.md ...... Style guidelines

Source:
  - situational_gita.txt ........ Converted book text
  - situational_gita.pdf ........ Original PDF (if included)

Scripts:
  - setup.sh .................... Run this first!
  - extract_themes.py ........... Extract book content
  - narrative_strategies.py ..... 12 unique strategies
  - article_generator.py ........ Main generator
  - gita_ui.py .................. Interactive UI

Data:
  - comprehensive_gita_data.json  Pre-extracted content (if included)
  - articles/ ................... Generated articles go here

FEATURES:
=========

✓ 60 life themes (Anger, Depression, Fear, etc.)
✓ 12 unique narrative strategies
✓ Intelligent theme-to-strategy matching
✓ AI-powered article generation
✓ Light of Dharma style compliance
✓ Hugo-ready markdown output

TWO WAYS TO USE:
================

1. CLAUDE CODE (Recommended):
   - No API key needed
   - No costs
   - Conversational interface
   - Same quality

   Usage: Just talk to Claude!
   "Generate an article about Loneliness"

2. STANDALONE SCRIPTS:
   - Requires Anthropic API key (costs money)
   - Good for automation
   - Batch generation of 100+ articles

   Usage: python3 gita_ui.py

SUPPORT:
========

Read the documentation files:
  - QUICK_START.md for fastest path
  - COMPLETE_GUIDE.md for everything

REQUIREMENTS:
=============

- Python 3.7+
- anthropic package (only for standalone mode)
- Anthropic API key (only for standalone mode)
- Claude Code (optional, but recommended)

GET STARTED:
============

Run: ./setup.sh

Then read: QUICK_START.md

Questions? Check COMPLETE_GUIDE.md

================================================================================
EOF

# Create archive
echo ""
echo "Creating archive..."
tar -czf "${PACKAGE_NAME}.tar.gz" "$PACKAGE_NAME"
zip -r "${PACKAGE_NAME}.zip" "$PACKAGE_NAME" > /dev/null 2>&1

# Summary
echo ""
echo "======================================================================"
echo "  Package Created Successfully!"
echo "======================================================================"
echo ""
echo "Package contents:"
echo "  Directory: $PACKAGE_NAME/"
echo "  Archive:   ${PACKAGE_NAME}.tar.gz"
echo "  Archive:   ${PACKAGE_NAME}.zip"
echo ""
echo "Package includes:"
ls -1 "$PACKAGE_NAME" | while read file; do
    echo "  ✓ $file"
done
echo ""
echo "To share:"
echo "  1. Send the .zip or .tar.gz file"
echo "  2. Recipient runs: ./setup.sh"
echo "  3. Ready to generate articles!"
echo ""
echo "======================================================================"
