# Sublime Bottom Margin

This is a Sublime Text 3 plugin that gives the editor a bottom margin, keeping some space between your cursor and the bottom of the view.

I made this plugin because I was too lazy to look all the way at the bottom of the window when I was taking notes in Sublime. This plugin shifts the view up as you are typing so that there is always a given amount of space between your cursor and the bottom of the window while you type.


## Manual Installation

1. Download or clone this repository to a directory `BottomMargin` in the Sublime Text Packages directory.
    * In Sublime Text 3, the Packages directory is called `Data/Packages`.
    * You can find this directory by clicking `Preferences > Browse Packages...` in Sublime.
2. Restart Sublime Text to complete installation.
3. In order for this plugin to work properly, the `scroll_past_end` setting in `Preferences > Settings - User` must be set to `true`.


## Usage

Plugin properties (margin size, on/off, etc.) can be changed either in the `Preferences > Package Settings > Bottom Margin` menu or by using the following key bindings and commands.

### Commands

| Key Binding   | Command Palette |
|:--------------|:----------------|
| `alt+shift+m` | Bottom Margin: Toggle On/Off        |
| `alt+shift+j` | Bottom Margin: Decrease Margin Size |
| `alt+shift+k` | Bottom Margin: Increase Margin Size |
| `alt+shift+t` | Bottom Margin: Toggle Typewriter Mode |

The Command Palette is opened using the key binding `ctrl+shift+p` (Windows) or `cmd+shift+p` (OSX).


## Configuration

All of the settings below can be manipulated using key bindings and the Command Palette.

To manually manage the settings of this plugin:

1. Open plugin settings by clicking `Preferences > Package Settings > Bottom Margin > Settings`.
2. If the file is blank, copy and paste in the default settings:

        {
            "bottom_margin_on": true,
            "bottom_margin_size": 3,
            "typewriter_mode": false
        }

3. The plugin's key bindings can be edited by going to `Preferences > Package Settings > Bottom Margin > Key Bindings`.

### Settings

`bottom_margin_size`

- set to a positive integer to control number of lines in the margin (Example: `"bottom_margin_size" : 5`)
- set to 0 or a negative integer to turn off bottom margin (ie, default Sublime behavior)
- if this setting is not present, default is 3

`bottom_margin_on`

- set to `true` to enable bottom margin
- set to `false` to return to default Sublime behavior
- if this setting is not present, bottom margin is enabled by default

`typewriter_mode`

- set to `true` to enable Typewriter Mode, set to `false` to disable
- if the setting is not present, Typewriter Mode is disabled by default
- Note: `bottom_margin_on` setting must be set to `true` (or not present) to enable Typewriter Mode


## Coming Soon

- Screenshots
- Installation using Package Control
- Better behavior for files with wrapped lines
- Focus mode: dim all but several lines around the current line (if possible)
- Sublime Text 2 version
- OSX testing


## License

This project is released under the terms of the [MIT license](http://en.wikipedia.org/wiki/MIT_License).
