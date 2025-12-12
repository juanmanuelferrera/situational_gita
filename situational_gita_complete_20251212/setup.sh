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
