document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chatForm');

    chatForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent the default form submission behavior
        submitForm();
    });
});

async function submitForm() {

    const inputElement = document.getElementById('chatMessage');
    const inputValue = inputElement.value.trim();

    if (inputValue !== '') {
        try {
            const response = await fetch('http://localhost:5000/123123', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: inputValue }),
            });

            if (response.ok) {
                const responseData = await response.json();
                updateOutputMessage(responseData.reply);
            } else {
                console.error('Error:', response.statusText);
            }
        } catch (error) {
            console.error('Error:', error.message);
        }

        // Clear the input box after submitting
        inputElement.value = '';
    }
}

function updateOutputMessage(sentence) {
    document.getElementById('outputMessage').value = sentence;
}
export default submitForm;
