def create_latex_template(questions):
    """Generates the main LaTeX template using multicols."""

    latex_template = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[margin=0.7in]{geometry}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{enumitem}
\usepackage{multicol}
\usepackage{ragged2e}
\usepackage{needspace}
\usepackage{array} % For better table control
\usepackage{tabularx} % For auto-width tables
\usepackage{fontsize} % For setting font size
\usepackage[none]{hyphenat} % Disable hyphenation


\begin{document}

\begin{multicols}{2}[\setlength{\columnsep}{0.5in}] % Increased column separation
\RaggedRight

\begin{enumerate}[label=\textbf{Q.\arabic*.}, itemsep=0.1in]
"""

    for q in questions:
        latex_template += r"\item\needspace{2\baselineskip} " + q['en']['question'] + r"\\"

        # Handle "Match the pairs"
        if 'pairs' in q['en']:
            if 'headings' in q['en']:
                latex_template += r"\begin{center}\fontsize{9pt}{11pt}\selectfont" + "\n"
                latex_template += r"\setlength\tabcolsep{15pt} % Increase horizontal space between columns" + "\n"
                latex_template += r"\begin{tabularx}{\linewidth}{>{\RaggedRight\arraybackslash}p{0.45\linewidth} >{\RaggedRight\arraybackslash}p{0.45\linewidth}}" + "\n"
                latex_template += r"\textbf{" + q['en']['headings'][0] + r"} & \textbf{" + q['en']['headings'][
                    1] + r"} \\ \hline\\[0.2cm]" + "\n"
                for i, pair in enumerate(q['en']['pairs']):
                    latex_template += numbered_pair_to_latex(pair, number=str(i + 1) + ".")
                    if i < len(q['en']['pairs']) - 1:
                        latex_template += r"\\[0.3\baselineskip]" + "\n"
                latex_template += r"\end{tabularx}\end{center}\normalsize" + "\n"
                latex_template += r"\setlength\tabcolsep{6pt} % Restore default column separation" + "\n"
            else:
                latex_template += r"\begin{enumerate}[label=\arabic*., leftmargin=0.6cm, itemsep=0in]" + "\n"
                for i, pair in enumerate(q['en']['pairs']):
                    latex_template += r"\item " + str(i + 1) + ". " + pair[0] + r" : " + pair[1] + r""
                    if i < len(q['en']['pairs']) - 1:
                        latex_template += r"\vspace{0.3\baselineskip}"
                    latex_template += r"\n"
                latex_template += r"\end{enumerate}" + "\n"

        elif 'statements' in q['en']:  # Handle statements
            latex_template += r"\begin{enumerate}[label=\arabic*., leftmargin=0.6cm, itemsep=0in]" + "\n"
            for s in q['en']['statements']:
                latex_template += r"\item " + s + r"" + "\n"
            latex_template += r"\end{enumerate}" + "\n"
            if 'final_statement' in q['en']:
                latex_template += q['en']['final_statement'] + r"\\" + "\n"

        if 'choices' in q['en']:  # Handle multiple choices
            latex_template += r"\begin{enumerate}[label=(\alph*), leftmargin=0.4cm, itemsep=0in]" + "\n"
            for choice in q['en']['choices']:
                latex_template += r"\item " + choice + r"" + "\n"
            latex_template += r"\end{enumerate}" + "\n"

        latex_template += r"\vspace{0.1in}" + "\n"

    latex_template += r"""
\end{enumerate}

\end{multicols}

