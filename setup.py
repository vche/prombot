# -*- encoding: utf-8 *-*
import sys
from setuptools import setup, find_packages

min_python = (3, 4)
if sys.version_info < min_python:
    print("prombot requires Python %d.%d or later" % min_python)
    sys.exit(1)

setup(
    name='prombot',
    author='Vivien Chene',
    author_email='viv.chene@gmail.com',
    # url='https://prombot.readthedocs.io/',
    description='Send prometheus alerts to a telegram bot',
    license='BSD',
    platforms=['Linux', 'MacOS X', 'FreeBSD', 'OpenBSD', 'NetBSD', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: BSD :: OpenBSD',
        'Operating System :: POSIX :: BSD :: NetBSD',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Monitoring',
    ],
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'prombot = prombot.app:main',
        ]
    },
    setup_requires=['setuptools_scm>=1.7'],
    install_requires=[
        'flask>=0.10',
        'requests',
    ],
)
