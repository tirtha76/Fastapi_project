def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"],
    }
def detail_helper(detail) -> dict:
    return {
        "id" : str(detail["_id"]),
        "location" : detail["location"],
        "number" : detail["number"],
        "ref_id" : str(detail["ref_id"]),

    }