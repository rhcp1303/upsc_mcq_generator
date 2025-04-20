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

8. **Presentation**

    *   Align the pairs properly with tabs, spaces and indentations such that 

        Example
        *1. Consider the following pairs:**

               Act                                          Prominent Feature
            1. Regulating Act of 1773                   :   Established a Supreme Court at Calcutta
            2. Amending Act of 1781                     :   Exempted revenue matters from Supreme Court jurisdiction
            3. Pitt's India Act of 1784                 :   Created the Board of Control
            4. Charter Act of 1833                      :   Made the Governor-General of Bengal the Governor-General of India

            Which of the pairs given above is/are correctly matched?
            (a) 1 only
            (b) 1, 2, and 3 only
            (c) 1, 2, 3, and 4
            (d) 2 and 4 only



**Example Response Required:**

Q.6) 
Consider the following pairs:
   Movement                                     Organization Leader
1. All India Anti-Untouchability League   :     Mahatma Gandhi
2. All India Kisan Sabha                  :     Swami Sahajanand Saraswati
3. Self-Respect Movement                  :     E. V. Ramaswami Naicker
Which of the pairs given above is/are correctly matched?
(a) 1 only
(b) 1 and 2 only
(c) 2 and 3 only
(d) 1, 2 and 3

Correct Answer: (d)

Explanation:

Gandhi set up All India Anti-Untouchability
League in September 1932. (Spectrum Page
438).
The All India Kisan Sabha was founded in
Lucknow in April 1936 With Swami Sahjananda
Saraswati as the president. (Spectrum Page
652).
Self-Respect Movement emerged in South
India under the leadership of E Ramaswamy
Naicker

**Note:**

* Avoid mentioning any information related to the prompt,query, source_content, target_content,  input text, input document, 
  LLM, LangChain, or vector embeddings used in the generation process.
* Present the output in a clear, organized, and user-friendly format.
* Do not use * in response text. Just give plain text.


"""
