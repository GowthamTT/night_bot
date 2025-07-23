from setuptools import find_packages, setup

package_name = 'yolov8'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ultra',
    maintainer_email='ultra@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'yolo_ob = yolov8.object_detection:main',
            'int_det = yolov8.intruder_detection:main',
            'rot_py = yolov8.routine:main' 
        ],
    },
)
