<h1>WIN OR BUST 🎲</h1>

<p>
  A tiny terminal game for two teams — <strong>Team A</strong> and <strong>Team B</strong> — written in Python.
  Each team has three players who enter numbers (1–200). Highest valid total <em>below the limit</em> wins.
</p>

<p>
  🔗 <strong>Repo:</strong>
  <a href="https://github.com/ahodot01/Game-1" target="_blank" rel="noopener noreferrer">
    https://github.com/ahodot01/Game-1
  </a>
</p>

<hr />

<h2>How to Play</h2>
<ul>
  <li>There are two teams: <strong>A</strong> and <strong>B</strong>.</li>
  <li>Each team has <strong>3 inputs</strong> (one per player) → total of <strong>6 numbers</strong> entered per round.</li>
  <li>Each number must be an <strong>integer between 1 and 200</strong>.</li>
  <li>You’ll be asked which team to assign the number to:
    <ul>
      <li>If a team already has 3 inputs, the game <em>auto-assigns</em> to the other team.</li>
    </ul>
  </li>
  <li><strong>Limit = 238</strong>:
    <ul>
      <li>If a team’s total &gt; 238 → that team <strong>busts</strong>.</li>
      <li>If both teams bust → <strong>draw</strong> and the round restarts.</li>
    </ul>
  </li>
</ul>

<h3>Scoring &amp; Prize</h3>
<ul>
  <li>If <strong>neither team busts</strong>: the team with the higher total wins; prize = that team’s total (in GBP).</li>
  <li>If <strong>one team busts</strong>: the other team wins; prize = <code>sum(Team A) + sum(Team B)</code>.</li>
  <li>If <strong>both bust</strong>: draw → automatic restart.</li>
  <li>If totals are <strong>exactly equal</strong> (and not bust): draw → automatic restart.</li>
</ul>

<hr />

<h2>Requirements</h2>
<ul>
  <li>Python 3.8+ (tested on 3.10/3.11/3.12)</li>
</ul>

<hr />

<h2>Run</h2>

<pre><code>python game_win_or_bust.py
</code></pre>

<p>
  If your file name is different, run:
</p>

<pre><code>python your_filename.py
</code></pre>

<hr />

<h2>Code Overview</h2>

<ul>
  <li><code>play_game()</code>: main game loop; validates input, assigns to teams, checks busts/draws, prints outcome.</li>
  <li><code>main()</code>: “Play again?” prompt; restarts the game or exits cleanly.</li>
</ul>

<p><em>Key behaviors:</em></p>
<ul>
  <li>Input validation for both the number (must be 1–200) and team (A/B).</li>
  <li>Automatic assignment when a team already has 3 inputs.</li>
  <li>Clear, step-by-step printouts for rules, scores, and outcomes.</li>
</ul>

<hr />

<h2>Sample Session</h2>

<pre><code>Welcome to WIN OR BUST game!

Rules: There are 2 teams: A and B. Each team has 3 players...
Number must be between 1 and 200.

Enter a number: 90
Add to Team A or B: A
Enter a number: 80
Add to Team A or B: B
...

Score of Team A is 230 and Score of Team B is 205.
Team A won. The prize is £230.

Play again? (Y/Yes/N/No/...):
</code></pre>

<hr />

<h2>License</h2>
<p><strong>License:</strong> PolyForm Noncommercial 1.0.0 (no commercial use). 
For commercial licensing, contact <a href="mailto:s.selection@gmail.com">s.selection@gmail.com</a>.</p>
