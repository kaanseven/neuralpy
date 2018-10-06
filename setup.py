from setuptools import find_packages, setup
print(find_packages(exclude=['DEPneuralpy']))
setup(
	name='neuralpy-upg',
	version='1.3.0',
        description='neuralpy for Python 3 - The most intuitive Neural Network Model',
	author='Jonathan N. Lee',
        keywords='neuralpy neural networks',
	author_email='jonathan_lee@berkeley.edu',
	url='https://github.com/jon--lee/neuralpy',
	license='MIT',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
		'Topic :: Software Development',
		'Topic :: Scientific/Engineering',
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.7',
		],
	install_requires=['numpy==1.15.2', 'matplotlib==3.0.0'],
        packages=find_packages(exclude=['DEPneuralpy'])
)
