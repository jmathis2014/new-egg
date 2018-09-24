from setuptools import setup

setup(name='egg-test',
      version='1.2',
      description='Egg testing Package',
      url='https://',
      author='James Mathis',
      author_email='james_mathis@americanwell.com',
      license='Github',
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: American Well',

            # Pick your license as you wish (should match "license" above)
            'License :: American Well',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 2.7',
        ],
      packages=['egg'],
      install_requires=[
           'requests',
      ],
#      scripts=[''],
      zip_safe=False)
