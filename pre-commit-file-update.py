#!/usr/bin/env python

import plistlib
import fileinput
import sys

sys.stdin = open('/dev/tty')
user_continue = raw_input('Update files for new version?? (y/n): ')

if user_continue == 'y':

    # get version number
    with open("tabrestorer.safariextension/Info.plist", "r+") as info_file:
        info_root = plistlib.readPlist(info_file)
        CFBundleShortVersionString_version_number = info_root['CFBundleShortVersionString']
        CFBundleVersion_version_number = info_root['CFBundleVersion']

    # update the update manifest with new version number
    with open("updatemanifest.plist", "r+") as manifest_file:
        manifest_root = plistlib.readPlist(manifest_file)
        manifest_root['Extension Updates'][0]['CFBundleShortVersionString'] = CFBundleShortVersionString_version_number
        manifest_root['Extension Updates'][0]['CFBundleVersion'] = CFBundleVersion_version_number
        manifest_file.seek(0)
        manifest_file.truncate()
        plistlib.writePlist(manifest_root, manifest_file)

    # update README file
    message_prompt = 'Your message for version ' + CFBundleVersion_version_number + ': '
    version_message = raw_input(message_prompt)
    for line in fileinput.input('README.md', inplace=1):
        if line.startswith('## Version History'):
            print line
            print '### ', CFBundleVersion_version_number
            print '- ', version_message
        else:
            sys.stdout.write(line)