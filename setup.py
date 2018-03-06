from distutils.core import setup

setup(
    name = 'LineTimeline',
    version = '1.0.0',
    description = 'Line TimeLine Api',
    author = 'Takanashi',
    author_email = 'tytyty311@cream.pink',
    install_requires = ['requests', 'json', 'lxml'],
    url = 'https://github.com/sharplin/LineTimeline',
    license = 'BSD-3-Clause',
    packages = ["LineTimeline"]
)
