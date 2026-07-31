#!/bin/bash
set -e

echo "📦 Bundling React app to single HTML artifact..."

# Check if we're in a project directory
if [ ! -f "package.json" ]; then
  echo "❌ Error: No package.json found. Run this script from your project root."
  exit 1
fi

# Check if index.html exists
if [ ! -f "index.html" ]; then
  echo "❌ Error: No index.html found in project root."
  echo "   This script requires an index.html entry point."
  exit 1
fi

# Install bundling dependencies
echo "📦 Installing bundling dependencies..."
pnpm add -D parcel @parcel/config-default parcel-resolver-tspaths html-inline

# Create Parcel config with tspaths resolver
if [ ! -f ".parcelrc" ]; then
  echo "🔧 Creating Parcel configuration with path alias support..."
  cat > .parcelrc << 'EOF'
{
  "extends": "@parcel/config-default",
  "resolvers": ["parcel-resolver-tspaths", "..."]
}
EOF
fi

# Clean previous build
echo "🧹 Cleaning previous build..."
rm -rf dist bundle.html

# Vite serves everything in public/ from the site root, so index.html refers to
# those assets as "/favicon.svg". Parcel resolves a leading "/" against the
# project root instead, and fails on files that only exist under public/.
# Build from a temporary entry point with those references rewritten.
BUILD_ENTRY="index.html"
if [ -d "public" ]; then
  BUILD_ENTRY="index.parcel.html"
  trap 'rm -f "$BUILD_ENTRY"' EXIT
  cp index.html "$BUILD_ENTRY"
  for asset in $(grep -oE '(href|src)="/[^"]+"' index.html \
                 | sed -E 's/.*="\/([^"]+)"/\1/' | sort -u); do
    if [ -f "public/$asset" ]; then
      echo "🔗 Rewriting /$asset -> ./public/$asset for Parcel"
      sed -i "s|\"/$asset\"|\"./public/$asset\"|g" "$BUILD_ENTRY"
    fi
  done
fi

# Build with Parcel
echo "🔨 Building with Parcel..."
pnpm exec parcel build "$BUILD_ENTRY" --dist-dir dist --no-source-maps

# Inline everything into single HTML
echo "🎯 Inlining all assets into single HTML file..."
pnpm exec html-inline "dist/$BUILD_ENTRY" > bundle.html

# Get file size
FILE_SIZE=$(du -h bundle.html | cut -f1)

echo ""
echo "✅ Bundle complete!"
echo "📄 Output: bundle.html ($FILE_SIZE)"
echo ""
echo "You can now use this single HTML file as an artifact in Claude conversations."
echo "To test locally: open bundle.html in your browser"