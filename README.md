# sublime-bottom-margin

Sublime Text 3 plugin that keeps some space between your cursor and the bottom of the view

## Manual Installation

1. Download or clone this repository to a directory `sublime-bottom-margin` in the Sublime Text Packages directory. In Sublime Text 3, that folder is called `Data/Packages`.
2. Restart Sublime Text to complete installation.

## Configuration

To manage the settings of this plugin:

1. Open user settings by clicking `Preferences`, then `Settings - User`.
2. Add the `bottom_margin_size` and `bottom_margin_off` options.

### Settings

`bottom_margin_size`

- set to a positive integer to control number of lines in the margin (Example: `"bottom_margin_size" : 5`)
- set to 0 or a negative integer to turn off bottom margin (ie, default Sublime behavior)
- default is 3

`bottom_margin_off`

- toggled by the keybinding (see below)
- set to true to turn off bottom margin and get back default Sublime behavior
- set to false to turn on bottom margin


## Key Bindings

The keybinding `alt+shift+m` will toggle the bottom margin on and off. This sequence can be changed in the file `sublime-bottom-margin/Default (Windows).sublime-keymap`

## Coming Soon

- Installation using Package Control
- Keybinding files for OSX and Linux
- Plugin-specific settings file
- Toggling on/off using the Sublime Command Palette
- Ability to set the bottom margin to be half of the window size
- "Focus mode": dim all but several lines around the current line (if possible)

## License

This project is released under the terms of the [MIT license](http://en.wikipedia.org/wiki/MIT_License).