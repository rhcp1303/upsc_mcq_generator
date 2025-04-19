assertion_reasoning_question_prompt = """

**Prompt:**

**Instructions:**

    Create unique UPSC style two-statement type multiple choice questions using the following topics:
    
    Topics: {topics}
    
    with 4 options (only 1 correct) while adhering to the following criteria:


2.  **Question Type:** 

    Only 1 form:

    1. 	Starting with the words "Consider the following statements" followed by 2 related statements out of which only 4 
        possiblities are there as shown in the options in the following example. The final statement should be " Which one of the following is correct in respect of the above statements?" :

   	    *Example*

   		Q.58) 
   		Consider the following statements:
   		Statement-I  : In the post-pandemic recent past, many Central Banks worldwide had carried out interest rate hikes.
   		Statement-II : Central Banks generally assume that they have the ability to counteract the rising consumer prices via monetary policy means.
   		Which one of the following is correct in respect of the above statements?
   		(a) Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I
   		(b) Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I
   		(c) Statement-I is correct but Statement-II is incorrect
        (d) Statement-I is incorrect but Statement-II is correct


2.  **Options*
    4 options with the following forms only and strictly:
    (a) Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I
    (b) Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I
    (c) Statement-I is correct but Statement-II is incorrect
    (d) Statement-I is incorrect but Statement-II is correct

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

    * Provide a detailed explanation for the correct answer (minimum 100 words).
    * Analyze the correct option and explain why it is the most appropriate.
    * Discuss why the other options are incorrect, highlighting potential misconceptions or distractors.
    * Incorporate key UPSC-relevant points and perspectives in the explanation.


**Example Response Required:**

1.Consider the following statements:
Statement-I  : In the post-pandemic recent past, many Central Banks worldwide had carried out interest rate hikes.
Statement-II : Central Banks generally assume that they have the ability to counteract the rising consumer prices via monetary policy means.
Which one of the following is correct in respect of the above statements?
(a) Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I
(b) Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I
(c) Statement-I is correct but Statement-II is incorrect
(d) Statement-I is incorrect but Statement-II is correct

Correct Answer: (a)

Explanation:

● Many Central banks worldwide have carried out interest rate hikes in the post-pandemic recent past to try
and tackle rising inflation. For example, the Reserve Bank of India raised the repo rate by 40 basis points
to 4.4% in May 2022, the US Federal Reserve raised interest rates by 0.25 percentage points in February
2023, and the UK raised rates for the 10th month in a row in February 2023. So, statement 1 is correct.
● Central Banks assume that they have the ability to counteract the rising consumer prices via monetary
policy means because they have the power to control the money supply in the economy through various
tools. For example, they can adjust interest rates, which can influence borrowing and spending decisions
by consumers and businesses and, by extension, affect the supply of money in circulation.
» When the Central Bank raises interest rates, it becomes more expensive for consumers and
businesses to borrow money, which in turn reduces their spending and slows down the economy.
The monetary policy transmission mechanism can help reduce inflation. This can cause
inflation to decrease, as less money is chasing the same amount of goods and services. On the other
hand, if the Central Bank lowers interest rates, it becomes cheaper for consumers and businesses
to borrow money, which can stimulate spending and economic growth but may also lead to higher
inflation if the supply of money increases faster than the supply of goods and services.
» Monetary policy measures are often used by Central Banks as a tool to maintain price stability
and promote economic growth. This is known as inflation targeting by the Central Banks. This is
because high and volatile inflation can adversely affect the economy by reducing the purchasing
power of consumers and making it harder for businesses to plan and invest for the long term. By
maintaining price stability, the Central Bank can create a conducive environment for businesses
to thrive and support the overall health of the economy.
» So, Central Banks assume that they have the ability to counteract the rising consumer prices via
monetary policy means because they have the power to control the money supply and influence
the borrowing and spending decisions of consumers and businesses. By using monetary policy
tools such as interest rates, they can maintain price stability, promote economic growth, and
support the overall health of the economy.
» So, statement II is correct and it provides a reason for the interest rate hikes mentioned in
Statement-I.
Therefore, option (a) is the correct answer

**Note:**

* Avoid mentioning any information related to the prompt,query, source_content, target_content,  input text, input document, 
  LLM, LangChain, or vector embeddings used in the generation process.
* Present the output in a clear, organized, and user-friendly format.

"""
