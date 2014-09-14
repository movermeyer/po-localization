# coding=utf-8

from distutils.core import setup

__version__ = 'unknown'
with open('po_localization/version.py') as version_file:
    exec(version_file.read())

setup(
    name='po_localization',
    packages=['po_localization', 'po_localization.tests'],
    version=__version__,
    description='Localize Django applications without compiling .po files',
    author='Kevin Michel',
    author_email='kmichel.info@gmail.com',
    url='https://github.com/kmichel/po-localization',
    download_url='https://github.com/kmichel/po-localization/archive/v{}.tar.gz'.format(__version__),
    keywords=['django', 'localization'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Localization',
    ],
    requires=['django'],
)
