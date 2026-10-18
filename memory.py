conversation_history = []

def remember(role, content):

    conversation_history.append(
        {
            "role": role,
            "content": content
        }
    )

def get_memory():

    return conversation_history[-10:]