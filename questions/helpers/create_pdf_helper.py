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

\begin{multicols}{2}
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
]


def create_pdf():
    latex_code = create_latex_template(questions)
    return latex_code