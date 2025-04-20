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

**Example Response Required:**

Q.12) 
Consider the following statements:
1. In the revenue administration of Delhi Sultanate, the in-charge of revenue collection was known as 'Amil'.
2. The Iqta system of Sultans of Delhi was an ancient indigenous institution.
3. The office of 'Mir Bakshi' came into existence during the reign of Khalji Sultans of Delhi.
Which of the statements given above is/are correct?
(a) 1 only
(b) 1 and 2 only
(c) 3 only
(d) 1, 2 and 3

Correct Answer: (a)

Explanation:

Amils were officers deputed to collect revenue
during the sultanate era in North India. Mir
Bakshi, on the other hand, was a Mughal high
office in charge of military pay and accounts.
Iqta system of land control was introduced in
India by the Delhi sultans. It was originally of
Central Asian and West Asian origin. 


**Note:**

* Avoid mentioning any information related to the prompt,query, source_content, target_content,  input text, input document, 
  LLM, LangChain, or vector embeddings used in the generation process.
* Present the output in a clear, organized, and user-friendly format.
* Do not use * in response text. Just give plain text.


"""