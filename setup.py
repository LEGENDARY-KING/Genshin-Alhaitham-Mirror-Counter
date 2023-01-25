import cx_Freeze
executables = [cx_Freeze.Executable("main.py",icon="alhaitham.ico",base="Win32GUI",target_name="Alhaitham Mirror Counter.exe")]
cx_Freeze.setup(
    name="Alhaitham Mirror Counter",
    options={"build_exe": {"packages":["pygame","ctypes","typing","pynput","configparser"], "include_files":["alhaitham.jpg","config.ini"]}},
    executables=executables
)
