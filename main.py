from openai import OpenAI

ALLOWED_GPT_MODELS = ['gpt-4o', 'gpt-4o-mini']

client = OpenAI()

def get_file_content(path: str) -> str | None:
    """
    Get content from specified file

    :param path: Path to the file
    :type path: str
    :return: String or None (if error)
    :rtype: str | None
    """
    if path == None or path == '':
        return None
    with open(path, "r", encoding="utf-8") as source_file:
        try:
            return source_file.read()
        except Exception as e:
            print(e)

def get_result_from_api(
    api_client: OpenAI, model: str, prompt: str, system_role_content: str
) -> str | None:
    """
    Sends the message with user's prompt to OpenAI API and returns parsed message.

    :param client: OpenAI API client
    :type client: OpenAI
    :param model: ChatGPT's model (ex. gpt-4o)
    :type model: str
    :param prompt: Prompt for api from user
    :type prompt: str
    :param system_role_content: Content of system role in completion definition
    :type prompt: str
    :return: Message from openAI API containing the answer or None if error
    :rtype: str | None
    """
    model_check = True if model in ALLOWED_GPT_MODELS else False
    prompt_check = True if prompt != '' else False
    system_role_check = True if system_role_content != '' else False
    if not model_check and not prompt_check and not system_role_check:
        print("Validation Error -> Values cannot be empty")
        return None
    try:
        completion = api_client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": system_role_content,
                },
                {"role": "user", "content": prompt},
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(e)


def write_content_to_file(path: str, content: str) -> None:
    """
    Write content to specified file

    :param path: Path to target file
    :type path: str
    :param content: Content that should be placed in a file
    :type content: str
    :return: Function will return None
    :rtype: None
    """
    content_check = True if content != '' else False
    if not content_check:
        return None
    with open(path, 'w', encoding='utf-8') as write_file:
        try:
            write_file.write(content)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    CONTENT_FILE_PATH = "./plik.txt"
    TARGET_ARTICLE_FILE_PATH = "./artykul.html"
    file_content = get_file_content(CONTENT_FILE_PATH)
    system_role = "You are a proffessional HTML creator. Your job is to create good tags and images to from my file."
    user_prompt = f"""
Transform the following text into an HTML structure that meets these guidelines:
- Use appropriate HTML tags to structure the content.
- Identify places where it would be appropriate to insert images and mark these spots using the <img> tag with the attribute src="image_placeholder.jpg". Add an alt attribute to each image with a detailed prompt that can be used to generate an image.
- Place captions below the images using the appropriate HTML tags.
- Do not add any CSS or JavaScript. The code should only contain content to be inserted between the <body> and </body> tags. Do not include <html>, <head>, or <body> tags.
- Please remember to skip any formatting addtions from generating. No html addition at top and any other additional chars. Generate only ready to use content for html file

Text to transform:
{file_content}
"""
    html_content = get_result_from_api(client, 'gpt-4o', user_prompt, system_role)
    write_content_to_file(TARGET_ARTICLE_FILE_PATH, html_content)
