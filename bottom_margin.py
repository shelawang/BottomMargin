import sublime, sublime_plugin

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

    Settings:

    bottom_margin_off: 
        - set to true to disable reposition command (default Sublime behavior)
        - set to false (or remove) to enable reposition command
    bottom_margin_size:
        - set to 0 or any negative number to disable repositioning
        - set to a postive integer to control size of bottom margin
    """
    def run(self, edit):
        # get the necessary settings
        sets = sublime.load_settings('Preferences.sublime-settings')
        margin_size = sets.get('bottom_margin_size')
        margin_off = sets.get('bottom_margin_off')

        # check if settings exist and allow repositioning
        if type(margin_off)==bool and margin_off:
            return
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

        # reposition view if cursor is below a given line
        max_cursor_pos = num_lines_in_view-margin_size
        if cursor_actual_pos > max_cursor_pos:
            old_pos = self.view.viewport_position()
            num_extra_lines_needed = cursor_actual_pos-max_cursor_pos
            new_pos = (old_pos[0], old_pos[1]+num_extra_lines_needed*line_height)
            self.view.set_viewport_position(new_pos)


class ToggleBottomMarginCommand(sublime_plugin.TextCommand):
    """
    A TextCommand that can be set to run whenever a certain key binding is
    entered (for example, "alt+shift+m").

    Example: (in Default.sublime-keymap)
        [{ "keys":["alt+shift+m"], "command":"toggle_bottom_margin" }]
    """
    def run(self, edit):
        setting_name = 'bottom_margin_off'
        sets = sublime.load_settings('Preferences.sublime-settings')
        margin_off = sets.get(setting_name)

        if type(margin_off)==bool:
            sets.set(setting_name, not margin_off)
        else:   # margin was originally on; must turn off
            sets.set(setting_name, True)

        sublime.save_settings('Preferences.sublime-settings')
