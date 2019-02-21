import os
ps=['Microsoft.Photos.exe','MicrosoftEdge.exe',
'WhatsNew.Store.exe','HxOutlook.exe','MicrosoftEdgeCP.exe','PaintStudio.View.exe',
'spoolsv.exe','igfxTray.exe','CCleaner64.exe','SystemSettings.exe']
print("hello im the task murderer by Oyasis\n I kill tasks")
for PS in ps:
	os.system("taskkill /f /im "+PS)

print(os.cpucount())
