from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    description="A command-line math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Pretom Das Hira",
    author_email="freelancer.pretomhir@gmail.com",
    url="https://github.com/pretomhira/dsss_homework_2",
    license="Apache",
    install_requires=[],  # Add dependencies here if required (e.g., numpy, pandas)
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.mathQuiz:mathQuiz"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
