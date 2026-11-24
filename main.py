from pathlib import Path
import webview

if __name__ == '__main__':
    webview.create_window('MITSI Dashboard — WebView', (Path(__file__).resolve().parent / 'index.html').as_uri(), width=1200, height=750)
    webview.start()
