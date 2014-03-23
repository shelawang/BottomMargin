import sublime, sublime_plugin

MARGIN_SIZE_SETTING = 'bottom_margin_size'
MARGIN_ON_SETTING = 'bottom_margin_on'
TYPEWRITER_SETTING = 'typewriter_mode'

class BottomOfViewListener(sublime_plugin.EventListener):
    def on_modified(self, view):
        view.run_command('reposition_view')


class RepositionViewCommand(sublime_plugin.TextCommand):
    """
    A TextCommand that runs whenever a view is modified - ie, text is entered
    or removed.

    If settings allow for it, then this command will reposition the view so that
    the cursor will always be a certain offset from the bottom of the window
    while the user is typing.
    """
    def run(self, edit):
        # get the necessary settings
        sets = sublime.load_settings('BottomMargin.sublime-settings')

        # if the settings don't exist, create them (for user convenience)
        settings_changed = False
        if not sets.has(MARGIN_SIZE_SETTING):
            sets.set(MARGIN_SIZE_SETTING, 3)
            settings_changed = True
        if not sets.has(MARGIN_ON_SETTING):
            sets.set(MARGIN_ON_SETTING, True)
            settings_changed = True
        if not sets.has(TYPEWRITER_SETTING):
            sets.set(TYPEWRITER_SETTING, False)
            settings_changed = True
        if settings_changed:
            sublime.save_settings('BottomMargin.sublime-settings')

        margin_size = sets.get(MARGIN_SIZE_SETTING)
        margin_on = sets.get(MARGIN_ON_SETTING)
        typewriter_mode = sets.get(TYPEWRITER_SETTING)

        # check if settings exist and allow repositioning
        if type(margin_on)==bool and not margin_on:
            return
        if not typewriter_mode:
            if type(margin_size)==float:
                margin_size = int(margin_size)
            if not type(margin_size)==int:
                margin_size = 3
            elif margin_size <= 0:
                return
 
        # get the number of lines visible in the view
        line_height = self.view.line_height()
        viewport_height = self.view.viewport_extent()[1]
        num_lines_in_view = int(viewport_height/line_height)

        # get the line number that the cursor is on
        selection = self.view.sel()
        end_of_sel = selection[len(selection)-1].end()
        cursor_line_num = self.view.rowcol(end_of_sel)[0]+1

        # get number of lines from cursor to top of view
        viewport_y_pos = self.view.viewport_position()[1]
        num_lines_out_of_view = int(viewport_y_pos/line_height)
        cursor_actual_pos = cursor_line_num - num_lines_out_of_view

        move_needed = False
        if typewriter_mode:
            # reposition view to keep cursor at center
            center_line = int(viewport_height/2/line_height)
            if cursor_actual_pos != center_line:
                move_needed = True
                old_pos = self.view.viewport_position()
                num_lines_to_move = cursor_actual_pos-center_line
        else:
            # reposition view if cursor is below a given line
            max_cursor_pos = num_lines_in_view-margin_size
            if cursor_actual_pos > max_cursor_pos:
                move_needed = True
                old_pos = self.view.viewport_position()
                num_lines_to_move = cursor_actual_pos-max_cursor_pos
                
        if move_needed:
            new_pos = (old_pos[0], old_pos[1]+num_lines_to_move*line_height)
            self.view.set_viewport_position(new_pos)


class ToggleBottomMarginCommand(sublime_plugin.TextCommand):
    """
    A TextCommand that can be set to run whenever a certain key binding is
    entered (for example, "alt+shift+m"). Toggles whether the bottom margin 
    is enabled or not.

    Example: (in Default.sublime-keymap)
        { "keys":["alt+shift+m"], "command":"toggle_bottom_margin" }
    """
    def run(self, edit):
        sets = sublime.load_settings('BottomMargin.sublime-settings')
        margin_on = sets.get(MARGIN_ON_SETTING)

        if type(margin_on)==bool:
            sets.set(MARGIN_ON_SETTING, not margin_on)
        else:   # margin was originally on; must turn off
            sets.set(MARGIN_ON_SETTING, False)

        sublime.save_settings('BottomMargin.sublime-settings')

    def is_checked(self):
        sets = sublime.load_settings('BottomMargin.sublime-settings')
        margin_on = sets.get(MARGIN_ON_SETTING)

        if type(margin_on)==bool:
            return margin_on
        else:
            return True


class ChangeBottomMarginSizeCommand(sublime_plugin.TextCommand):
    """
    A TextCommand that increases the bottom margin size by one line.
    Can be set to run whenever a key binding is entered (for example,
    "alt+shift+k" and "alt+shift+j").

    Example: (in Default.sublime-keymap)
        { "keys":["alt+shift+k"], "command":"change_bottom_margin_size",
            "args" : {"change_by" : 1} }
    """
    def run(self, edit, change_by):
        sets = sublime.load_settings('BottomMargin.sublime-settings')
        margin_size = sets.get(MARGIN_SIZE_SETTING)

        if not (type(margin_size)==int or type(margin_size)==float):
            margin_size = 3

        sets.set(MARGIN_SIZE_SETTING, int(margin_size)+change_by)
        sublime.save_settings('BottomMargin.sublime-settings')


class ToggleTypewriterModeCommand(sublime_plugin.TextCommand):
    """
    A TextCommand that toggles whether typewriter mode is on or not.
    Can be set to run when a key binding is entered (for example, 
    "alt+shift+t").

    Example: (in Default.sublime-keymap)
        { "keys":["alt+shift+t"], "command":"toggle_typewriter" }
    """
    def run(self, edit):
        sets = sublime.load_settings('BottomMargin.sublime-settings')
        typewriter_mode = sets.get(TYPEWRITER_SETTING)

        if type(typewriter_mode)==bool:
            sets.set(TYPEWRITER_SETTING, not typewriter_mode)
        else:   # typewriter was originally off; must turn on
            sets.set(TYPEWRITER_SETTING, True)

        sublime.save_settings('BottomMargin.sublime-settings')

    def is_checked(self):
        sets = sublime.load_settings('BottomMargin.sublime-settings')
        typewriter_mode = sets.get(TYPEWRITER_SETTING)

        if type(typewriter_mode)==bool:
            return typewriter_mode
        else:
            return False
