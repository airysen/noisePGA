from setuptools import setup, find_packages


def lib_import(name):
    for lb in name:
        try:
            exec('import {0}'.format(lb))
        except ImportError as e:
            print("\n{0} not found. {1}. \n".format(lb, e))
            exit()

lib_import(['numpy', 'deap', 'sklearn', 'pandas'])

setup(name='noisePGA',
      version='0.1',
      description='Noise PGA',
      long_description='A simpe genetic algorithm for feature selection',
      classifiers=[
          'Development Status :: Alpha',
          'License :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Feature selection :: Genetic algorithm',
      ],
      url='https://github.com/airysen/noisePGA',
      author='Arseniy Kustov',
      author_email='me@airysen.co',
      license='MIT',
      packages=find_packages(),
      install_requires=['deap', 'sklearn'
                        ],
      include_package_data=True,

      zip_safe=False)
