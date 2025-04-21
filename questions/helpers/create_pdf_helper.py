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
                latex_template += r"\begin{center}"
                latex_template += r"\begin{tabular}{>{\RaggedRight}p{0.45\linewidth} >{\RaggedRight}p{0.45\linewidth}}"
                latex_template += r"\textbf{" + q['en']['headings'][0] + r"} & \textbf{" + q['en']['headings'][1] + r"} \\ \hline"
                for pair in q['en']['pairs']:
                    latex_template += pair_to_latex(pair)
                latex_template += r"\end{tabular}"
                latex_template += r"\end{center}"
            else:
                latex_template += r"\begin{enumerate}[label=\arabic*., leftmargin=0.6cm, itemsep=0in]"
                for i, pair in enumerate(q['en']['pairs']):
                    latex_template += r"\item " + str(i + 1) + ". " + pair[0] + r" : " + pair[1] + r""
                latex_template += r"\end{enumerate}"

        elif 'statements' in q['en']:  # Handle statements
            latex_template += r"\begin{enumerate}[label=\arabic*., leftmargin=0.6cm, itemsep=0in]"
            for s in q['en']['statements']:
                latex_template += r"\item " + s + r""
            latex_template += r"\end{enumerate}"

        if 'choices' in q['en']:  # Handle multiple choices
            latex_template += r"\begin{enumerate}[label=(\alph*), leftmargin=0.4cm, itemsep=0in]"
            for choice in q['en']['choices']:
                latex_template += r"\item " + choice + r""
            latex_template += r"\end{enumerate}"

        latex_template += r"\vspace{0.1in}"

    latex_template += r"""
\end{enumerate}

\end{multicols}

\end{document}
"""
    return latex_template

def pair_to_latex(pair):
    """Formats a pair for LaTeX table, handling line breaks."""
    return r"\RaggedRight " + pair[0] + r" & \RaggedRight " + pair[1] + r" \\"


questions = [
    {
        "en": {
            "question": "With reference to Centre-State Relations, consider the following pairs:",
            "headings": ["Committee/Commission", "Associated Recommendation"],
            "pairs": [
                ["Sarkaria Commission", "Permanent Inter-State Council under Article 263"],
                ["Punchhi Commission", "Regulation of deployment of Central Armed Forces in States"],
                ["Rajamannar Committee", "Abolition of All India Services"],
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