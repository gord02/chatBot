import re

def remove_chat_metadata(chat_export_file):
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # e.g. "9/16/22, 06:34"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # e.g. "Martin"
    metadata_end = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_end

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern, "", content)
    
    data = tuple(cleaned_corpus.split("\n"))
    data = remove_non_message_text(data)
    return data

def remove_non_message_text(export_text_lines):
    messages = export_text_lines[1:-1]
    filtered_messages = []
    filter_out_msgs = ("<Media omitted>")
    for msg in messages:
        if msg not in filter_out_msgs:
            filtered_messages.append(msg)
    return filtered_messages
