# cse6250-project-structure-validator
This project is for students enrolled in Georgia Tech's CSE6250: Big Data Analytics for Healthcare. Ensuring your project directory structure conforms to the project submission requirements can be a pain (for TAs and students alike). Let's make life a little easier.

## Usage
```bash
$ python validate.py <PATH_TO_PARENT_OF_PROJECT> <PROJECT_NAME>
```

| Argument | Description | Example  |
| ------------- |:-------------:| -----:|
| <PATH_TO_PARENT_OF_PROJECT> | Path to the parent directory containing your project | /home/student/projects/cse6250/hw4 |
| <PROJECT_NAME> | The project being validated | hw4 |

**Note**: `<PATH_TO_PARENT_OF_PROJECT>` should contain the directory `<GA_TECH_ID>-<GA_TECH_ACCOUNT>-<PROJECT_NAME>/` (Ex. 012345678-johnsmith1-hw4)

Example:
```bash
$ python validate.py /home/student/projects/cse6250/hw4 hw4
```
