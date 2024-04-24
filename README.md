# PyFOSSAKit

A Python SDK for interacting with the FOSSA API, providing an easy way to integrate FOSSA's software composition analysis and license compliance capabilities into your Python applications.

## Introduction

PyFOSSAKit is an open-source Python library designed to simplify and automate the process of interacting with the [FOSSA](https://fossa.com/) API. It allows developers to quickly retrieve information about projects, manage licenses, and handle security issues directly through Python scripts.

## Features

- Comprehensive coverage of FOSSA API endpoints.
- Straightforward methods for managing projects, revisions, issues, and users.
- Simplified handling of vulnerabilities and dependencies.
- Support for custom configurations and extensible codebase.

## Configuration

To use PyFOSSAKit, you need to set your FOSSA API key as an environment variable. This is important for keeping your API key secure and not hard-coded in your application.

### Setting Environment Variables

#### On macOS and Linux:

Open a terminal and use the following command to set the `FOSSA_API_KEY` environment variable (replace `your_api_key_here` with your actual FOSSA API key):

```bash
export FOSSA_API_KEY=your_api_key_here
```

To make this change permanent, add the export command to your shell's configuration file (e.g., ~/.bashrc, ~/.zshrc).

On Windows:

Open a command prompt or PowerShell and set the FOSSA_API_KEY variable:

```bash
set FOSSA_API_KEY=your_api_key_here
```


For a more permanent solution, you can set the environment variable through the System Properties:

1) Press Win + R, type sysdm.cpl, and press Enter.
2) Go to the Advanced tab and click on Environment Variables.
3) Under System Variables, click New.
4) Set the variable name as FOSSA_API_KEY and the value as your actual API key.
5) After setting the environment variable, restart any open terminals or IDEs for the changes to take effect.

### Verifying the Environment Variable
To verify that the FOSSA_API_KEY has been set correctly, you can echo it in your terminal:

macOS and Linux:

```bash
echo $FOSSA_API_KEY
```

Windows:

```bash
echo %FOSSA_API_KEY%
```

## Installation


Since PyFOSSAKit uses Poetry for package management, install it using Poetry instead of pip:

```bash
poetry add PyFOSSAKit
```

Or, clone the repository and install the dependencies via Poetry:

```bash
git clone https://your-repository-url.git
cd PyFOSSAKit
poetry install
```

Quickstart example of listing all projects using the PyFOSSAKit client:

```bash
from fossa_sdk import FOSSAClient
```

### Usage
After configuring your environment variable, you can use the SDK as follows:

```python
from client import FOSSAClient

# Initialize the client with your FOSSA API key
fossa_client = FOSSAClient(api_key=os.getenv('FOSSA_API_KEY'))

# Now you can use fossa_client to interact with the FOSSA API
# ...
```

For more detailed usage examples, refer to the usage examples section.


## Usage Examples

### Initialize the FOSSA client with your API key

```bash
client = FOSSAClient(api_key='your_fossa_api_key')
```

### List all projects in your FOSSA account

```bash
projects = client.list_projects()
```

### Listing Users

Retrieve and list all users within your organization.

```python
users = client.list_users()
for user in users:
    print(user.username, user.email)
```

### Getting Project Details

Fetch detailed information about a specific project using its identifier.

```python
project_id = 'your_project_id'
project_details = client.get_project_details(project_id)
print(project_details.name, project_details.id)
```


### Deleting a Project

Delete a project from FOSSA by providing its identifier.

```python
delete_response = client.delete_project(project_id)
print(delete_response)
```

### Retrieving Security Issues by Team

Get a list of security issues associated with each team.

```python
security_issues = client.get_security_issues_by_team()
for issue in security_issues:
    print(issue.id, issue.title)
```

### Managing Vulnerabilities

Check for vulnerabilities and get safe version recommendations.

```python
locators = ['locator1', 'locator2']
vulnerabilities = client.get_vulnerabilities_by_locator(locators)
for vulnerability in vulnerabilities:
    print(vulnerability.id, vulnerability.description)

safe_versions = client.get_next_safe_versions([revision_locator])
for safe_version in safe_versions:
    print(safe_version['locator'], safe_version['nextSafeVersion'])
```

### Testing

Run tests using pytest:

```bash
pytest tests
```