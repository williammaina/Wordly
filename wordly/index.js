const weatherApi = "https://api.dictionaryapi.dev/api/v2/entries/en/"

async function tosearchWord () {
  const wordForm  = document.getElementById('word-form').value;
  const displayArea = document.getElementById('display-word-meaning');

  // Basic validation to ensure a state code is entered
  if (!wordForm) {
    displayArea.innerHTML = '<p>Please enter a a word (e.g. cat ).</p>';
    return;
  }

  try {
    // 1. Fetch the data based on the state code
    const response = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${wordForm}`);
    
    if (!response.ok) throw new Error("Could not fetch the word.");

    const data = await response.json();

    // 2. Clear the display area for new results
    displayArea.innerHTML = '';

    const wordData = data[0];

  
    // 2. Display the Word and Phonetic (Main Header)
    const wordTitle = document.createElement('h1');
    wordTitle.textContent = `${wordData.word} [${wordData.phonetic || ''}]`;
    displayArea.appendChild(wordTitle);

    // 3. Loop through 'meanings' (Noun, Verb, etc.)
    wordData.meanings.forEach(meaning => {
     
      // Create a sub-header for the part of speech
      const partOfSpeech = document.createElement('h2');
      partOfSpeech.textContent = meaning.partOfSpeech;
      displayArea.appendChild(partOfSpeech);

      // Create a list for definitions under this part of speech
      const definitionList = document.createElement('ul');

      meaning.definitions.forEach(def => {
        const li = document.createElement('li');
        li.textContent = def.definition;
        li.style.color = "blue";
        li.style.alignContent ="center";
        //li.style.flexDirection ="column";

        
        
        // Optional: Add an example if it exists
        if (def.example) {
          const example = document.createElement('p');
          example.style.fontStyle = "italic";
          example.textContent = `Example: "${def.example}"`;
          li.appendChild(example);
        }

        definitionList.appendChild(li);
      });

      displayArea.appendChild(definitionList);
    });
  } catch (error) {
    console.error("Error:", error);
    displayArea.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
  }
}

// 8. Attach the function to the button
document.getElementById('submitBtn').addEventListener('click', tosearchWord);