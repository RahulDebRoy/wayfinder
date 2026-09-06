' Wayfinder bridge — silent auto-start wrapper.
' Used only for automatic launch at Windows login (via Task Scheduler or
' the Startup folder). Runs the bridge with no visible console window.
'
' For manual runs where you want to see status/errors, use
' start_wayfinder_bridge.bat instead.

Set objShell = CreateObject("WScript.Shell")
scriptDir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
objShell.CurrentDirectory = scriptDir
objShell.Run "cmd /c python wayfinder_bridge.py", 0, False
