from LSP.plugin import AbstractPlugin, ClientConfig, register_plugin, unregister_plugin
from LSP.plugin.core.protocol import Location
from LSP.plugin.core.typing import Any, Callable, List, Mapping, Optional
from LSP.plugin.locationpicker import LocationPicker
import os
import shutil
import sublime
from urllib.parse import unquote, urlparse


SESSION_NAME = "mdita"

_SEARCH_PATHS = [
    os.path.expanduser("~/go/bin"),
    os.path.expanduser("~/.local/bin"),
    "/usr/local/bin",
]


def _find_binary() -> str:
    found = shutil.which("mdita-lsp")
    if found:
        return found
    for d in _SEARCH_PATHS:
        candidate = os.path.join(d, "mdita-lsp")
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate
    return "mdita-lsp"


class MditaLsp(AbstractPlugin):
    @classmethod
    def name(cls) -> str:
        return SESSION_NAME

    @classmethod
    def needs_update_or_installation(cls) -> bool:
        return False

    @classmethod
    def additional_variables(cls) -> dict:
        return {"mdita_lsp_path": _find_binary()}

    @classmethod
    def on_pre_start(cls, window: sublime.Window, initiating_view: sublime.View,
                     workspace_folders: List[Any], configuration: ClientConfig) -> Optional[str]:
        binary = _find_binary()
        configuration.command = [binary]
        return None

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
