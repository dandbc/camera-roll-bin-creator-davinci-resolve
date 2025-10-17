# 🎬 Camera Roll Bin Creator for DaVinci Resolve  
**by Daniel Bañuelos | More tools at [dandbc.mx/tools](https://dandbc.mx/tools)**

Generate professionally named camera roll bins inside **DaVinci Resolve’s Media Pool** — fast, clean, and error-free.  
Perfect for **DIT**, **assistant editors**, and **post teams** who need consistent structure like `A001`, `A002`, `A003` without manual labor.

---

## 🚀 Features

✔ **Batch Bin Creation** — Generate multiple camera roll folders in a single click  
✔ **Custom Start Index** — Begin at `A001`, `A101`, `B205`, etc.  
✔ **Digit Padding Control** — Choose between `A001`, `A0001`, etc.  
✔ **Camera Letter Prefix** — Apply A/B/C roll logic for multi-cam shoots  
✔ **Runs Directly in Resolve** — Accessible from *Workspace → Scripts → Edit*  
✔ **Safe Undo Integration** — Groups actions when Resolve supports it

---

## 🎯 Ideal Use Cases

- DIT ingest organization for multiple cards
- Preparing editorial bin structures before timeline work
- Standardizing naming conventions across shared workflows
- Multi-camera or multi-day shoot structure setup

---

## 📦 Installation

📄 Full step-by-step install instructions are available in **INSTALL.md**, but here’s the quick version:

> ✅ Copy `Create_CameraRoll_Bins.py` into your Resolve Scripts directory:  
> _Scripts/Edit/…_ → Restart Resolve → Run via **Workspace → Scripts → Edit**

---

## 📸 Example Output

If configured as:

| Prefix | Digits | Count | Start Index |
|--------|--------|-------|------------|
| `A`    | `3`    | `5`   | `101`      |

✅ Result in Media Pool:
A101
A102
A103
A104
A105

---

## 🔌 Usage Summary

1. **Select a folder** in the Media Pool (or Root if none is selected)
2. Run: `Workspace → Scripts → Edit → Camera Roll Bin Creator`
3. Enter:
   - Number of bins
   - Digit padding
   - Start index
   - Prefix letter (A, B, C…)
4. ✅ Click **OK** — bins are created instantly

---

## ⚖️ License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.  
You may use, modify, and distribute this tool, but any derivative must remain under GPL-3.0 and include credit to **Daniel Bañuelos**.

> Full license text is available in the `LICENSE` file.

---

## 👤 Author

**Daniel Bañuelos** — Postproduction Supervisor & Workflow Designer  
🔗 Website: https://dandbc.mx/tools  
🔗 LinkedIn: https://linkedin.com/in/danielbanuelos  
📧 Contact: dany.b@dandbc.mx

---

🎬 *Want custom DaVinci Resolve tools or workflow automation?*  
Let’s build something — **dany.b@dandbc.mx**
