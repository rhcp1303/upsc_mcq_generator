three_statements_question_prompt = """

**Prompt:**

**Instructions:**

    Create one UPSC style two-statement type multiple choice questions using the following topics:
    
    Topics: {topics}
    
    with 4 options (only 1 correct) while adhering to the following criteria:

1.  **Question Type:** 

    Only 3 forms:
    
    1. 	Starting with the words "Consider the following statements" followed by 3 related statements. The final statement 
        should be "Which of the statements given above is/are correct?" :

    	*Example*

   		Q.55) 
   		With reference to the role of biofilters in Recirculating Aquaculture System, consider the following statements:
        1. Biofilters provide waste treatment by removing uneaten fish feed.
        2. Biofilters convert ammonia present in fish waste to nitrate.
        3. Biofilters increase phosphorus as nutrient for fish in water.
        How many of the statements given above are correct?
        (a) Only one
        (b) Only two
        (c) All three
        (d) None

    2. 	Starting with the words "With reference to Indian History, consider the following statements" followed by 3 related 
        statements. The final statement should be "Which of the statements given above is/are correct?" :

        *Example*

		Q.59) 
		With reference to Indian history, consider the following statements:
        1. The Dutch established their factories/warehouses on the east coast on lands granted to them by Gajapati rulers.
        2. Alfonso de Albuquerque captured Goa from the Bijapur Sultanate.
        3. The English East India Company established a factory at Madras on a plot of land leased from a representative of the Vijayanagara empire.
        Which of the statements given above are correct?
        (a) 1 and 2 only
        (b) 2 and 3 only
        (c) 1 and 3 only
        (d) 1, 2 and 3



    3. 	Starting with the words "With reference to (a specific subject of the question), consider the following statements" 
        followed by 3 related statements. The final statement should be "Which of the statements given above is/are correct?":

	    *Example*

		Q.4) 
		Consider the following statements about 'the Charter Act of 1813':
        1. It ended the trade monopoly of the East India Company in India except for trade in tea and trade with China.
        2. It asserted the sovereignty of the British Crown over the Indian territories held by the Company.
        3. The revenues of India were now controlled by the British Parliament.
        Which of the statements given above are correct?
        (a) 1 and 2 only
        (b) 2 and 3 only
        (c) 1 and 3 only
        (d) 1, 2 and 3


2.  **Options*
    4 options with the following two forms only:
    
    *   Form 1:
    
    (a) 1 and 2 only
    (b) 2 and 3 only
    (c) 1 and 3 only
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
    "statements": [
        "(Statement 1 without enumerator)",
        "(Statement 2 without enumerator)",
        "(Statement 3 without enumerator)"
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
    "question": "Consider the following statements:",
    "statements": [
        "In the revenue administration of Delhi Sultanate, the in-charge of revenue collection was known as 'Amil'.",
        "The Iqta system of Sultans of Delhi was an ancient indigenous institution.",
        "The office of 'Mir Bakshi' came into existence during the reign of Khalji Sultans of Delhi."
    ],
    "final_statement": "Which of the statements given above is/are correct?",
    "choices": [
        "1 only",
        "1 and 2 only",
        "3 only",
        "1, 2 and 3"
    ],
    "correct_answer": "a",
    "explanation": "Amils were officers deputed to collect revenue\\nduring the sultanate era in North India. Mir\\nBakshi, on the other hand, was a Mughal high\\noffice in charge of military pay and accounts.\\nIqta system of land control was introduced in\\nIndia by the Delhi sultans. It was originally of\\nCentral Asian and West Asian origin."
}}

 
 
**Note:**

* Avoid mentioning any information related to the prompt,query, source_content, target_content,  input text, input document, 
  LLM, LangChain, or vector embeddings used in the generation process.
* Present the output in a clear, organized, and user-friendly format.
* Do not use * in response text. Just give plain text.


"""