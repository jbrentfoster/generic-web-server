import json
import logging
import utils


async def send_async_request(url, user, password):
    response_json_list = []
    try:
        response = await utils.rest_get_tornado_httpclient(url, user, password)
        response_json = json.loads(response)
        if type(response_json) is dict:
            response_json_list.append(response_json)
            response = json.dumps(response_json_list, indent=2, sort_keys=True)
        with open("jsongets/response.json", 'w', encoding="utf8") as f:
            # json.dump(response, f, sort_keys=True, indent=4, separators=(',', ': '))
            f.write(response)
            f.close()
        return response
    except Exception as err:
        result = {'action': 'collect', 'status': 'failed'}
        logging.info(response)
        return "Something went wrong!"


def get_response():
    with open("jsongets/response.json", 'r', ) as f:
        response = json.load(f)
        f.close()
    return json.dumps(response)


def process_ws_message(message):
    response = "Got the message from websocket, here's my reply"
    return response
