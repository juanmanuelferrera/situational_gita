#!/bin/bash

# This script exports org-mode to LaTeX by extracting headers and content

INPUT="situational_gita_book.org"
OUTPUT="situational_gita_book.tex"

echo "Exporting $INPUT to $OUTPUT..."

# Start building the TEX file
{
    echo "% Generated from $INPUT"
    echo "\\documentclass[12pt,twoside]{book}"
    echo ""
    
    # Extract all LATEX_HEADER lines and convert them
    grep "^#+LATEX_HEADER:" "$INPUT" | sed 's/^#+LATEX_HEADER: //' 
    
    echo ""
    echo "\\begin{document}"
    echo ""
    
    # Now we need to extract the content between #+BEGIN_EXPORT latex and #+END_EXPORT
    # and also regular org content
    
    awk '
    BEGIN { in_export = 0; in_org = 1; }
    
    /^#+BEGIN_EXPORT latex/ { in_export = 1; in_org = 0; next }
    /^#+END_EXPORT/ { in_export = 0; in_org = 1; next }
    
    # Skip org-mode directives
    /^#+TITLE:/ { next }
    /^#+SUBTITLE:/ { next }
    /^#+Author:/ { next }
    /^#+DATE:/ { next }
    /^#+LATEX_CLASS:/ { next }
    /^#+LATEX_CLASS_OPTIONS:/ { next }
    /^#+LATEX_COMPILER:/ { next }
    /^#+OPTIONS:/ { next }
    /^#+LATEX_HEADER:/ { next }
    /^# / { next }  # Skip org comments
    
    # Print LaTeX export blocks directly
    in_export == 1 { print; next }
    
    # Convert org-mode content to LaTeX
    in_org == 1 && NF > 0 {
        line = $0
        
        # Convert bold: *text* -> \textbf{text}
        gsub(/\*([^*]+)\*/, "\\textbf{\\1}", line)
        
        # Convert italic: /text/ -> \emph{text}  
        gsub(/\/([^\/]+)\//, "\\emph{\\1}", line)
        
        # Convert special characters
        gsub(/—/, "---", line)
        gsub(/"/, "``", line)
        gsub(/"/, "''\'\'", line)
        
        print line
        next
    }
    
    # Print blank lines
    NF == 0 && in_org == 1 { print ""; next }
    
    ' "$INPUT"
    
    echo ""
    echo "\\end{document}"
    
} > "$OUTPUT"

echo "Export complete: $OUTPUT"
