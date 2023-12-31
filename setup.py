from setuptools import setup, Command, find_packages
from setuptools.command.install import install
import os
# import subprocess

package_data = {
    '': ['*.png', '*.txt', '*.md', '*.py'],
    'Scripts': ['*.py'],
}

class Install(install):

    def run(self):
        install.run(self)
        os.system('python3 setup.py bdist_wheel')
        os.system('pip install dist/*.py')
        os.system('python3 post_install.py')

with open('README.md', 'r') as f:
    long_desctiption = f.read()

from setuptools import setup, Command
import os

setup(
    name='BashMate',
    version='0.1',
    author='HARSHIT',
    author_email='harshitbhadana111@gmail.co',
    description='Developer focused Command Line Tools',
    long_description=long_desctiption,
    long_description_content_type='text/markdown',
    packages= ['Scripts/'],
    # package_data= package_data,
    licence_files = ['LICENSE.txt'],
    scripts=['Scripts/workman.py', 'Scripts/wizard.py', 'post_install.py'],

    install_requires=['colorama', 'openai'],

    entry_points={
        'console_scripts': [
            'wm = workman:main',
            'wiz = wizard:main',
            'bashmate = post_install:post_install'
        ],
    },

    cmdclass={
        'install' : Install
    }
)