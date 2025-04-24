two_statements_question_prompt = """

**Prompt:**

**Instructions:**

    Create one UPSC style two-statement type multiple choice questions using the following topics:
    
    Topics: {topics}
    
    with 4 options (only 1 correct) while adhering to the following criteria:


1.  **Question Type:** 

    Only 3 forms:
    
    1. 	Starting with the words "Consider the following statements" followed by 2 related statements out of which only 4 
        possibilities are there as shown in the options in the following example. The final statement should be "Which of the 
        statements given above is/are correct?" :

   	    *Example*

   		Q.58)
   		Consider the following statements:
		1. In the tropical zone, the western sections of the oceans are warmer than the eastern sections owing to the influence of trade winds.
		2. In the temperate zone, westerlies make the eastern sections of oceans warmer than the western sections.
		Which of the statements given above is/are correct?
		(a) 1 only
		(b) 2 only
		(c) Both 1 and 2
		(d) Neither 1 nor 2

    2. 	Starting with the words "With reference to Indian History, consider the following statements" followed by 2 related 
        statements out of which only 4 possiblities are there as shown in the options in the following example. The final 
        statement should be "Which of the statements given above is/are correct?" :

        *Example*

		Q.59) 
		With reference to Indian history, consider the following statements:
		1. The Dutch established their factories/warehouses on the east coast on lands granted to them by Gajapati rulers.
		2. Alfonso de Albuquerque captured Goa from the Bijapur Sultanate.
		Which of the statements given above are correct?
		(a) 1 only
		(b) 2 only
		(c) Both 1 and 2
		(d) Neither 1 nor 2


    3. 	Starting with the words "With reference to (a specific subject of the question), consider the following statements" followed by 2 related statements out of 
	    which only 4 possiblities are there as shown in the options in the following example. The final statement should be "Which of the statements given above is/are correct?":

	    *Example*

		Q.10)
		With reference to Swadeshi Movement, consider the following statements:
		1. It contributed to the revival of the indigenous artisan crafts and industries.
		2. The National Council of Education was established as a part of Swadeshi Movement.
		Which of the statements given above is/are correct?
		(a) 1 only
		(b) 2 only
		(c) Both 1 and 2
		(d) Neither 1 nor 2

    
2.  **Options*
    4 options with the following forms only and strictly:
    (a) 1 only
    (b) 2 only
    (c) Both 1 and 2
    (d) Neither 1 nor 2

3.    **Cognitive Skills:** 

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
        "(Statement 2 without enumerator)"
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
    "question": "With reference to the proposals of Cripps Mission, consider the following statements:",

    "statements": [
        "The Constituent Assembly would have members nominated by the Provincial Assemblies as well as the Princely States.",
        "Any Province, which is not prepared to accept the new Constitution would have the right to sign a separate agreement with Britain regarding its future status."
    ],
    "final_statement": "Which of the statements given above is/are correct?",
    "choices": [
        "1 only",
        "2 only",
        "Both 1 and 2",
        "Neither 1 nor 2"
    ],
    "correct_answer": "b",
    "explanation": "● In March 1942, a mission headed by Stafford Cripps was sent to India with constitutional proposals to seek Indian support for the war. \\n● It proposed that the Constituent Assembly was to be composed of elected (and not\\nnominated) members from provinces. Only the section representing the Princely states was\\nto be nominated. So, statement 1 is not correct.\\n● It also stated that if any Province which is not prepared to accept the new Constitution would\\n have the right to sign a separate agreement with Britain regarding its future status. This \\n became the primary reason for the failure of the Cripps mission as this provision allowed for \\n balkanization of India. So, statement 2 is correct."
}}

{{
    "question": "Consider the following statements:",
    "statements": [
        "The Montagu-Chelmsford Reforms of 1919 recommended granting voting rights to all the women above the age of 21.",
        "The Government of India Act of 1935 gave women reserved seats in the legislature."
    ],
    "final_statement": "Which of the statements given above is/are correct?",
    "choices": [
        "1 only",
        "2 only",
        "Both 1 and 2",
        "Neither 1 nor 2"
    ],
    "correct_answer": "d",
    "explanation": "Statement 1 is incorrect. The Montague Chelmsford reforms of 1919 did not recommend granting voting rights to all women above the age of 21. Although it recommended the voting rights to women in limited numbers to be extended on the basis of property, tax or education.\n\nStatement 2 is incorrect. The Government of India Act 1935 gave women separate electorate (and did not reserved seats for women in legislature). It provided separate electorates to depressed classes and labours also."
}}


**Note:**

* Avoid mentioning any information related to the prompt,query, source_content, target_content,  input text, input document, 
  LLM, LangChain, or vector embeddings used in the generation process.
* Present the output in a clear, organized, and user-friendly format.
* Do not use * in response text. Just give plain text.

"""
