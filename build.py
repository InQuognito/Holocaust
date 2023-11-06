import logic

import os, shutil

# Export settings
file_to_run = 'main'
name_technical = logic.name_localized.lower().replace(' ', '_')

# Build executeable
if os.path.isdir('dist'):
	shutil.rmtree('dist/')
os.system('py -m PyInstaller ' + file_to_run + '.py --onefile')

# Rename file and ZIP
os.rename('dist/' + file_to_run + '.exe', 'dist/' + name_technical + '.exe')
shutil.make_archive(logic.name_localized, 'zip', 'dist/')

# Cleanup
os.remove(file_to_run + '.spec')
shutil.rmtree('build/')
