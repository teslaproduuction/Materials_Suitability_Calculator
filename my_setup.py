import os

name_proj = "test_eel"
noconsole = "--windowed"  # ставим "" - если нужна консоль, " --windowed " - если не нужна
onefile = " --onefile "  # указываем, что exe должен быть упакован в один файл
if __name__ == "__main__":
    cmd_txt = f'python -m eel main.py web --noconfirm --onefile --hide-console "hide-late" --name {name_proj} --icon=icon.ico'
    os.system(cmd_txt)
