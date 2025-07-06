from tkX.tkx import using_ctk
import customtkinter
import tkinter as tk
from tkinter import ttk

def configure_modern_style(widget, **kwargs):
    """
    Configures a widget with a blend of tkinter.ttk and customtkinter styles.

    This function attempts to apply the provided style arguments using the
    most appropriate property names for the underlying widget library
    (customtkinter if available, otherwise ttk).
    """
    ttk_config = {}
    ctk_config = {}
    tk_config = {}  # Add this for tk.Tk window

    # Mapping of common argument names to tkinter/ttk and customtkinter equivalents
    arg_map = {
        "fg": {"ttk": "foreground", "ctk": "text_color"},
        "bg": {"ttk": "background", "ctk": "bg_color", "tk": "bg"},  # Added 'tk' mapping
        "activefg": {"ttk": "activeforeground", "ctk": "text_color_on_hover"},
        "activebg": {"ttk": "activebackground", "ctk": "hover_color"},
        "font": {"ttk": "font", "ctk": "font"},
        "relief": {"ttk": "relief", "ctk": "relief"},
        "borderwidth": {"ttk": "borderwidth", "ctk": "border_width"},
        "width": {"ttk": "width", "ctk": "width"},
        "height": {"ttk": "height", "ctk": "height"},
        "anchor": {"ttk": "anchor", "ctk": "anchor"},
        "wraplength": {"ttk": "wraplength", "ctk": "wraplength"},
        "justify": {"ttk": "justify", "ctk": "justify"},
        "cursor": {"ttk": "cursor", "ctk": "cursor"},
    }

    # Standard CTkButton arguments (for validation and handling)
    ctk_standard_args = ['width', 'height', 'border_width', 'relief', 'cursor',
                         'command', 'state', 'takefocus', 'textvariable',
                         'image', 'compound', 'padx', 'pady', 'anchor']

    for key, value in kwargs.items():
        if isinstance(widget, tk.Tk):  # Check if it's the main window
            tk_key = arg_map.get(key, {}).get("tk", key)  # Default to original key
            tk_config[tk_key] = value
        elif using_ctk:
            ctk_key = arg_map.get(key, {}).get("ctk", key)  # Default to original key
            if ctk_key not in ctk_standard_args and ctk_key != "font":  # Exclude font
                ctk_config[ctk_key] = value
            elif ctk_key in ctk_standard_args:
                ctk_config[ctk_key] = value  # Pass standard CTkButton args
        else:
            ttk_key = arg_map.get(key, {}).get("ttk", key)  # Default to original key
            ttk_config[ttk_key] = value

    if tk_config:
        widget.configure(**tk_config)  # Apply Tk window config
    elif using_ctk and ctk_config:
        widget.configure(**ctk_config)
    elif ttk_config:
        widget.configure(**ttk_config)