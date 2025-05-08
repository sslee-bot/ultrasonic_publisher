import os
from glob import glob
from setuptools import setup

package_name = 'ultrasonic_publisher'

setup(
    name=package_name,
    version='0.19.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
        # (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='sslee-bot',
    author_email='physism@gmail.com',
    maintainer='sslee-bot',
    maintainer_email='physism@gmail.com',
    description='ros2 ultrasonic publisher',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ultrasonic_publisher_node = ultrasonic_publisher.ultrasonic_publisher_node:main',
        ]
    }
)
