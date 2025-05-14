document.addEventListener('DOMContentLoaded', () => {
    const submitBtn = document.getElementById('submitBtn');
    const confirmationModal = document.getElementById('confirmationModal');
    const confirmSubmitBtn = document.getElementById('confirmSubmitBtn');
    const cancelSubmitBtn = document.getElementById('cancelSubmitBtn');

    submitBtn.addEventListener('click', (event) => {
        event.preventDefault();
        confirmationModal.style.display = 'block';
    });

    cancelSubmitBtn.addEventListener('click', () => {
        confirmationModal.style.display = 'none';
    });

    confirmSubmitBtn.addEventListener('click', () => {
        confirmationModal.style.display = 'none';
        // Call the function in your main script to show results
        // Assuming the showResults() function is in 'test1_script.js'
        // You might need to adjust how you call it based on your script's scope.
        if (window.showResults) {
            window.showResults();
        } else {
            console.error("showResults function not found in the global scope.");
        }
    });

    window.addEventListener('click', (event) => {
        if (event.target === confirmationModal) {
            confirmationModal.style.display = 'none';
        }
    });
});

document.addEventListener('DOMContentLoaded', async () => {
    const startBtn = document.getElementById('startBtn');
    const questionContainer = document.getElementById('questionContainer');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');
    const resultsContainer = document.getElementById('resultsContainer');
    const scorecardFrame = document.getElementById('scorecardFrame');
    const scorecardContent = document.getElementById('scorecardContent');
    const header = document.querySelector('.header');
    const homeButton = document.getElementById('homeButton');
    const homeButtonFrame = document.getElementById('homeButtonFrame');
    const timerPanel = document.getElementById('timerPanel');
    const timerDisplay = document.getElementById('timer');

    let questions = [];
    let userAnswers = {};
    let currentQuestionIndex = 0;
    let timerInterval;
    let timeLeft;
    const testDuration = 1 * 60;
    const questionsPerPage = 100;

    async function fetchQuestions() {
        try {
            const response = await fetch('/api/test1');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const jsonData = await response.json();
            return jsonData.map(item => item.en);
        } catch (error) {
            console.error("Error fetching questions:", error);
            alert("Failed to load questions. Please check the API or network connection.");
            return [];
        }
    }

    function updateTimerDisplay() {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        timerDisplay.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    }

    function startTimer() {
        timeLeft = testDuration;
        updateTimerDisplay();
        timerPanel.style.display = 'block';
        timerInterval = setInterval(() => {
            timeLeft--;
            updateTimerDisplay();
            if (timeLeft <= 0) {
                clearInterval(timerInterval);
                showResults();
                alert("Time's up!");
            }
        }, 1000);
    }

    function stopTimer() {
        clearInterval(timerInterval);
    }

    startBtn.addEventListener('click', async () => {
        questions = await fetchQuestions();
        if (questions && questions.length > 0) {
            startQuiz();
            startTimer();
        }
    });

    function startQuiz() {
        startBtn.style.display = 'none';
        header.style.display = 'none';
        prevBtn.style.display = 'inline-block';
        nextBtn.style.display = 'inline-block';
        submitBtn.style.display = 'inline-block';
        homeButtonFrame.style.display = 'none';
        currentQuestionIndex = 0;
        userAnswers = {};
        scorecardFrame.style.display = 'none';
        questionContainer.style.display = 'block';
        resultsContainer.style.display = 'none';
        timerPanel.style.display = 'block';
        displayQuestion();
    }

    function displayQuestion() {
        questionContainer.innerHTML = '';
        const questionData = questions[currentQuestionIndex];
        if (!questionData) return;

        const questionNumberFrame = document.createElement('div');
        questionNumberFrame.className = 'question-number-frame';
        questionNumberFrame.textContent = `Q. ${currentQuestionIndex + 1} )`;
        questionContainer.appendChild(questionNumberFrame);

        const questionTextElement = document.createElement('h4');
        questionTextElement.innerHTML = questionData.question;
        questionContainer.appendChild(questionTextElement);

        // Handle statements if present
        if (questionData.statements && Array.isArray(questionData.statements) && questionData.statements.length > 0) {
            const statementsContainer = document.createElement('ol');
            statementsContainer.className = 'statements-list';
            questionData.statements.forEach((statement, index) => {
                const listItem = document.createElement('li');
                listItem.textContent = statement;
                statementsContainer.appendChild(listItem);
            });
            questionContainer.appendChild(statementsContainer);

            if (questionData.final_statement) {
                const finalStatementElement = document.createElement('p');
                finalStatementElement.className = 'final-statement';
                finalStatementElement.textContent = questionData.final_statement;
                questionContainer.appendChild(finalStatementElement);
            }
        }

        // Handle headings and pairs if present
        if (questionData.headings && Array.isArray(questionData.headings) && questionData.headings.length > 0 &&
            questionData.pairs && Array.isArray(questionData.pairs) && questionData.pairs.length > 0) {
            const table = document.createElement('table');
            table.className = 'pairs-table';
            table.classList.add(`cols-${questionData.headings.length}`);
            const thead = table.createTHead();
            const headerRow = thead.insertRow();
            headerRow.insertCell().textContent = '';
            questionData.headings.forEach(heading => {
                const th = document.createElement('th');
                th.textContent = heading;
                headerRow.appendChild(th);
            });
            const tbody = table.createTBody();
            questionData.pairs.forEach((pair, index) => {
                const tr = tbody.insertRow();
                const numberCell = tr.insertCell();
                numberCell.textContent = `${index + 1}.`;
                numberCell.className = 'pair-number';
                pair.forEach(value => {
                    const td = tr.insertCell();
                    td.textContent = value;
                });
                while (tr.cells.length < questionData.headings.length + 1) {
                    tr.insertCell();
                }
            });
            questionContainer.appendChild(table);

            if (questionData.final_statement) {
                const finalStatementElement = document.createElement('p');
                finalStatementElement.className = 'final-statement';
                finalStatementElement.textContent = questionData.final_statement;
                questionContainer.appendChild(finalStatementElement);
            }
        }

        const choices = questionData.choices || [];
        const options = ['a', 'b', 'c', 'd'].slice(0, choices.length);

        options.forEach((optionKey, index) => {
            const choiceText = choices[index];
            const optionBtn = document.createElement('button');
            optionBtn.className = 'option-btn';
            optionBtn.textContent = choiceText;
            optionBtn.dataset.option = optionKey;

            const optionNumberContainer = document.createElement('div');
            optionNumberContainer.className = 'option-number-container';
            optionNumberContainer.textContent = optionKey.toUpperCase();
            optionBtn.prepend(optionNumberContainer);

            if (userAnswers[currentQuestionIndex] === optionKey) {
                optionBtn.classList.add('selected');
            }

            optionBtn.addEventListener('click', () => {
                if (userAnswers[currentQuestionIndex] === optionKey) {
                    delete userAnswers[currentQuestionIndex];
                    optionBtn.classList.remove('selected');
                } else {
                    userAnswers[currentQuestionIndex] = optionKey;
                    document.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('selected'));
                    optionBtn.classList.add('selected');
                }
            });

            questionContainer.appendChild(optionBtn);
        });

        prevBtn.disabled = currentQuestionIndex === 0;
        nextBtn.disabled = currentQuestionIndex === questions.length - 1;
    }

    function nextQuestion() {
        if (currentQuestionIndex < questions.length - 1) {
            currentQuestionIndex++;
            displayQuestion();
        }
    }

    function prevQuestion() {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            displayQuestion();
        }
    }

    function showResults() {
        stopTimer();
        questionContainer.style.display = 'none';
        prevBtn.style.display = 'none';
        nextBtn.style.display = 'none';
        submitBtn.style.display = 'none';
        timerPanel.style.display = 'none';
        resultsContainer.style.display = 'block';
        homeButtonFrame.style.display = 'block';
        let resultsHTML = '';
        let score = 0;
        let correctCount = 0;
        let incorrectCount = 0;
        let attemptedCount = 0;

        questions.forEach((questionData, index) => {
            const correctAnswer = (questionData.correct_answer || '').toLowerCase();
            const userAnswer = userAnswers[index];
            const isCorrect = userAnswer === correctAnswer;

            resultsHTML += `
                <div class="question-result">
                    <div class="question-number-frame">Q. ${index + 1} )</div>
                    <p>${questionData.question}</p>
            `;

            // Display statements in results
            if (questionData.statements && Array.isArray(questionData.statements) && questionData.statements.length > 0) {
                const statementsContainer = document.createElement('ol');
                statementsContainer.className = 'statements-list';
                questionData.statements.forEach(statement => {
                    const listItem = document.createElement('li');
                    listItem.textContent = statement;
                    statementsContainer.appendChild(listItem);
                });
                resultsHTML += statementsContainer.outerHTML;
                if (questionData.final_statement) {
                    resultsHTML += `<p class="final-statement">${questionData.final_statement}</p>`;
                }
            }

            // Display pairs in results
            if (questionData.headings && Array.isArray(questionData.headings) && questionData.headings.length > 0 &&
                questionData.pairs && Array.isArray(questionData.pairs) && questionData.pairs.length > 0) {
                const table = document.createElement('table');
                table.className = 'pairs-table results-pairs-table';
                table.classList.add(`cols-${questionData.headings.length}`);
                const thead = table.createTHead();
                const headerRow = thead.insertRow();
                headerRow.insertCell().textContent = ''; // Empty cell for numbering
                questionData.headings.forEach(heading => {
                    const th = document.createElement('th');
                    th.textContent = heading;
                    headerRow.appendChild(th);
                });
                const tbody = table.createTBody();
                questionData.pairs.forEach((pair, index) => {
                    const tr = tbody.insertRow();
                    const numberCell = tr.insertCell();
                    numberCell.textContent = `${index + 1}.`;
                    numberCell.className = 'pair-number';
                    pair.forEach(value => {
                        const td = tr.insertCell();
                        td.textContent = value;
                    });
                    while (tr.cells.length < questionData.headings.length + 1) {
                        tr.insertCell();
                    }
                });
                resultsHTML += table.outerHTML;
                if (questionData.final_statement) {
                    resultsHTML += `<p class="final-statement">${questionData.final_statement}</p>`;
                }
            }

            const choices = questionData.choices || [];
            const options = ['a', 'b', 'c', 'd'].slice(0, choices.length);

            options.forEach((optionKey, index) => {
                const choiceText = choices[index];
                let className = 'option-btn';
                const correctOptionLetter = (questionData.correct_answer || '').toLowerCase();

                if (optionKey === correctOptionLetter) className += ' correct';
                if (optionKey === userAnswer && optionKey !== correctOptionLetter) className += ' incorrect';
                if (optionKey === userAnswer) className += ' selected';

                const optionBtn = `<button class="${className.trim()}" disabled>
                    <div class="option-number-container">${optionKey.toUpperCase()}</div>
                    ${choiceText}
                </button>`;
                resultsHTML += optionBtn;
            });

            resultsHTML += `<p class="explanation">Explanation: ${questionData.explanation ? questionData.explanation.replace(/\n/g, '<br>') : 'No explanation available.'}</p>`;
            resultsHTML += `</div>`;

            if (isCorrect) {
                score += 2;
                correctCount++;
                attemptedCount++;
            } else if (userAnswer) {
                score -= 2 / 3;
                incorrectCount++;
                attemptedCount++;
            }
        });

        scorecardContent.innerHTML = `
            <p><span class="scorecard-label">Score:</span><span class="scorecard-value">${score.toFixed(2)}</span></p>
            <p><span class="scorecard-label">Correct:</span><span class="scorecard-value">${correctCount}</span></p>
            <p><span class="scorecard-label">Incorrect:</span><span class="scorecard-value">${incorrectCount}</span></p>
            <p><span class="scorecard-label">Attempted:</span><span class="scorecard-value">${attemptedCount}</span></p>
            <p><span class="scorecard-label">Total:</span><span class="scorecard-value">${questions.length}</span></p>
        `;
        scorecardFrame.style.display = 'block';
        resultsContainer.innerHTML = resultsHTML;
    }

    window.showResults = showResults;
    prevBtn.addEventListener('click', prevQuestion);
    nextBtn.addEventListener('click', nextQuestion);
    homeButton.addEventListener('click', () => {
        window.location.href = "";
    });
});