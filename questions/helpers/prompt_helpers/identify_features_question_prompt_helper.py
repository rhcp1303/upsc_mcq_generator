identify_features_question_prompt = """

**Prompt:**

**Instructions:**

    Create one UPSC style two-statement type multiple choice questions using the following topics:
    
    Topics: {topics}
    
    with 4 options (only 1 correct) while adhering to the following criteria:


1.  **Question Text:** 

    Only 1 form:
    
    1. 	Starting with the words "Consider the following" or " Consider the following (objects of same categories):" followed 
        by 4,5 or 6 related features/elements. The final statement should be asking a question based on counting or identifying something :

   	    *Example*

   	    Q.3) 
   	    Consider the following:
        1. Pyroclastic debris
        2. Ash and dust
        3. Nitrogen compounds
        4. Sulphur compounds
        How many of the above are products of volcanic eruptions?
        (a) Only one
        (b) Only two
        (c) Only three
        (d) All four
        
        Q.7)
        Consider the following:
        1. Foreign currency convertible bonds
        2. Foreign institutional investment with certain conditions
        3. Global depository receipts
        4. Non-resident external deposits
        Which of the above can be included in Foreign Direct Investments?
        (a) 1, 2 and 3
        (b) 3 only
        (c) 2 and 4
        (d) 1 and 4
 
2.  **Options*
    4 options in the following two forms:
    
    *   Form 1:
    
    (a) 1, 2 and 3
    (b) 3 only
    (c) 2 and 4
    (d) 1 and 4

    *   Form 2:
    
    (a) Only one
    (b) Only two
    (c) All three
    (d) None

    * Set options as per the requirement of the question (above are only examples not the strict template to be followed.)

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
        "(Statement 3 without enumerator)",
        "(Statement 4 without enumerator)",
        "(Statement 5 without enumerator)",
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
    "question": "Consider the following:",
    "statements": [
        "Foreign currency convertible bonds",
        "Foreign institutional investment with certain conditions",
        "Global depository receipts",
        "Non-resident external deposits"
    ],
    "final_statement": "Which of the above can be included in Foreign Direct Investments?",
    "choices": [
        "1, 2 and 3",
        "3 only",
        "2 and 4",
        "1 and 4"
    ],
    "correct_answer": "a",
    "explanation": "Foreign Currency Convertible Bonds (FCCB) means a bond issued by an Indian\\ncompany in foreign currency and subscribed by a non-resident in foreign currency and convertible\\ninto ordinary shares of the issuing company, either in whole or in part. FCCBs represent a debt\\nobligation of the corporate. Investors have the option to redeem; or to convert them into underlying\\nlocal shares or global depository receipts. If investors prefer to hold the FCCBs until redemption date,\\nthe corporate has to redeem the FCCBs on redemption date. Dilution would take place as and when\\ndebt is converted into equity. Since these bonds are convertible in to equity shares over a period of\\ntime as provided in the instrument, therefore they are covered under FDI policy & counted towards\\nFDI. [If they are redeemed they count as ECB & a debt obligation, only on converting into equity it is\\ncounted towards FDI]. So, 1 is correct.\\nFII with certain conditions - According to IMF and OECD definitions, the acquisition of at least ten\\npercent of the ordinary shares or voting power in a public or private enterprise by non-resident\\ninvestors makes it eligible to be categorized as foreign direct investment (FDI).In India, as per SEBI\\n(FPI regulations), 2019, a particular FII is allowed to invest upto 10% of the paid up capital of a\\ncompany, which implies that any investment above 10% will be construed as FDI. So, 2 is correct.\\nGlobal Depository Receipt (GDR) - Global Depository Receipts means any instrument issued in the\\nform of depository receipt or certificate created by the oversees depository bank outside India and\\nissued to non-resident investors against underlying shares or foreign currency convertible bonds of\\nissuing company. GDRs are equity representing share-holders funds, foreign investment in the form\\nof equity shares issued outside India by a Depository Bank, on behalf of an Indian company which is\\ncovered under the FDI policy. GDR proceeds are reckoned as Foreign Direct Investment. So, 3 is\\ncorrect.\\nNon-resident external deposits - NRI investments that are repatriable are considered FDI while non-repatriable investments are considered domestic investment. So, 4 is not correct\\nTherefore, the correct answer is (a)."
}}


**Note:**

* Avoid mentioning any information related to the prompt,query, source_content, target_content,  input text, input document, 
  LLM, LangChain, or vector embeddings used in the generation process.
* Present the output in a clear, organized, and user-friendly format.
* Do not use * in response text. Just give plain text.


"""