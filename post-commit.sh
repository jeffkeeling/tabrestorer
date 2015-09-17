#!/bin/bash
git checkout gh-pages
git checkout master -- updatemanifest.plist tabrestorer.safariextz
git commit -m "update extension and manifest from master" --no-verify
git push
git checkout master