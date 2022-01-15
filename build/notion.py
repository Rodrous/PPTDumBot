import os

async def feedback_n_bugs_json(ctx, args: str, selectName: str):
    NOTION_KEY = os.environ.get("notionKey")
    NOTION_ID = os.environ.get("notionDbID")
    AUTHOR = str(ctx.author)
    AUTHOR_ID = int(ctx.author.clientId)
    MSG = args
    header = {"Authorization": NOTION_KEY, "Notion-Version": "2021-05-13"}
    data = {
        "parent": {
            "database_id": NOTION_ID
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": AUTHOR
                        }
                    }
                ]
            },
            "Type": {
                "select": {
                    "name": selectName
                }
            },
            "ID": {
                "number": AUTHOR_ID
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "text": [
                        {
                            "type": "text",
                            "text": {
                                "content": args
                            }
                        }
                    ]
                }
            }
        ]
    }
    return header, data