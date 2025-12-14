#!/bin/bash

# Get all verse references with context
grep -B 2 "Bhagavad-gītā [0-9]\+\.[0-9]\+" situational_gita_book.org | \
  grep -E "(^% Chapter [0-9]+:|Bhagavad-gītā [0-9]+\.[0-9]+)" | \
  awk '
    /^% Chapter/ { chapter = $0; gsub(/^% Chapter /, "", chapter); gsub(/:.*/, "", chapter) }
    /Bhagavad-gītā/ { 
      match($0, /Bhagavad-gītā ([0-9]+\.[0-9]+)/, arr)
      if (arr[1] != "") {
        verses[arr[1]] = verses[arr[1]] (verses[arr[1]] ? ", " : "") "Ch. " chapter
      }
    }
    END {
      n = asorti(verses, sorted_verses)
      for (i = 1; i <= n; i++) {
        verse = sorted_verses[i]
        split(verse, parts, ".")
        print parts[1] "." parts[2] " | " verses[verse]
      }
    }
  ' | sort -t. -k1n -k2n
