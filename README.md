# MITSI Dashboard — WebView Edition

Offline desktop prototype based on MITSI Flow Manager Tkinter v3.3. Uses Python, pywebview and vanilla HTML/CSS/JavaScript.

## Run

```sh
pip install -r requirements.txt
python main.py
```

On Windows, install Microsoft Edge WebView2 Runtime if necessary. Open index.html directly for browser mode.

The starter supports flow tabs, grid cards, notes, screenshot upload/paste/drop, card swapping, and JSON .mitsi import/export. Annotation display is retained; interactive annotation editing, native recovery snapshots and full report parity are pending. Browser storage is best-effort; export projects regularly. No cloud storage or server is required.
