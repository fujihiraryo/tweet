from setuptools import setup

setup(
    name="tweet",
    version="0.0.1",
    entry_points={
        "console_scripts": [
            "tweet=tweet.app:tweet",
        ]
    },
    py_modules=["tweet.app"],
)
