# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  The hints were not consistent. Some bugs that I ran into was that when it would say "higher" as a tip, it was actually lower. Another bug I ran into was that when it would say "lower", it was actually higher. The new game button also did not work, as in when I would run out of guesses, and try to restart the game, it didn't work appropriately. A bug that I noticed was that the number of guesses given for each difficulty did not make any sense, as in you had more guesses if you were on the Normal mode compared to the Easy mode.

  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used GitHub Copilot and Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  An AI suggestion that was correct was the hints being backwards. The AI suggested that the hint "higher" was actually lower, and the hint "lower" was actually higher. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  AI was incorrect, it tried to suggest tests that just failed. I verified the result by manually running the tests and making changes where it was necessary

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I had to see the physical application working appropriately and have a test working for it
- Describe at least one test you ran (manual or using pytest)  
I ran the test_parse_guess_rejects_none_and_blank() test and the goal for that test was to reject the guess if it didn't contain any characters
- Did AI help you design or understand any tests? How?
AI just helped me understand how to test the tests to verify that they were working appropriately

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
I think the secret number would change everytime I interacted with a button, like the Submit button for example
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
It essentially just rebuilds itself everytime you press a button. So think of it as rolling a dice everytime you interact with the website
- What change did you make that finally gave the game a stable secret number?
Storing the secret number in a session state after it was initialized

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  hmmm??
  Have AI try to catch some of these errors by itself, then manually verify these errors.
- What is one thing you would do differently next time you work with AI on a coding task?
  When I am working on AI as a coding task, I want it to act as a junior software engineer, doing majority of the coding, while I focus on the test cases, and ensuring the proposed changes actually work without breaking anything else
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I think that this project has helped me understand how to utilize AI not only as programming assistance or a search engine, but a tool that can improve how quickly I diagnose and fix different errors. I also didn't know that AI was good at writing decent tests for your code