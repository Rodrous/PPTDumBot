import base64

async def feedback_n_bugs_json(ctx, args: str, selectName: str):
    with open("config/notion.txt") as file:
        f = file.readlines()
    notion = []
    for item in f:
        n = item.partition("#")[0]
        n = n.rstrip()
        n = base64.b64decode(n).decode("utf-8")
        notion.append(n)

    NOTION_KEY = str(notion[0])
    NOTION_ID = str(notion[1])
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