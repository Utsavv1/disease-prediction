document.querySelectorAll('.symptom-btn').forEach(button => {
    button.addEventListener('click', () => {
      const inputField = document.getElementById('symptomsInput');
      let currentValue = inputField.value;

      // Add symptom only if it's not already in the input
      if (!currentValue.includes(button.dataset.symptom)) {
        inputField.value = currentValue 
                          ? currentValue + ', ' + button.dataset.symptom 
                          : button.dataset.symptom;
      }
    });
  });
  const startSpeechRecognitionButton = document.getElementById('startSpeechRecognition');
const symptomsInput = document.getElementById('symptomsInput'); // Correct input field reference

startSpeechRecognitionButton.addEventListener('click', startSpeechRecognition);

function startSpeechRecognition() {
    const recognition = new webkitSpeechRecognition(); // Speech recognition API
    recognition.lang = 'en-US'; // Set the language for recognition

    recognition.onresult = function (event) {
        const result = event.results[0][0].transcript;

        // Add the transcribed text to the symptoms input field
        if (symptomsInput.value.trim()) {
            symptomsInput.value += `, ${result}`; // Append to existing text
        } else {
            symptomsInput.value = result; // Add as the first symptom
        }
    };

    recognition.onerror = function (event) {
        console.error('Speech recognition error:', event.error);
    };

    recognition.onend = function () {
        console.log('Speech recognition ended.');
    };

    recognition.start();
}


document.querySelectorAll('.symptom-btn').forEach(button => {
    button.addEventListener('click', () => {
        let currentValue = symptomsInput.value;

        // Add symptom only if it's not already in the input
        if (!currentValue.includes(button.dataset.symptom)) {
            symptomsInput.value = currentValue 
                ? currentValue + ', ' + button.dataset.symptom 
                : button.dataset.symptom;
        }

        // Change the button color to green
        button.style.backgroundColor = 'green';
        button.style.color = 'white';

        // Optional: Add a 'selected' class for better control (CSS approach)
        button.classList.add('selected');
    });
});
  // Get references to the microphone icon and the start button
  const microphoneIcon = document.getElementById('microphoneIcon');

  // Add a click event listener to the microphone icon
  microphoneIcon.addEventListener('click', startSpeechRecognition);
  
  // Existing function for starting speech recognition
  function startSpeechRecognition() {
      const recognition = new webkitSpeechRecognition(); // Speech recognition API
      recognition.lang = 'en-US'; // Set the language for recognition
  
      recognition.onresult = function (event) {
          const result = event.results[0][0].transcript;
  
          // Add the transcribed text to the symptoms input field
          if (symptomsInput.value.trim()) {
              symptomsInput.value += `, ${result}`; // Append to existing text
          } else {
              symptomsInput.value = result; // Add as the first symptom
          }
      };
  
      recognition.onerror = function (event) {
          console.error('Speech recognition error:', event.error);
      };
  
      recognition.onend = function () {
          console.log('Speech recognition ended.');
      };
  
      recognition.start();
  }
  