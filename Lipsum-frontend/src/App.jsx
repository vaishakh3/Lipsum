import './App.css'
import Landing from './pages/Landing/Landing'
import Home from "./pages/Home/Home";
import Initial from "./pages/Initial/Initial";
import Quiz from './pages/Quiz/Quiz';

function App() {

  return (
    <div className="App">
      <Landing/>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Initial />} />
          <Route path="/Home" element={<Home />} />
          <Route path="/Quiz" element={<Quiz/>} />
        </Routes>

       </BrowserRouter>
    </div>
  )
}

export default App
