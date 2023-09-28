# Flask Api which gets json files from a folder and read the information and returns in an api.

import os
import json
import asyncio
from flask import Flask, jsonify

app = Flask(__name__)

async def read_json_file(file_path):
    async with asyncio.Lock():
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data.get('account_id'), data.get('account_name')

async def process_folder(folder_path):
    tasks = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            tasks.append(read_json_file(file_path))
    results = await asyncio.gather(*tasks)
    return results


@app.route('/get_accounts', methods=['GET'])
def get_accounts():
    folder_path = "path/to/folder/json/accounts"
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    account_data = loop.run_until_complete(process_folder(folder_path))
    loop.close()
    account_info = [{'account_id': account_id, 'account_name': account_name} for account_id, account_name in account_data if account_id and account_name]
    return jsonify(account_info)

if __name__ == "__main__":
    app.run(debug=True)
