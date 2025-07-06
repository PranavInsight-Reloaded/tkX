import tkinter as tk
from tkinter import ttk

# Try to import customtkinter and set availability flag
try:
    import customtkinter
    ctk_available = True
except ImportError:
    print("Warning: customtkinter not found. Falling back to ttk.")
    ctk_available = False

using_ctk = ctk_available

def is_using_ctk():
    return using_ctk


# Singleton base class for ModernTk
_modern_tk_instance = None

class ModernTk:
    _instance = None

    def __new__(cls, window=None):
        global _modern_tk_instance
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            if using_ctk:
                cls._instance.window = window or customtkinter.CTk()
                cls._instance.poppins_regular_ctkfont = customtkinter.CTkFont(family="Poppins", size=13)
                cls._instance.poppins_bold_ctkfont = customtkinter.CTkFont(family="Poppins", size=13, weight="bold")
            else:
                cls._instance.window = window or tk.Tk()
                cls._instance.poppins_regular_tkfont = ("Poppins", 13)
                cls._instance.poppins_bold_tkfont = ("Poppins", 13, "bold")
            _modern_tk_instance = cls._instance
        return cls._instance


def _get_font(kwargs):
    global _modern_tk_instance
    if not _modern_tk_instance:
        _modern_tk_instance = ModernTk()
    return kwargs.pop("font", _modern_tk_instance.poppins_regular_ctkfont)


def ModernLabel(window=None, **kwargs):
    font = _get_font(kwargs)
    if using_ctk:
        return customtkinter.CTkLabel(window or _modern_tk_instance.window,
                                      text=kwargs.get("text", ""),
                                      font=font,
                                      text_color=kwargs.get("fg", "black"),
                                      bg_color=kwargs.get("bg", "transparent"))
    else:
        return ttk.Label(window or _modern_tk_instance.window,
                         text=kwargs.get("text", ""),
                         font=font)


def ModernSplLabel(window=None, **kwargs):
    font = _get_font(kwargs)
    if using_ctk:
        return customtkinter.CTkLabel(window or _modern_tk_instance.window,
                                      text=kwargs.get("text", ""),
                                      font=font,
                                      text_color=kwargs.get("fg", "black"),
                                      bg_color=kwargs.get("bg", "transparent"))
    else:
        return ttk.Label(window or _modern_tk_instance.window,
                         text=kwargs.get("text", ""),
                         font=font)


def ModernMaxRoundedLabel(window=None, **kwargs):
    font = _get_font(kwargs)
    if using_ctk:
        return customtkinter.CTkLabel(window or _modern_tk_instance.window,
                                      text=kwargs.get("text", ""),
                                      font=font,
                                      text_color=kwargs.get("fg", "black"),
                                      bg_color=kwargs.get("bg", "transparent"))
    else:
        return ttk.Label(window or _modern_tk_instance.window,
                         text=kwargs.get("text", ""),
                         font=font)


def ModernRoundedButton(window=None, **kwargs):
    font = _get_font(kwargs)
    if using_ctk:
        return customtkinter.CTkButton(window or _modern_tk_instance.window,
                                       text=kwargs.get("text", ""),
                                       command=kwargs.get("command", None),
                                       font=font,
                                       fg_color=kwargs.get("bg", None),
                                       hover_color=kwargs.get("activebg", None),
                                       text_color=kwargs.get("fg", "black"),
                                       corner_radius=10)
    else:
        return ttk.Button(window or _modern_tk_instance.window,
                          text=kwargs.get("text", ""),
                          command=kwargs.get("command", None),
                          font=font)


def ModernEntry(window=None, **kwargs):
    font = _get_font(kwargs)
    if using_ctk:
        return customtkinter.CTkEntry(window or _modern_tk_instance.window,
                                      font=font,
                                      placeholder_text=kwargs.get("placeholder_text", ""),
                                      show=kwargs.get("show", None),
                                      text_color=kwargs.get("fg", "black"),
                                      bg_color=kwargs.get("bg", "transparent"),
                                      border_color=kwargs.get("border_color", None))
    else:
        return ttk.Entry(window or _modern_tk_instance.window,
                         font=font)


def ModernRadiobutton(window=None, **kwargs):
    font = _get_font(kwargs)
    if using_ctk:
        return customtkinter.CTkRadioButton(window or _modern_tk_instance.window,
                                            text=kwargs.get("text", ""),
                                            value=kwargs.get("value", None),
                                            variable=kwargs.get("variable", None),
                                            font=font,
                                            text_color=kwargs.get("fg", "black"),
                                            bg_color=kwargs.get("bg", "transparent"))
    else:
        return ttk.Radiobutton(window or _modern_tk_instance.window,
                               text=kwargs.get("text", ""),
                               value=kwargs.get("value", None),
                               variable=kwargs.get("variable", None),
                               font=font)


def ModernCheckbox(window=None, **kwargs):
    font = _get_font(kwargs)
    if using_ctk:
        return customtkinter.CTkCheckBox(window or _modern_tk_instance.window,
                                         text=kwargs.get("text", ""),
                                         font=font,
                                         text_color=kwargs.get("fg", "black"),
                                         bg_color=kwargs.get("bg", "transparent"))
    else:
        return ttk.Checkbutton(window or _modern_tk_instance.window,
                               text=kwargs.get("text", ""),
                               font=font)


def ModernCBoxes(window=None, values=None, **kwargs):
    font = _get_font(kwargs)
    values = values or kwargs.get("values", [])
    if using_ctk:
        return customtkinter.CTkComboBox(window or _modern_tk_instance.window,
                                         values=values,
                                         font=font,
                                         dropdown_fg_color=kwargs.get("dropdown_fg_color", None),
                                         dropdown_text_color=kwargs.get("fg", "black"),
                                         fg_color=kwargs.get("bg", "#f2f2f2"))
    else:
        return ttk.Combobox(window or _modern_tk_instance.window,
                            values=values,
                            font=font)