\end{document}
"""
    return latex_template


def numbered_pair_to_latex(pair, number=""):
    """Formats a numbered pair for LaTeX table with hanging indentation for line breaks."""
    indent_length = "2em"  # Adjust this value as needed for the width of the number
    return r"\makebox[" + indent_length + r"][l]{" + number + r"}\RaggedRight\arraybackslash \hangindent=" + indent_length + r" " + \
        pair[0] + r" & \RaggedRight\arraybackslash \hangindent=0pt " + pair[1] + r" \\" + "\n"


questions = [
    {
        "en": {
            "question": "With reference to Centre-State Relations, consider the following pairs:",
            "headings": ["Committee/Commission with very long text",
                         "Associated Recommendation that is also quite lengthy"],
            "pairs": [
                ["Sarkaria Commission with a slightly longer name",
                 "Permanent Inter-State Council under Article 263 which can also have more words"],
                ["Punchhi Commission",
                 "Regulation of deployment of Central Armed Forces in States to a significant extent"],
                ["Rajamannar Committee with an extended title",
                 "Abolition of All India Services and related matters that require more space"],
            ],
            "choices": [
                "1 only",
                "1 and 2 only",
                "2 and 3 only",
                "1, 2 and 3"
            ],
        },
    },
    {
        "en": {
            "question": "Consider the following statements regarding Centre-State financial relations in India:",
            "statements": [
                "The Finance Commission's recommendations on the distribution of tax revenues between the Union and the States are binding on the Union Government.",
                "Grants-in-aid under Article 275 of the Constitution are provided to States based solely on the recommendations of the Finance Commission.",
                "The Goods and Services Tax (GST) Council is empowered to make recommendations to the Union and the States on matters related to GST, but its decisions are non-binding in nature.",
            ],
            "choices": [
                "Only one",
                "Only two",
                "All three",
                "None"
            ],
        },
    },
    {
        "en": {
            "question": "The Sarkaria Commission's recommendations on Centre-State relations, while largely accepted, faced specific criticisms regarding their implementation and scope. Which of the following best encapsulates a significant critique of the post-Sarkaria Commission scenario?",
            "choices": [
                "The near-complete adoption of all recommendations led to an over-centralized system, diminishing state autonomy beyond what the Commission intended.",
                "The Commission's proposals for fiscal federalism were fully implemented, but the states lacked the administrative capacity to effectively utilize the increased resources.",
                "Despite some progress, the selective implementation of recommendations, particularly concerning the deployment of central forces in states, often bypassed the spirit of consultation and consensus advocated by the Commission.",
                "The establishment of the Inter-State Council, as recommended, became defunct due to the lack of political will from both the Centre and the states to address contentious issues.",
            ],
        },
    },
    {
        "en": {
            "question": "Consider the following statements regarding Centre-State financial relations in India:",
            "statements": [
                "The Finance Commission is a constitutional body primarily responsible for recommending the distribution of net proceeds of taxes between the Union and the States, and the principles that should govern the grants-in-aid of the revenues of the States out of the Consolidated Fund of India.",
                "Article 293 of the Constitution empowers the States to borrow only from the Union Government and prevents them from raising loans directly from the open market or other financial institutions.",
            ],
            "choices": [
                "1 only",
                "2 only",
                "Both 1 and 2",
                "Neither 1 nor 2",
            ],
        },
    },
    {
        "en": {
            "question": "Consider the following statements regarding the Sarkaria Commission:",
            "statements": [
                "1. It recommended the abolition of Article 356 of the Constitution, advocating for alternative mechanisms to address constitutional breakdowns in states.",
                "2. It suggested that the Governor should be an eminent person from outside the state, and should be detached from local politics of the state."
            ],
            "final_statement": "Which of the statements given above is/are correct?",
            "choices": [
                "(a) 1 only",
                "(b) 2 only",
                "(c) Both 1 and 2",
                "(d) Neither 1 nor 2"
            ],
            "correct_answer": "(b)",
            "explanation": "The Sarkaria Commission, established in 1983 to examine and review the working of the existing arrangements between the Union and the States, made several important recommendations to improve Centre-State relations. While the commission did address Article 356, it did not recommend its abolition. Instead, it advocated for its judicious use as a last resort, emphasizing that all other alternatives should be exhausted before invoking it. The commission laid down stringent guidelines for its application, suggesting that it should only be used in cases of demonstrable breakdown of constitutional machinery where the state government is unable to function according to the Constitution. It also suggested that a warning should be issued to the state government before resorting to Article 356 and that the reasons for its imposition should be communicated to the Parliament. Therefore, statement 1 is incorrect.\n\nRegarding the role of the Governor, the Sarkaria Commission made specific recommendations to ensure impartiality and effectiveness. It suggested that the Governor should be an eminent person from outside the state, possessing expertise in various fields. The commission emphasized that the Governor should be detached from local politics and should not have been an active politician in recent years. This recommendation aimed to ensure that the Governor acts as a neutral arbiter and upholds the Constitution without being influenced by local political considerations. The commission also highlighted the importance of consulting the Vice-President and the Speaker of the Lok Sabha when selecting a Governor. Therefore, statement 2 is correct.\n\nIn summary, the Sarkaria Commission's recommendations were aimed at fostering cooperative federalism and improving the overall efficiency of Centre-State relations. Its report has been a valuable resource for policymakers and academics in understanding the complexities of federal governance in India. The commission's emphasis on the judicious use of Article 356 and the importance of an impartial Governor reflects its commitment to upholding the principles of constitutionalism and federalism."
        }
    },
    {
        "en": {
            "question": "Consider the following:",
            "statements": [
                "The power to legislate on residuary subjects.",
                "The appointment and removal of Governors of States.",
                "The composition and powers of the Inter-State Council.",
                "The principles governing the distribution of tax revenues between the Centre and the States."
            ],
            "final_statement": "How many of the above reflect the Union Government's dominance in Centre-State relations in India?",
            "choices": [
                "Only One",
                "Only Two",
                "Only Three",
                "Only Four"
            ]
        },

    },
    {
        "en": {
            "question": "Consider the following statements:",
            "statements": [
                "Article 263 of the Indian Constitution mandates the establishment of an Inter-State Council only upon the recommendation of the Sarkaria Commission.",
                "The recommendations of the Punchhi Commission on Centre-State relations suggest that the Governor of a state should not be burdened with the Chancellorship of universities."
            ],
            "final_statement": "Which of the statements given above is/are correct?",
            "choices": [
                "1 only",
                "2 only",
                "Both 1 and 2",
                "Neither 1 nor 2"
            ],
            "correct_answer": "b",
            "explanation": "Statement 1 is incorrect. Article 263 empowers the President to establish an Inter-State Council if he feels that such a council would serve the public interest. The Sarkaria Commission (1983-1988) did recommend the establishment of a permanent Inter-State Council under Article 263. However, Article 263 itself does not mandate the establishment of the council only upon the recommendation of the Sarkaria Commission. The President can act independently based on his assessment of the public interest. The Inter-State Council was first established in 1990. Article 263 states: \"If at any time it appears to the President that the public interests would be served by the establishment of a Council charged with the duty of (a) inquiring into and advising upon disputes which may have arisen between States; (b) investigating and discussing subjects in which some or all of the States, or the Union and one or more of the States, have a common interest; or (c) making recommendations upon any such subject and, in particular, recommendations for the better co-ordination of policy and action with respect to that subject, it shall be lawful for the President by order to establish such a Council, and to define the nature of the duties to be performed by it and its organization and procedure.\"\n\nStatement 2 is correct. The Punchhi Commission (2007-2010) on Centre-State relations made several recommendations to improve the functioning of the federal system. One of its recommendations was that the Governor of a state should not be burdened with the Chancellorship of universities. The Commission argued that the Governor's role as Chancellor often involves them in the day-to-day administration of the universities, which can compromise their impartiality and neutrality. The Punchhi Commission felt that the Governor should be free from such responsibilities to focus on their constitutional duties as the head of the state. This recommendation stems from a broader concern about maintaining the Governor's non-partisan role and avoiding unnecessary conflicts with the state government. The Commission noted the potential for friction when the Governor, as Chancellor, is involved in university affairs, especially concerning appointments and policy decisions. Therefore, they recommended separating these roles to ensure the Governor's focus remains on their constitutional responsibilities and to minimize potential areas of conflict between the Governor and the state government. This separation is intended to enhance the Governor's ability to act as a neutral arbiter and advisor to the state government, promoting smoother Centre-State relations and better governance within the state."
        }
    },
]


def create_pdf():
    latex_code = create_latex_template(questions)
    return latex_code
