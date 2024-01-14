// Get the video element from the DOM
const videoElement = document.getElementById('video');

// Function to start the video stream
async function startVideo() {

    try {
        // Request permission to access the camera
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });

        // Set the video source to the stream
        videoElement.srcObject = stream;
    } catch (error) {
        console.error('Error accessing camera:', error);
    }
}

export default startVideo;
