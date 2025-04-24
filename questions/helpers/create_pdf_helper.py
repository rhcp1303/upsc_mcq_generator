def create_latex_template(questions):
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

        elif 'statements' in q['en']:
            latex_template += r"\begin{enumerate}[label=\arabic*., leftmargin=0.6cm, itemsep=0in]" + "\n"
            for s in q['en']['statements']:
                latex_template += r"\item " + s + r"" + "\n"
            latex_template += r"\end{enumerate}" + "\n"
            if 'final_statement' in q['en']:
                latex_template += q['en']['final_statement'] + r"\\" + "\n"

        if 'choices' in q['en']:
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
    indent_length = "2em"
    return r"\makebox[" + indent_length + r"][l]{" + number + r"}\RaggedRight\arraybackslash \hangindent=" + indent_length + r" " + \
        pair[0] + r" & \RaggedRight\arraybackslash \hangindent=0pt " + pair[1] + r" \\" + "\n"


questions = [{
    "en": {
        "question": "With reference to Centre-State relations in India, consider the following statements:",
        "statements": [
            "The Sarkaria Commission recommended the establishment of a permanent Inter-State Council under Article 263 of the Constitution, but proposed that its decisions should be binding on both the Union and the States.",
            "The Finance Commission's recommendations on the distribution of tax revenue between the Union and the States are binding on the Union Government, ensuring predictable and equitable resource allocation.",
            "Article 356 of the Constitution, concerning President's Rule, can only be invoked if there is a breakdown of constitutional machinery in the entire state, and not in a specific part or region of the state."
        ],
        "final_statement": "Which of the statements given above is/are correct?",
        "choices": [
            "Only one",
            "Only two",
            "All three",
            "None"
        ],
        "correct_answer": "d",
        "explanation": "Statement 1 is incorrect. While the Sarkaria Commission did recommend the establishment of a permanent Inter-State Council under Article 263, it specifically stated that the Council's recommendations should be advisory in nature, not binding. The intention was to foster cooperation and consultation, not to create a mechanism where the Union or States could be forced to comply with the Council's decisions. Making the decisions binding would potentially undermine the federal structure by limiting the autonomy of both the Union and the States to make their own policy choices within their respective spheres of competence. The Inter-State Council aims to promote dialogue and consensus-building, respecting the sovereignty of each level of government. \n\nStatement 2 is incorrect. The recommendations of the Finance Commission are advisory in nature, not binding. While the Union Government generally accepts and implements these recommendations, it retains the discretion to deviate from them. The Finance Commission, constituted under Article 280 of the Constitution, makes recommendations on the distribution of net proceeds of taxes between the Union and the States, and the principles governing grants-in-aid to the States out of the Consolidated Fund of India. However, the final decision on accepting and implementing these recommendations rests with the Union Government, subject to parliamentary approval. This allows the Union Government to consider broader economic and fiscal priorities while making resource allocation decisions. \n\nStatement 3 is incorrect. Article 356 can be invoked not only when there is a breakdown of constitutional machinery in the entire state, but also if such a breakdown occurs in a part of the state, making the overall governance of the state impossible to carry on in accordance with the provisions of the Constitution. While the general understanding is that Article 356 is invoked for the entire state, the Supreme Court has clarified through judicial pronouncements that a partial breakdown can also justify its imposition. This interpretation provides flexibility to the Union Government to address specific situations of constitutional crisis within a state without necessarily taking over the entire administration. However, the use of Article 356 remains a sensitive issue due to its potential for misuse and its impact on federalism."
    }
},
    {
        "en": {
            "question": "With reference to Centre-State relations, consider the following pairs:",
            "headings": [
                "Constitutional Provision",
                "Description"
            ],
            "pairs": [
                [
                    "Article 256",
                    "Union's power to give directions to a State as to the construction and maintenance of means of communication declared to be of national or military importance."
                ],
                [
                    "Article 257(4)",
                    "Deals with the power of the Union to entrust functions to a State government with the consent of that State government."
                ],
                [
                    "Article 258(2)",
                    "Deals with the power of the State to entrust functions to the Union government with the consent of that Union government."
                ],
                [
                    "Article 263",
                    "Establishment of an Inter-State Council if at any time it appears to the President that the establishment of such a Council would serve the public interests."
                ]
            ],
            "final_statement": "Which of the pairs given above is/are correctly matched?",
            "choices": [
                "1 and 4 only",
                "2 and 3 only",
                "1, 3 and 4 only",
                "1, 2, 3 and 4"
            ],
            "correct_answer": "a",
            "explanation": "Article 256: Obligation of States and the Union\nThe executive power of every State shall be so exercised as to ensure compliance with the laws made by Parliament and any existing laws which apply in that State, and the executive power of the Union shall extend to the giving of such directions to a State as may appear to the Government of India to be necessary for that purpose.\n\nArticle 257(2): The executive power of the Union shall also extend to the giving of directions to a State as to the construction and maintenance of means of communication declared in the direction to be of national or military importance.\n\nArticle 258(1): Notwithstanding anything in this Constitution, the President may, with the consent of the Government of a State, entrust either conditionally or unconditionally to that Government or to its officers functions in relation to any matter to which the executive power of the Union extends.\nArticle 258(2): A law made by Parliament which applies in any State may, notwithstanding that it relates to a matter with respect to which the Legislature of the State has no power to make laws, confer powers and impose duties, or authorise the conferring of powers and the imposition of duties, upon the State or officers and authorities thereof.\nArticle 263: Provisions with respect to an inter-State Council.\nIf at any time it appears to the President that the public interests would be served by the establishment of a Council for inquiring into and advising upon disputes which may have arisen between States; investigating and discussing subjects in which some or all of the States, or the Union and one or more of the States, have a common interest; or making recommendations upon any such subject and, in particular, recommendations for the better co-ordination of policy and action with respect to that subject, it shall be lawful for the President by order to establish such a Council, and to define the nature of the duties to be performed by it and the organisation and procedure thereof.\n\nTherefore, only pairs 1 and 4 are correctly matched. Article 257(4) doesn't exist and Article 258(2) is incorrectly described, and Article 263 is correctly described."
        }
    }
]


def create_pdf():
    latex_code = create_latex_template(questions)
    return latex_code
