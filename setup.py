from setuptools import setup

setup(name = 'jotit',
      packages = ['jotit', 'jotit.static', 'jotit.templates'],
      package_data = {'jotit': ['defaults.yml'], 'jotit.static': ['humans.txt'], 'jotit.templates': ['*.html']},
      version = '0.1.3',
      description = 'Super minimal file-based CMS',
      author = 'Nikola Kantar',
      author_email = 'nik@nkantar.com',
      url = 'https://github.com/nkantar/jotit',
      download_url = 'https://github.com/nkantar/jotit/tarball/0.1.3',
      install_requires=['Flask', 'gfm', 'pyyaml'],
      keywords = ['cms', 'markdown'],
      classifiers = [],
      license = 'GPLv3',
      zip_safe = False)
