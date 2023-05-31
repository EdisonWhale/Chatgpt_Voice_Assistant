import json
import random

# Get recent messages


def get_recent_messages():

    # define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are interviewing the user for a job as retail assitant Ask short questions that are relevant to the juior position. You name is WHALE. The user is Edison.Keep answer under 30 words. "
    }

    # Initialize messgae
    messages = []

    # Add a random element
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + \
            "Your response will include soem dry humour."
    else:
        learn_instruction["content"] = learn_instruction["content"] + \
            " Your response will include challenging question."

    # Append instruction to message
    messages.append(learn_instruction)

    # Get last message

    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # append last 5 items of data
        if data:
            if len(data) < 5:
                for item in data:
                    messages.append(item)
            else:
                for item in data[-5:]:
                    messages.append(item)

    except Exception as e:
        print(e)
        pass

    return messages
