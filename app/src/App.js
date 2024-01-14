import './App.css';
import startVideo from './components/startVideo';
import capturePicture from './components/picture';
import submitForm from './components/enter';
import displayMsg from './components/displayMsg';

function App() {

  document.addEventListener('DOMContentLoaded', function () {
    fetch('/get_response')
    .then(response => response.json())
    .then(data => {
        document.getElementById('output-box').innerText = data.response;
    }).catch(error =>console.error('Error: ', error));
  });

  return (
    <div class="wrapper">
    <form action="">
        <h1>ChatBox</h1>
        <div class = "output-box">
            <input type="text" placeholder="Would you like to talk about your feelings?" readOnly />
            <displayMsg />
        </div>
        <div class = "input-box">
            <input type="text" id = "chatMessage" placeholder="Enter your message" required onKeyDown = {submitOnEnter}/>
            <startVideo />
            <capturePicture />
        </div>
    </form>
    </div>

  );

  function submitOnEnter(event) {
    if (event.key === "Enter") {
        submitForm();
    }
  }

  function updateOutputMessage(sentence) {
    document.getElementById('outputMessage').value = sentence;
  }
}

export default App;
