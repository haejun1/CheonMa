import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import HomeComponent from "./components/HomeComponent";
import Page1Component from "./components/Page1Component";
import Page2Component from "./components/Page2Component";
import Page3Component from "./components/Page3Component";
import Page4Component from "./components/Page4Component";

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/page1">Page 1</Link>
            </li>
            <li>
              <Link to="/page2">Page 2</Link>
            </li>
            <li>
              <Link to="/page3">Page 3</Link>
            </li>
            <li>
              <Link to="/page4">Page 4</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<HomeComponent />} />
          <Route path="/page1" element={<Page1Component />} />
          <Route path="/page2" element={<Page2Component />} />
          <Route path="/page3" element={<Page3Component />} />
          <Route path="/page4" element={<Page4Component />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
