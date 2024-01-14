import './App.css';
import startVideo from './components/startVideo';
import capturePicture from './components/picture';
import submitForm from './components/enter';

function App() {
  
  return (
    <div class="wrapper">
    <form action="">
        <h1>ChatBox</h1>
        <div class = "output-box">
            <input type="text" placeholder="..." readOnly />
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
