from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    if args != {}:
        matched_users = []
        for user in USERS:
            # Check if the user's id matches
            if "id" in args and user["id"] == args["id"]:
                matched_users.append(user)
                continue

            # Check if the user's name matches
            if "name" in args and args["name"].lower() in user["name"].lower():
                matched_users.append(user)
                continue

            # Check if the user's age matches
            if "age" in args and user["age"] in range(int(args["age"])-1, int(args["age"])+2):
                matched_users.append(user)
                continue

            # Check if the user's occupation matches
            if "occupation" in args and args["occupation"].lower() in user["occupation"].lower():
                matched_users.append(user)
                continue

        # Remove duplicates
        unique_users = []
        for user in matched_users:
            if user not in unique_users:
                unique_users.append(user)

        # Sort the results based on the priority of how they were matched
        sorted_users = sorted(unique_users, key=lambda user: (
            user["id"] == args.get("id"), 
            args.get("name") and args["name"].lower() in user["name"].lower(),
            args.get("age") and user["age"] in range(int(args["age"])-1, int(args["age"])+2),
            args.get("occupation") and args["occupation"].lower() in user["occupation"].lower()
        ), reverse=True)

        return sorted_users
    
    else:
        return USERS
