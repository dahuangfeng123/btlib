from distutils.core import setup

setup(name='BTLib',
      version='0.1a1',
      description='Multi-Lingual Novel Presentation Platform',
      author='Michael Williams, Semen Walter',
      author_email='draringi@draringi.net',
      url='https://github.com/draringi/btlib/',
      packages=['btlib'],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'Framework :: Django',
          'Environment :: Web Environment',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Topic :: Text Editors',
      ],
      long_description=open('README.rst').read(),
      install_requires=[
          "Django >= 1.4.0",
          "PIL>=1.1.7",
          "diff-match-patch>=20120106",
      ],
)
