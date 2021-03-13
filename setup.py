# -*- coding: utf-8 -*-
"""Installer for the idgx.temas package."""

from setuptools import find_packages
from setuptools import setup


version = '3.0a1'
long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='idgx.temas',
    version=version,
    description="Temas para o Portal Padrao",
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: Theme",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Python Plone CMS IDGX .gov.br identidade_digital egov',
    author='ForContent',
    author_email='suporte@forcontent.com.br',
    url='https://github.com/collective/idgx.temas',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/idgx.temas',
        'Source': 'https://github.com/collective/idgx.temas',
        'Tracker': 'https://github.com/collective/idgx.temas/issues',
        # 'Documentation': 'https://idgx.temas.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['idgx'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7, >=3.8",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'Products.CMFPlone >=5.2',
        'idgx.portal',
        'plone.api',
        'plone.app.themingplugins',
        'plone.resource',
        'z3c.jbot',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
            'plone.app.theming',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
