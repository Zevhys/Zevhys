// ! Welcome, dear curious developer, to the abyss of my README Easter Egg.
// ! Remember: curiosity is a gift, but here it might just make you question reality.

(function () {
  const secretMessage = `
    ---------------------------------------------------------
    |  Hello, intrepid developer!                           |
    |                                                       |
    |  You've unearthed my secret JavaScript Easter Egg.    |
    |  Congratulations? Perhaps. Or maybe, just maybe,      |
    |  you’re procrastinating. Again.                       |
    |                                                       |
    |  Fear not; I’ve been there too. But while you’re here,|
    |  let’s make it count.                                 |
    |                                                       |
    |  🚀 Check out my projects, they might blow your mind. |
    |  (Or at least mildly impress you—same thing, right?)  |
    ---------------------------------------------------------
  `;

  const sarcasticWisdom = [
    "Why fix bugs when you can just comment them out? 💡🐛",
    "Code review: where all your dreams go to die. ⚰️😵‍💫",
    "Debugging is like being a detective in a crime movie where you are also the murderer. 🕵️‍♂️🔪",
    "Your worth is not defined by your code. Except during code reviews. 😂",
    "If it works, don't touch it. If it doesn't work, also don't touch it. 😉",
  ];

  console.log(secretMessage);
  console.log(
    "🤔 Random Developer Wisdom :\n ",
    sarcasticWisdom[Math.floor(Math.random() * sarcasticWisdom.length)]
  );

  console.log(`
PS : This console Easter egg will self-destruct in...
5.. 4.. 3... 2... 1...
  `);

  setTimeout(() => {
    console.log("\n".repeat(0));
    console.log("💥 Boom. It's gone. Just like your deadlines.");
  }, 5000);
})();
