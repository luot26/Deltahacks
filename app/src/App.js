import './App.css';
import startVideo from './components/startVideo';
import capturePicture from './components/picture';
import getInput from './components/enter';

function App() {
  return (
    <div class="wrapper">
    <form action="">
        <h1>ChatBox</h1>
        <div class = "output-box">
            <input type="text" placeholder="..." readOnly />
        </div>
        <div class = "input-box">
            <input type="text" placeholder="Enter your message" required onKeyDown = "getInput(event)"/>
            <startVideo />
            <capturePicture />
        </div>
    </form>
    </div>
  );
}

export default App;
