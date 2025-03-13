import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()



__name__ = "new"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "ManishaKusalkar"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "mk071803@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version="0.0.0",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for text summarization task",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
