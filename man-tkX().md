🚀 Quick Start


# Quick start to tkX():
 `from tkX.tkx import ModernTk, ModernLabel, ModernEntry, ModernRoundedButton`
`from ModernCard import ModernCard`

```app = ModernTk().window
app.title("Modern UI")
app.geometry("400x400")

ModernLabel(app, text="Welcome!", fg="white").pack(pady=10)

ModernEntry(app, placeholder_text="Username", fg="black").pack(pady=5)
ModernRoundedButton(app, text="Login", fg="white", bg="#7cfc00").pack(pady=10)

card = ModernCard(app, title="Hello Ganache!", description="This is a frosted, reusable card.", button_text="Go", command=lambda: print("Go clicked"))
card.pack(pady=20)
app.mainloop()
```

# 🛠 Folder Structure

tkX/
│
├── tkx.py              # Main widget components
├── ModernCard.py       # Simplified, animated card component
├── __init__.py         # Module entry
└── demo/               # (Optional) Sample demos

# 🧠 Built With
1.🐍 Python + Tkinter

2.🌟 customtkinter

3.🎨 Inspired by iOS & Dribbble UI palettes

# 🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss the vibe.

# 📄 License
MIT — do whatever you want, just don’t ship it with Comic Sans 😤

---

## 📚 Programming Guide – `docs/USAGE.md`

markdown
# 🧠 How to Use tkX Components

## 🔹 Initialization

```python
from tkX.tkx import ModernTk
window = ModernTk().window
🔹 Labels
python
Copy
Edit
ModernLabel(window, text="Hello", fg="white", bg="#1e1e1e").pack()
ModernSplLabel(window, text="Special", fg="cyan").pack()
ModernMaxRoundedLabel(window, text="Large Title", fg="magenta").pack()
🔹 Inputs
python
Copy
Edit
ModernEntry(window, placeholder_text="Type here...", fg="white", bg="#333").pack()
ModernCBoxes(window, values=["One", "Two", "Three"], fg="black", bg="#eee").pack()
🔹 Buttons
python
Copy
Edit
ModernRoundedButton(window, text="Click Me", command=do_something, fg="white", bg="#7cfc00").pack()
🔹 Toggles
python
Copy
Edit
ModernCheckbox(window, text="Enable Feature", fg="white").pack()
ModernRadiobutton(window, text="Option A", variable=some_var, value="a", fg="white").pack()
🔹 Cards
python
Copy
Edit
from ModernCard import ModernCard

card = ModernCard(window,
    title="Your Title",
    description="Your details go here.",
    button_text="Do It",
    command=your_func
)
card.pack(pady=20)
Includes auto-hover effect, left-aligned content, and click-ready CTA.
```
# 🎨 Theme Tip
## Create a shared theme dict:
```
python
Copy
Edit
THEME = {
  "bg": "#1e1e2e",
  "fg": "#f8f8f2",
  "accent": "#ff79c6",
  "button": "#7cfc00"
}
```
# Then pass values like: fg=THEME["fg"], bg=THEME["bg"]

💡 Tips
1.Always initialize ModernTk first

2.Use pack(pady=...) generously for spacing

3.Combine ModernCard inside Frame or modal for reusability

---

### Need a logo, dark/light toggle system, or Python package version with `setup.py`?

### Just say the word — I can prep it like it’s ready for PyPI 🧁
