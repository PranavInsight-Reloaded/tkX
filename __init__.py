# Fixed __init__.py - Breaking the circular import
# First import the core modules
from .tkx import ModernLabel, ModernSplLabel, ModernRoundedButton, ModernMaxRoundedLabel
from .tkx import ModernRadiobutton, ModernCheckbox, ModernEntry, ModernCBoxes
from .tkx import using_ctk, is_using_ctk
from .styleX import configure_modern_style
# Then import the extras
from .modern_card import ModernCard

