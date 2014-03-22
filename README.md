# Sublime Bottom Margin

This is a Sublime Text 3 plugin that gives the editor a bottom margin, keeping some space between your cursor and the bottom of the view.

I made this plugin because I was too lazy to look all the way at the bottom of the window when I was taking notes in Sublime. This plugin shifts the view up as you are typing so that there is always a given amount of space between your cursor and the bottom of the window while you type.


## Manual Installation

1. Download or clone this repository to a directory `BottomMargin` in the Sublime Text Packages directory.
    * In Sublime Text 3, the Packages directory is called `Data/Packages`.
    * You can find this directory by clicking `Preferences > Browse Packages...` in Sublime.
2. Restart Sublime Text to complete installation.


## Usage

Plugin properties (margin size, on/off) can be changed in the `Preferences > Package Settings > Bottom Margin` menu.

### Commands

| Key Binding   | Command Palette |
|:--------------|:----------------|
| `alt+shift+m` | Bottom Margin: Toggle On/Off        |
| `alt+shift+j` | Bottom Margin: Decrease Margin Size |
| `alt+shift+k` | Bottom Margin: Increase Margin Size |

The Command Palette is opened using the key binding `ctrl+shift+p` (Windows) or `cmd+shift+p` (OSX).


## Configuration

To manually manage the settings of this plugin:

1. Open plugin settings by clicking `Preferences > Package Settings > Bottom Margin > Settings`.
2. If the file is blank, copy and paste in the default settings:

        {
            "bottom_margin_off": false,
            "bottom_margin_size": 3
        }

3. The plugin's key bindings can be edited by going to `Preferences > Package Settings > Bottom Margin > Key Bindings`.

### Settings

`bottom_margin_size`

- set to a positive integer to control number of lines in the margin (Example: `"bottom_margin_size" : 5`)
- set to 0 or a negative integer to turn off bottom margin (ie, default Sublime behavior)
- if this setting is not present, default is 3

`bottom_margin_off`

- toggled by the key binding (see below)
- set to `true` to return to default Sublime behavior
- set to `false` to enable bottom margin
- if this setting is not present, bottom margin is enabled by default


## Coming Soon

- Screenshots
- Installation using Package Control
- Typewriter mode: set the bottom margin to be half of the window size
- Focus mode: dim all but several lines around the current line (if possible)
- Sublime Text 2 version


## License

This project is released under the terms of the [MIT license](http://en.wikipedia.org/wiki/MIT_License).
