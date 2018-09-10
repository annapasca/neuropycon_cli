from setuptools import setup

setup(
    name='neuropycon_cli',
    version='0.1.0',
    author='Dmitrii Altukhov',
    author_email='dm.altukhov@ya.ru',
    description='command line interface for neuropycon.ephypype',
    license='MIT',
    zip_safe=False,
    packages=['neuropycon_cli'],
    url='https://github.com/neuropycon/neuropycon_cli.git',
    install_requires=[
        'nipype',
        'Click',
        'ephypype'
        # 'configparser'
    ],
    entry_points='''
        [console_scripts]
        neuropycon=neuropycon_cli.neuropycon:cli
    '''
)
