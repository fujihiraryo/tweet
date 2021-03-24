from setuptools import setup

setup(
    entry_points={
        "console_scripts": [
            "tweet=app:tweet",
        ]
    }
)
