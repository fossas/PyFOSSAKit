from models.user import User

def list_users(client, email=None):
    params = {'email': email} if email else {}
    return client._request('GET', "/users", params=params)

def get_user(client, user_id):
    return client._request('GET', f"/users/{user_id}")

def delete_user(client, user_id):
    client._request('DELETE', f"/users/{user_id}")
    return {"message": "User deleted successfully."}

def set_user_permission(client, user_id, role_id):
    data = {'roleId': role_id}
    return client._request('PUT', f"/user/{user_id}/permission", data=data)

def enable_disable_user(client, user_id, enabled):
    data = {'enabled': enabled}
    return client._request('PUT', f"/user/{user_id}/enabled", data=data)

def set_user_team_roles(client, user_id, team_roles):
    return client._request('PUT', f"/user/{user_id}/team-roles", json=team_roles)

def list_roles(client):
    return client._request('GET', "/roles")

def list_teams(client):
    return client._request('GET', "/teams")

def create_team(client, team_data):
    return client._request('POST', "/teams", json=team_data)

def update_team(client, team_id, team_data):
    return client._request('PUT', f"/teams/{team_id}", json=team_data)

def assign_team_projects(client, team_id, projects):
    data = {'projects': projects}
    return client._request('PUT', f"/teams/{team_id}/projects", json=data)

def edit_team_users(client, team_id, action, users):
    data = {'action': action, 'users': users}
    return client._request('PUT', f"/teams/{team_id}/users", json=data)

def invite_user_to_organization(client, organization_id, emails):
    data = {'emails': emails}
    return client._request('POST', f"/organizations/{organization_id}/invite", json=data)