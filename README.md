# Tab Restorer
Tab Restorer is a Safari extension that provides a button in the Safari toolbar with the 5 most recently closed tabs allowing you to quickly restore them upon clicking each one.

![Screenshot of Tab Restorer](https://raw.githubusercontent.com/jeffkeeling/tabrestorer/master/screenshot.jpg)

## Installation
1. Download the extension [here](http://jeffkeeling.github.io/tabrestorer/tabrestorer.safariextz)
2. Double-click the downloaded tabrestorer.safariextz file

## Usage
When you click the Tab Restorer button, you will see the 5 most recently closed tabs with the last closed tab at the top. Upon clicking one these links, it will open to the right of your currently open tabs.

### Optional Usage
If you open so many tabs that they overflow, it can be difficult to know if you really opened another new tab. In the settings for this extension, you can turn on a badge alert to flash when you open a new overflowed tab.
![Screenshot of new tab overflow alert](https://raw.githubusercontent.com/jeffkeeling/tabrestorer/master/screenshot2.jpg)

### Hooks
The included hooks will update the update manifest and README to account for new versions of the extension as well as provide a canonical link to the extension on the gh-pages branch.

Symlink the hooks like so:

```
ln -s ../../pre-commit.sh .git/hooks/pre-commit
ln -s ../../pre-commit-file-update.py .git/hooks/pre-commit-file-update.py
ln -s ../../post-commit.sh .git/hooks/post-commit
```

The gh-pages page fetches the most up-to-date README data from the Master branch using the steps outline in [GithubDocSync](https://github.com/bradrhodes/GithubDocSync)

## Version History

### 1.5
 - Created settings menu for new tab notification

### 1.4
 - Added open tab notification to toolbar button

## Author
Jeff Keeling

http://jeffkeeling.me