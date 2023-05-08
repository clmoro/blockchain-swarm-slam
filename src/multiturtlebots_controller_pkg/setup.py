import os
from setuptools import setup
from glob import glob

package_name = 'multiturtlebots_controller_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', 'cslam_interfaces', 'cslam_common_interfaces'), glob('msg/*.msg'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='focalfossa',
    maintainer_email='focalfossa@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'robot_controller_1 = multiturtlebots_controller_pkg.robot_controller_1:main',
          'robot_estimator_1 = multiturtlebots_controller_pkg.robot_estimator_1:main',
          'robot_controller_2 = multiturtlebots_controller_pkg.robot_controller_2:main',
          'robot_estimator_2 = multiturtlebots_controller_pkg.robot_estimator_2:main',
          'robot_controller_3 = multiturtlebots_controller_pkg.robot_controller_3:main',
          'robot_estimator_3 = multiturtlebots_controller_pkg.robot_estimator_3:main',
          'robot_controller_4 = multiturtlebots_controller_pkg.robot_controller_4:main',
          'robot_estimator_4 = multiturtlebots_controller_pkg.robot_estimator_4:main',
          'odometry_noise = multiturtlebots_controller_pkg.odometry_noise:main',
        ],
    },
)
