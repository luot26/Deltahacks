import startVideo from "./startVideo";
// Get the video element from the DOM
const videoElement = document.getElementById('video');

// Function to capture a picture and send it to the backend
function capturePicture(videoElement) {
    // Create a canvas element
    const canvas = document.createElement('canvas');
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;

    // Draw the current frame from the video onto the canvas
    const context = canvas.getContext('2d');
    context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

    // Convert the canvas image to a data URL
    const dataUrl = canvas.toDataURL('image/jpeg');

    // Send the data URL to the backend using an HTTP request (e.g., using fetch)
    fetch('/upload', {
        method: 'POST',
        body: JSON.stringify({ image: dataUrl }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the backend
            console.log('Response from backend:', data);
        })
        .catch(error => {
            console.error('Error sending image to backend:', error);
        });
}

// Call the startVideo function to begin the video stream
startVideo();

export default capturePicture;


