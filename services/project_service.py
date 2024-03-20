from models.project import Project

def get_project_details(client, project_id):
    return client._request('GET', f"/projects/{project_id}")

def list_projects(client):
    return client._request('GET', "/projects")

def delete_project(client, project_id):
    client._request('DELETE', f"/projects/{project_id}")
    return {"message": "Project deleted successfully."}