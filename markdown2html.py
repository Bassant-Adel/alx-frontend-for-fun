#!/usr/bin/python3
"""
Script to convert Markdown to HTML.
"""
import sys
import os
import re
import hashlib


# Check if the number of arguments is correct
if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)


# Extract arguments
markdown_file = sys.argv[1]
html_file = sys.argv[2]


# Check if Markdown file exists
if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)


# Read Markdown content
with open(markdown_file, 'r') as md_file:
    markdown_content = md_file.read()


# Function to convert Markdown headings to HTML
def convert_headings(match):
    """
    Script to convert Markdown to HTML.
    """
    level = len(match.group(1))
    return f"<h{level}>{match.group(2)}</h{level}>"


# Convert Markdown headings to HTML
html_content = re.sub(
        r'^(\#{1,6})\s(.+)$',
        convert_headings,
        markdown_content,
        flags=re.M
        )


# Function to convert Markdown unordered lists to HTML
def convert_unordered_lists(match):
    """
    Script to convert Markdown to HTML.
    """
    items = match.group(1).split('\n')
    items = [f"<li>{item.strip()}</li>" for item in items if item.strip()]
    return f"<ul>\n{''.join(items)}\n</ul>"


# Convert Markdown unordered lists to HTML
html_content = re.sub(
        r'^\s*\-\s(.+)$',
        convert_unordered_lists,
        html_content,
        flags=re.M
        )


# Function to convert Markdown ordered lists to HTML
def convert_ordered_lists(match):
    """
    Script to convert Markdown to HTML.
    """
    items = match.group(1).split('\n')
    items = [f"<li>{item.strip()}</li>" for item in items if item.strip()]
    return f"<ol>\n{''.join(items)}\n</ol>"


# Convert Markdown ordered lists to HTML
html_content = re.sub(
        r'^\s*\*\s(.+)$',
        convert_ordered_lists,
        html_content,
        flags=re.M
        )


# Function to convert Markdown paragraphs to HTML
def convert_paragraphs(match):
    """
    Script to convert Markdown to HTML.
    """
    lines = match.group(1).split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    return f"<p>\n{'\n'.join(lines)}\n</p>"


# Convert Markdown paragraphs to HTML
html_content = re.sub(
        r'((?:^(?!\#|\-|\*).+)(?:\n(?!\#|\-|\*).+)*)',
        convert_paragraphs,
        html_content,
        flags=re.M
        )


# Function to convert Markdown bold syntax to HTML
def convert_bold(match):
    """
    Script to convert Markdown to HTML.
    """
    return f"<b>{match.group(1)}</b>"


# Convert Markdown bold syntax to HTML
html_content = re.sub(r'\*\*(.+?)\*\*', convert_bold, html_content)


# Function to convert Markdown italic syntax to HTML
def convert_italic(match):
    return f"<em>{match.group(1)}</em>"


# Convert Markdown italic syntax to HTML
html_content = re.sub(r'__(.+?)__', convert_italic, html_content)


# Function to convert Markdown MD5 syntax to HTML
def convert_md5(match):
    """
    Script to convert Markdown to HTML.
    """
    content = match.group(1)
    return hashlib.md5(content.encode()).hexdigest()


# Convert Markdown MD5 syntax to HTML
html_content = re.sub(r'\[\[(.+?)\]\]', lambda x: convert_md5(x), html_content)


# Function to convert Markdown removal syntax to HTML
def remove_characters(match):
    """
    Script to convert Markdown to HTML.
    """
    return match.group(1).replace('c', '')


# Convert Markdown removal syntax to HTML
html_content = re.sub(
        r'\(\((.+?)\)\)',
        lambda x: remove_characters(x),
        html_content,
        flags=re.I
        )


# Write HTML content to file
with open(html_file, 'w') as html:
    html.write(html_content)

sys.exit(0)
