from LSP.plugin import AbstractPlugin, register_plugin, unregister_plugin
from LSP.plugin.core.protocol import Location
from LSP.plugin.core.typing import Any, Callable, List, Mapping
from LSP.plugin.locationpicker import LocationPicker
import os
import sublime
from urllib.parse import unquote, urlparse


SESSION_NAME = "mdita-lsp"


class MditaLsp(AbstractPlugin):
    @classmethod
    def name(cls) -> str:
        return SESSION_NAME

    @classmethod
    def needs_update_or_installation(cls) -> bool:
        return False

    def on_pre_server_command(self, command: Mapping[str, Any], done_callback: Callable[[], None]) -> bool:
        command_name = command['command']
        if command_name == 'mdita-lsp.findReferences':
            command_arguments = command['arguments']
            if command_arguments and 'locations' in command_arguments[0]:
                self._handle_show_references(command_arguments[0]['locations'])
            done_callback()
            return True
        if command_name == 'mdita-lsp.createFile':
            command_arguments = command.get('arguments')
            if command_arguments and len(command_arguments) > 0:
                self._handle_create_file(str(command_arguments[0]))
            done_callback()
            return True
        return False

    def _handle_create_file(self, uri: str) -> None:
        parsed = urlparse(uri)
        path = unquote(parsed.path)
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.close()
        window = sublime.active_window()
        if window:
            window.open_file(path)

    def _handle_show_references(self, references: List[Location]) -> None:
        session = self.weaksession()
        if not session:
            return
        view = sublime.active_window().active_view()
        if not view:
            return
        if len(references) == 1:
            args = {
                'location': references[0],
                'session_name': session.config.name,
            }
            window = view.window()
            if window:
                window.run_command('lsp_open_location', args)
        elif references:
            LocationPicker(view, session, references, side_by_side=False)
        else:
            sublime.status_message('No references found')


def plugin_loaded() -> None:
    register_plugin(MditaLsp)


def plugin_unloaded() -> None:
    unregister_plugin(MditaLsp)
