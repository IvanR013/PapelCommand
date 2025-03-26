from setuptools import setup, find_packages

setup(
    name='papel',
    version='1.1.0',
    py_modules=['papel'],
    install_requires=['send2trash'],
    entry_points={
        'console_scripts': [
            'papel=papel:move_to_trash',  # Aquí se hace referencia a tu función 'move_to_trash' dentro del archivo 'papel.py'
        ],
    },
    author='Iván Rodriguez',
    description='In Windows, macOS & Linux, allows you to move instantly any file to recycle bin.',
    long_description=open('README.mkd').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/IvanR013/PapelCommand.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',  # Aquí se especifica la licencia directamente
)
