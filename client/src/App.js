import React from "react";
import Navbar from "./components/Navbar/Navbar";
import About from "./components/Pages/About";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import MyLibrary from "./components/Pages/MyLibrary";

const App = () => {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<About />}  />
          <Route path="/about" element={<About />}  />
          <Route path="/mylibrary" element={<MyLibrary />}  />
        </Routes>
      </Router>
    </div>
  );
};

export default App;
