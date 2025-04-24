match_the_pairs_prompt = """

**Prompt:**

**Instructions:**

    Create one UPSC style two-statement type multiple choice questions using the following topics:
    
    Topics: {topics}
    
    with 4 options (only 1 correct) while adhering to the following criteria:


1.  **Question Type:** 

    Only 1 form:

    1. 	Starting with the words "Consider the following pairs" or "With reference to (topic of the question), consider the following pairs" 
        followed by 3 to 6 pairs. The final statement should be "Which of the pairs given above is/are correctly matched?" :

   	    *Example*

   		Q.15) 
   		With reference to Indian National Movement, consider the following pairs: 
   		
            Person                       Position held
        1.  Sir Tej Bahadur Sapru    :   President, All India Liberal Federation
        2.  K. C. Neogy              :   Member, The Constituent Assembly
        3.  P. C. Joshi              :   General Secretary, Communist Party of India
        Which of the pairs given above is/are correctly matched?
        (a) 1 only
        (b) 1 and 2 only
        (c) 3 only
        (d) 1, 2 and 3


2.  **Options*

    4 options with the following two forms only:
    
    *   Form 1:
    (a) 1 only
    (b) 1 and 2 only
    (c) 2 and 3 only
    (d) 1, 2 and 3


    *   Form 2:
    (a) Only one
    (b) Only two
    (c) All three
    (d) None

3.  **Cognitive Skills:** 

    Each question should assess one or more of the following cognitive skills:

    * Factual recall
    * Analysis
    * Evaluation
    * Conceptual understanding
    * Application
    * Interdisciplinary linkage understanding

4. **Difficulty Level:**

    * Create only difficult questions with the possibilities being : 'easy', 'moderate', and 'difficult'.
    * Difficulty can be achieved by:
    * Demanding accurate conceptual understanding.
    * Requiring recall of lesser-known but significant facts.
    * Including plausible distractors that are close to the correct answer.
    * Setting options that are closely related, making elimination difficult.

5. **Question Quality:**

    * Avoid vague, unclear, and obvious statements in the questions.
    * Avoid asking generic question which doesnt pinpoint to a specific concept or precise information
    
6. **Correct Answer:** 

    *Clearly indicate the correct option (a, b, c, or d).
    
7. **Explanation:**

    * Provide a detailed explanation for the correct answer (minimum 500 words).
    * Incorporate key UPSC-relevant points and perspectives in the explanation.



**Output Format:**

Return the generated question as a JSON object without any backtick (don't add ```json) in the following format:

{{
    "question": "(Generated Question Text - only the introduction statement)",
    "headings": ["(Heading 1)","(Heading 2)"],
    
    "pairs": [
        ["(Element 1)","(Element 2)"],
        ["(Element 1)","(Element 2)"],
        ["(Element 1)","(Element 2)"],
        ["(Element 1)","(Element 2)"],
        ["(Element 1)","(Element 2)"]
    ],
    "final_statement": "(Final statement of the question)",
    "choices": [
        "Choice 1 without enumerator",
        "Choice 2 without enumerator",
        "Choice 3 without enumerator",
        "Choice 4 without enumerator"
    ],
    "correct_answer": "(Correct Option - a, b, c, or d)",
    "explanation": "(Detailed Explanation with escaped special characters and \\n for newlines)"
}}


**Example Response Required:**

{{
    "question": "Consider the following pairs:",
    "headings": ["Movement","Organization Leader"],
    
    "pairs": [
        ["All India Anti-Untouchability League","Mahatma Gandhi"],
        ["All India Kisan Sabha","Swami Sahajanand Saraswati"],
        ["Self-Respect Movement","E. V. Ramaswami Naicker"]
    ],
    "final_statement": "Which of the pairs given above is/are correctly matched?",
    "choices": [
        "1 only",
        "1 and 2 only",
        "2 and 3 only",
        "1, 2 and 3"
    ],
    "correct_answer": "d",
    "explanation": "Gandhi set up All India Anti-Untouchability \\nLeague in September 1932. (Spectrum Page\\n438).\\nThe All India Kisan Sabha was founded in\\nLucknow in April 1936 With Swami Sahjananda\\nSaraswati as the president. (Spectrum Page\\n652).\\nSelf-Respect Movement emerged in South\\nIndia under the leadership of E Ramaswamy\\nNaicker"

}}


**Note:**

* Avoid mentioning any information related to the prompt,query, source_content, target_content,  input text, input document, 
  LLM, LangChain, or vector embeddings used in the generation process.
* Present the output in a clear, organized, and user-friendly format.
* Do not use * in response text. Just give plain text.


"""
