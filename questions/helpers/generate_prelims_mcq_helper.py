import json
import gradio as gr
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from ..helpers.prompt_helpers.single_statement_question_prompt_helper import \
    single_statement_question_prompt
from ..helpers.prompt_helpers.two_statements_question_prompt_helper import \
    two_statements_question_prompt
from ..helpers.prompt_helpers.three_statements_question_prompt_helper import \
    three_statements_question_prompt
from ..helpers.prompt_helpers.identify_features_question_prompt_helper import \
    identify_features_question_prompt
from ..helpers.prompt_helpers.match_the_pairs_question_prompt_helper import \
    match_the_pairs_prompt
from ..helpers.common_utils import SubjectCode, QuestionContentType

os.environ["TOKENIZERS_PARALLELISM"] = "false"

api_key_1 = "AIzaSyCxTCYQO7s23L33kC4Io4G-i1p1ytD-OiI"
api_key_2 = "AIzaSyC_w68KVtMCloF5V3NKAUBp6EdhqcA0ylw"
api_key_3 = "AIzaSyAA39dIq31iDJR-i7mZRWEKhkVVIr1Bz4g"
api_key_4 = "AIzaSyD0nx9rH7HhQZDpJrY0hOaOR9Xok4r-liM"
api_key_5 = "AIzaSyBq2_GdMf0KhowSVSb0hn4Z_8B81kBewXY"


def generate_mock_mcq(question_type, keywords):
    if question_type == "Single Statement":
        prompt = single_statement_question_prompt
        api_key = api_key_1
    elif question_type == "Two Statements":
        prompt = two_statements_question_prompt
        api_key = api_key_2
    elif question_type == "Three Statements":
        prompt = three_statements_question_prompt
        api_key = api_key_3
    elif question_type == "Match the Pairs":
        prompt = match_the_pairs_prompt
        api_key = api_key_4
    elif question_type == "Identify Features":
        prompt = identify_features_question_prompt
        api_key = api_key_5
    else:
        return "Invalid question type"

    query = prompt.format(topics=keywords)
    os.environ["GOOGLE_API_KEY"] = api_key
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    response = llm.invoke(query).content
    return response


def generate_and_format(question_type, keywords, subject, question_content_type):
    raw_response = generate_mock_mcq(question_type, keywords)
    cleaned_json = raw_response.replace("```json", "").replace("```", "")
    print("cleaned json response: \n" + cleaned_json)
    try:
        parsed_json = json.loads(cleaned_json)
        parsed_json["subject"] = subject
        parsed_json["question_content_type"] = question_content_type
        return parsed_json
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return {"error": "Failed to parse JSON response."}


def save_json_to_file(json_output):
    if json_output and "error" not in json_output:
        try:
            data_to_save = {"en": json_output}
            with open("temp/mcq_output.json", "a") as f:
                json.dump(data_to_save, f, indent=4)
                f.write(',\n')
            return "JSON output appended to mcq_output.json"
        except Exception as e:
            return f"Error saving JSON: {e}"
    else:
        return "No valid JSON output to save."


css = """
#output_box {
    width: 100% !important; /* Adjust percentage as needed */
    min-height: 300px; /* Adjust minimum height as needed */
    max-height: 600px; /* Adjust maximum height as needed */
    overflow-y: auto; /* Enable vertical scrolling if content overflows */
    overflow-x: hidden !important; /* Prevent horizontal scrolling */
    white-space: pre-wrap !important; /* Preserve whitespace and line breaks, wrap text */
    word-break: break-word !important; /* Force long words to break */
}
"""

with gr.Blocks(css=css) as iface:
    gr.Markdown("# Mock MCQ Generator (UPSC Style)")
    with gr.Row():
        subject_dropdown = gr.Dropdown(
            choices=[subject.name for subject in SubjectCode],
            label="Subject"
        )
        question_content_type_dropdown = gr.Dropdown(
            choices=[content_type.name for content_type in QuestionContentType],
            label="Question Content Type"
        )
    with gr.Row():
        question_type_dropdown = gr.Dropdown(
            choices=["Single Statement", "Two Statements", "Three Statements", "Match the Pairs", "Identify Features"],
            label="Question Type"
        )
        keywords_textbox = gr.Textbox(label="Keywords/Topics (comma-separated)")
    output_json = gr.JSON(label="Generated MCQ", elem_id="output_box")
    with gr.Row():
        generate_button = gr.Button("Generate MCQ")
        save_button = gr.Button("Save JSON to File")
    save_status = gr.Textbox(label="Save Status")

    generate_button.click(
        fn=generate_and_format,
        inputs=[question_type_dropdown, keywords_textbox, subject_dropdown, question_content_type_dropdown],
        outputs=output_json
    )

    save_button.click(
        fn=save_json_to_file,
        inputs=[output_json],
        outputs=save_status
    )

iface.launch()
