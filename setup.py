from setuptools import find_packages,setup

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT="-e ."

def get_requirements()->list[str]:
   with open(REQUIREMENT_FILE_NAME)as requirements_file:
      requirement_list=requirement_file.readline()
      requirement_list=[requirements_name.repalce("\n", "")for requirementsn in requirement_list]
      if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name="sensor",
    version="0.0.2",
    author="sanjay",
    author_email="bohara.sanjay@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)