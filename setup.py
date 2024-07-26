setup(
    name="CUkeys",
    version="1.0.0",
    description="Play custom sounds when key is pressed",
    author="Joža",
    include_package_data=True,
    install_requires=[
        "keyboard", "pygame"
    ],
    entry_points={"console_scripts": ["realpython=reader.__main__:main"]},
)