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
from ..helpers import common_utils as cu

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


def generate_and_format(question_type, keywords):
    raw_response = generate_mock_mcq(question_type, keywords)
    return raw_response


iface = gr.Interface(
    fn=generate_and_format,
    inputs=[
        gr.Dropdown(
            choices=["Single Statement", "Two Statements", "Three Statements", "Match the Pairs", "Identify Features"],
            label="Question Type"
        ),
        gr.Textbox(label="Keywords/Topics (comma-separated)"),
    ],
    outputs=gr.Code(label="Generated MCQ"),
    title="Mock MCQ Generator (UPSC Style)",
    description="Generate UPSC-style multiple-choice questions based on the selected question type and provided keywords using Gemini-2.0-flash.",
)

iface.launch()