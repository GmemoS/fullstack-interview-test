import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "./index.css";
import { Navigation } from "./components/Navigation";
import { Branches } from "./components/Branches";
import { Commits } from "./components/Commits";
import {CommitDetail} from "./components/CommitDetail";

export function App() {
    return(
        <Router>
            <Navigation />
            <Routes>
                <Route path="/" element={<Branches />} />
                <Route path="/branch" element={<Commits />} />
                <Route path="/commit" element={<CommitDetail />} />
            </Routes>
        </Router>
    )
}
