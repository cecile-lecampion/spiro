from setuptools import setup, find_packages
setup(name = 'spiro',
      version = '1.0b2',
      packages = find_packages(),
      scripts = ['bin/spiro'],
      install_requires = ['picamera==1.13', 'RPi.GPIO==0.6.5', 'Flask==1.1.1', 'gevent==1.4.0'],
      author = 'Jonas Ohlsson',
      author_email = 'jonas.ohlsson@slu.se',
      description = 'Control software for the SPIRO biological imaging system',
      url = 'https://github.com/jonasoh/spiro',
      include_package_data = True,
      zip_safe = False,
      )
