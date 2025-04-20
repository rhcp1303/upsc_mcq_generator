single_statement_question_prompt = """

**Prompt:**

**Instructions:**
    Create one UPSC style single-statement type multiple choice questions using the following topics:
    
    Topics: {topics}
    
    with 4 options (only 1 correct) while adhering to the following criteria:
    
1. **Question Type:** 

    Only a single statement or a small passage asking the question.


2. **Cognitive Skills:** 

    Each question should assess one or more of the following cognitive skills:

    * Factual recall
    * Analysis
    * Evaluation
    * Conceptual understanding
    * Application
    * Interdisciplinary linkage understanding

3. **Difficulty Level:**

    * Create only difficult questions with the possibilities being : 'easy', 'moderate', and 'difficult'.
    * Difficulty can be achieved by:
    * Demanding accurate conceptual understanding.
    * Requiring recall of lesser-known but significant facts.
    * Including plausible distractors that are close to the correct answer.
    * Setting options that are closely related, making elimination difficult.

4. **Question Quality:**

    * Avoid vague, unclear, and obvious statements in the questions.
    * Avoid asking generic question which doesnt pinpoint to a specific concept or precise information
    
5. **Correct Answer:** 

    *Clearly indicate the correct option (a, b, c, or d).
    
6. **Explanation:**
    * Provide a detailed explanation for the correct answer (minimum 500 words).
    * Incorporate key UPSC-relevant points and perspectives in the explanation.

    

**Example Response:**

Q.1)
Which of the following statements about the Indian National Congress is correct?

(a) It was founded primarily by Indian businessmen.
(b) Its initial focus was on social reforms rather than political independence.
(c) Mahatma Gandhi led the Congress from its inception.
(d) It was founded in 1885 in Kolkata.


Correct Answer: (d)

Explanation:

The Indian National Congress was founded on December 28, 1885, in Kolkata (then Calcutta). While some businessmen were involved, the Congress also included intellectuals, lawyers, and social reformers. The initial focus was on moderate reforms within the British system. Mahatma Gandhi joined the Congress later in his life and became a prominent leader.

Q.2) 
Which of the following events marked a turning point in the Indian National Congress's approach towards achieving independence?

(a) The Surat Split of 1907
(b) The Lucknow Pact of 1916
(c) The Non-Cooperation Movement of 1920
(d) The Poona Pact of 1932

Correct Answer: (c)

Explanation:

The Non-Cooperation Movement, launched in 1920 under Gandhi's leadership, marked a significant shift in the Congress's approach. It moved away from moderate reforms and embraced mass civil disobedience, marking a more assertive and radical phase in the struggle for independence.


**Note:**

* Avoid mentioning any information related to the prompt,query, source_content, target_content,  input text, input document, 
  LLM, LangChain, or vector embeddings used in the generation process.
* Present the output in a clear, organized, and user-friendly format.
* Do not use * in response text. Just give plain text.



"""