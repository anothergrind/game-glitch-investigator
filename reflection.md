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
  Not available. The AI didn't halluncinate on me surprisingly

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I had to see the physical application working appropriately
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  hmmm??
  Have AI try to catch some of these errors by itself, then manually verify these errors.
- What is one thing you would do differently next time you work with AI on a coding task?
  When I am working on AI as a coding task, I want it to act as a junior software engineer, doing majority of the coding, while I focus on the test cases, and ensuring the proposed changes actually work without breaking anything else
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I think that this project has helped me understand how to utilize AI not only as programming assistance or a search engine, but a tool that can improve how quickly I diagnose and fix different errors