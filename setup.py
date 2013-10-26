#import DistUtilsExtra.auto
#try:
'''
from cx_Freeze import setup, Executable
files = ["synchronize-rd.png", "COPYING"]

buildOptions = dict(packages=['wx.lib.pubsub'], excludes=[], include_files=files, includes=[])

executables = [
Executable(script='synchronizerd.py', targetName='synchronizerd', shortcutName='SynchroniZeRD', shortcutDir='DesktopFolder', icon='synchronize-rd.png')
]
setup(name='SynchroniZeRD',
      version='1.0.0',
      license='GPL-3',
      author='Ronnie Andrew',
      author_email='ronnieandrew92@gmail.com',
      description='A simple folder synchronizer application that uses rsync.',
      long_description='',
      url="http://www.roandigital.com/applications/synchronizerd",
      options=dict(build_exe=buildOptions),
      executables=executables, requires=['wx', 'rsync'])

'''
#except:
from distutils.core import setup

setup(name='SynchroniZerD',
        version='1.0.0',
        description='A simple folder synchronizer application that uses rsync.',
        long_description='SynchroniZeRD is a folder synchronizer application that uses rsync to synchronize and wxWidgets for the UI',
        author='Ronnie Andrew',
        author_email='ronnieandrew92@gmail.com',
        url='http://www.launchpad.net/synchronizerd',
        #py_modules=['synchronizerd'],
        #scripts=['synchronizerd.py'],
        packages=['synchronizerd'],
        package_dir=['synchronizerd':'SynchroniZeRD/synchronizerd'],
        data_files=[('images', ['images/synchronize-rd.png'])]
        )
