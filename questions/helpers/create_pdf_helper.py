def create_latex_template_for_questions(questions):
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


def create_latex_template_for_solutions(questions):
    latex_template = r"""
    \documentclass[11pt,a4paper]{article}
    \usepackage[margin=0.7in, right=1in]{geometry} % Added right margin
    \usepackage{amsmath}
    \usepackage{amssymb}
    \usepackage{enumitem}
    \usepackage{ragged2e}
    \usepackage{needspace}
    \usepackage{array}
    \usepackage{tabularx}
    \usepackage{fontsize}
    \usepackage[none]{hyphenat}
    \usepackage{xcolor}

    \definecolor{solutioncolor}{rgb}{0.1, 0.5, 0.2}
    \setlength{\parindent}{0pt}

    \begin{document}

    \begin{multicols}{1}
    \RaggedRight

    \section*{\centering ANSWERS}
    \hrulefill
    \vspace{0.5cm}

    """

    for i, q in enumerate(questions):
        latex_template += r"\needspace{1\baselineskip}" + "\n"
        latex_template += r"\textbf{Q." + str(i + 1) + ".}" + r" "
        if 'correct_answer' in q['en']:
            latex_template += r"\textbf{\textcolor{solutioncolor}{" + q['en'][
                'correct_answer'].upper() + r"}}" + r"\\" + "\n"
        else:
            latex_template += "No Answer Provided\\" + "\n"
        latex_template += r"\vspace{0.1cm}" + "\n"

        if 'explanation' in q['en']:
            latex_template += q['en']['explanation'].replace("\n\n", "\n\n\\vspace{0.2cm}\n\n") + "\n"
            latex_template += r"\vspace{0.3cm}" + "\n"

    latex_template += r"""
    \end{multicols}

    \end{document}
    """
    return latex_template